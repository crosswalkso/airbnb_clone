from django.contrib import admin
from .models import Review

# Register your models here.

class ScoreFilter(admin.SimpleListFilter):
    title = "Filter by score!"
    parameter_name = "score"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]
    def queryset(self, request, reviews):
        feel = self.value()
        if feel == "bad":
            return reviews.filter(rating__lt=3)
        elif feel == "good":
            return reviews.filter(rating__gte=3)

class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "potato"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]
 
    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        WordFilter,
        ScoreFilter,
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )