import { Button, Heading, Text, VStack } from "@chakra-ui/react";
import { Link } from "react-router-dom";

export default function NotFound() {
  //   return <h1>404 Not Found Error</h1>;
  return (
    <VStack bg="green.100" minH="100vh" justifyContent={"center"}>
      <Heading>Page not found.</Heading>
      <Text>It seems that you're lost.</Text>
      <Link to="/">
        <Button colorScheme={"twitter"} variant={"solid"}>
          Go home
        </Button>
      </Link>
    </VStack>
  );
}
