from django.db import transaction
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Perk, Experience
from .serializers import PerkSerializer, ExperienceSerializer, ExperienceDetailSerializer

from categories.models import Category
from bookings.models import Booking
from bookings.serializers import PublicBookingSerializer, CreateRoomBookingSerializer

class Experiences(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_experiences = Experience.objects.all()
        serializer = ExperienceSerializer(all_experiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be experience")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            experience = serializer.save(
                host=request.user,
                category=category,
            )
            perks = request.data.get("perks")
            if perks:
                for perk_pk in perks:
                    perk = Perk.objects.get(pk=perk_pk)
                    experience.perks.add(perk)
            serializer = ExperienceSerializer(experience)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ExperienceDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience,
            context={"request":request},
        )
        return Response(serializer.data)


    def put(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        serializer = ExperienceDetailSerializer(
            experience,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():

            category_pk = request.data.get("category")
            if category_pk:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be experience")
            
            with transaction.atomic():
                if 'category' in locals():
                    experience = serializer.save(
                        host=request.user,
                        category=category,
                    )
                else:
                    experience = serializer.save(host=request.user)

                perks = request.data.get("perks")
                print(perks)
                try:
                    if perks:
                        experience.perks.clear()
                        for perk_pk in perks:
                            perk = Perk.objects.get(pk=perk_pk)
                            experience.perks.add(perk)
                except Exception:
                    raise ParseError("perk not found")

                serializer = ExperienceDetailSerializer(
                    experience,
                    context={"request":request},
                )
                return Response(serializer.data)
        
            
        else:
            Response(serializer.errors)
        

    def delete(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class ExperienceBookings(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except:
            raise NotFound
    
    def get(self, request, pk):
        experience = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        bookings = Booking.objects.filter(
            experience=experience,
            check_in__gt=now,
        )
        
        serializer = PublicBookingSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        experience = self.get_object(pk)
        serializer = CreateRoomBookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(
                experience=experience,
                user=request.user,
                kind=Booking.BookingKindChoices.EXPERIENCE,
            )
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ExperienceBookingDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound("experience")

    def get_booking(self, booking_pk):
        try:
            return Booking.objects.get(pk=booking_pk)
        except Booking.DoesNotExist:
            raise NotFound("booking")

    def get(self, request, pk, booking_pk):
        try:
            experience = self.get_object(pk)
            now = timezone.localtime(timezone.now()).date()
            booking = Booking.objects.filter(experience=experience, pk=booking_pk, check_in__gt=now)[0]
            
            serializer = PublicBookingSerializer(booking)
            
            return Response(serializer.data)
        except :
            raise ParseError("예약이 없습니다.")

    
    def put(self, request, pk, booking_pk):
        experience = self.get_object(pk)
        now = timezone.localtime(timezone.now()).date()
        booking = Booking.objects.filter(experience=experience, pk=booking_pk, check_in__gt=now)[0]
        serializer = CreateRoomBookingSerializer(
            booking,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            booking = serializer.save(user=request.user)
            serializer = PublicBookingSerializer(booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, booking_pk):
        booking = self.get_booking(booking_pk)
        booking.delete()
        return Response(HTTP_204_NO_CONTENT)
    
        

class Perks(APIView):

    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(
                PerkSerializer(perk).data,
                )
        else:
            return Response(serializer.errors)

class PerkDetail(APIView):

    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(
                PerkSerializer(updated_perk).data,
                )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)