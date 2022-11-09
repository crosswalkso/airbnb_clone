import { FaComment, FaGithub } from "react-icons/fa";
import { Box, Button, Divider, HStack, Text } from "@chakra-ui/react";

export default function SocialLogin() {
  return (
    <Box mb={4}>
      <HStack my={8}>
        <Divider />
        <Text textTransform={"uppercase"} color="gray.500" fontSize="xs" as="b">
          Or
        </Text>
        <Divider />
      </HStack>
      <HStack>
        <Button leftIcon={<FaGithub />} bg="gray.300">
          Continue with Github
        </Button>
        <Button leftIcon={<FaComment />} colorScheme={"yellow"}>
          Continue with Kakao
        </Button>
      </HStack>
    </Box>
  );
}
