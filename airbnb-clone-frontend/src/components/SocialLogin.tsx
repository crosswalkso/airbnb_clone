import { FaComment, FaGithub } from "react-icons/fa";
import { Box, Button, Divider, HStack, Text } from "@chakra-ui/react";

export default function SocialLogin() {
  const kakaoParams = {
    client_id: "f7447e07ca9b4ab2947c87956bc91b5c",
    redirect_uri: "http://127.0.0.1:3000/social/kakao",
    response_type: "code",
  };
  const params = new URLSearchParams(kakaoParams).toString();
  console.log(params);
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
        <Button
          as="a"
          href="https://github.com/login/oauth/authorize?client_id=54c6b7dbb39c88e1e0b8&scope=read:user,
          user:email"
          leftIcon={<FaGithub />}
          bg="gray.300"
        >
          Continue with Github
        </Button>
        <Button
          as="a"
          href={`https://kauth.kakao.com/oauth/authorize?${params}`}
          leftIcon={<FaComment />}
          colorScheme={"yellow"}
        >
          Continue with Kakao
        </Button>
      </HStack>
    </Box>
  );
}
