import { Box, Button, Grid, HStack, Image, Text, useColorModeValue, VStack } from "@chakra-ui/react";
import { FaRegHeart, FaStar } from "react-icons/fa";

export default function Room() {
  const gray = useColorModeValue("gray.600", "gray.300");
  return (
    <VStack alignItems={"flex-start"}>
      <Box position="relative" overflow={"hidden"} mb={3} rounded="3xl">
        <Image
          h="100%"
          src="https://a0.muscache.com/im/pictures/prohost-api/Hosting-588591556733008349/original/109195e0-e466-4738-8f8c-10239fe44f59.jpeg?im_w=720"
        />
        <Button variant={"unstyled"} position="absolute" top={0} right={0} color="white">
          <FaRegHeart size="20px" />
        </Button>
      </Box>
      <Box>
        <Grid gap={2} templateColumns={"80fr 1fr"}>
          <Text display={"block"} as="b" noOfLines={1} fontSize="md" color={gray}>
            속초시, 한국
          </Text>
          <HStack spacing={1}>
            <FaStar size={15} />
            <Text>5.0</Text>
          </HStack>
        </Grid>
        <Text fontSize={"sm"} color={gray}>
          <Text as="b">₩188,400 / 박</Text>
        </Text>
      </Box>
    </VStack>
  );
}
