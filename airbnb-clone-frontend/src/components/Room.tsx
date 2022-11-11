import { Box, Button, Grid, HStack, Image, Text, useColorModeValue, VStack } from "@chakra-ui/react";
import { FaRegHeart, FaStar } from "react-icons/fa";

interface IRoomProps {
  imageUrl: string;
  name: string;
  rating: number;
  price: number;
}

export default function Room({ imageUrl, name, rating, price }: IRoomProps) {
  const gray = useColorModeValue("gray.600", "gray.300");
  return (
    <VStack alignItems={"flex-start"}>
      <Box position="relative" overflow={"hidden"} mb={3} rounded="3xl">
        <Image h="100%" src={imageUrl} />
        <Button variant={"unstyled"} position="absolute" top={0} right={0} color="white">
          <FaRegHeart size="20px" />
        </Button>
      </Box>
      <Box>
        <Grid gap={2} templateColumns={"80fr 1fr"}>
          <Text display={"block"} as="b" noOfLines={1} fontSize="md" color={gray}>
            {name}
          </Text>
          <HStack spacing={1}>
            <FaStar size={15} />
            <Text>{rating}</Text>
          </HStack>
        </Grid>
        <Text fontSize={"sm"} color={gray}>
          <Text as="b">₩{price} / 박</Text>
        </Text>
      </Box>
    </VStack>
  );
}
