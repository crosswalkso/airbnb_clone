import { Box, Grid, GridItem, HStack, Image, Text, VStack } from "@chakra-ui/react";
import { FaStar } from "react-icons/fa";

export default function Home() {
  return (
    <Grid mt={10} px={40} columnGap={4} rowGap={8} templateColumns="repeat(4, 1fr)">
      <VStack alignItems={"flex-start"}>
        <Box overflow={"hidden"} mb={3} rounded="3xl">
          <Image
            h="100%"
            src="https://a0.muscache.com/im/pictures/prohost-api/Hosting-588591556733008349/original/109195e0-e466-4738-8f8c-10239fe44f59.jpeg?im_w=720"
          />
        </Box>
        <Box>
          <Grid gap={2} templateColumns={"6fr 1fr"}>
            <Text display={"block"} as="b" noOfLines={1} fontSize="md">
              속초시, 한국
            </Text>
            <HStack spacing={1}>
              <FaStar size={15} />
              <Text>5.0</Text>
            </HStack>
          </Grid>
          <Text fontSize={"sm"} color="gray.600">
            <Text as="b">₩188,400 / 박</Text>
          </Text>
        </Box>
      </VStack>
    </Grid>
  );
}
