import { Input, Box, Container, Stack, Button, Card } from "@mui/material";
import React, { SyntheticEvent } from "react";
import useSWR from "swr";

type Message = {
  user: UserType;
  body: string;
};

type UserType = "USER" | "TUTOR";

const fetchTutorResponse = async (input: string): Promise<string> => {
  console.log("request - ", input);
  return await fetch("http://localhost:8888/messages", {
    method: "POST",
    body: JSON.stringify(input),
    headers: {
      "Content-Type": "application/json",
    },
  }).then((res) => res.text());
};

export const ChatWindow = () => {
  const [chatThread, setChatThread] = React.useState<Message[]>([]);
  const [isLoading, setIsLoading] = React.useState<boolean>(false);

  const handleSubmit = (event: SyntheticEvent<HTMLFormElement>) => {
    event.preventDefault();

    const userInput = event.currentTarget.userInput.value;
    const userMessage = {
      body: userInput,
      user: "USER" as UserType,
    };

    const loadingMessage = {
      body: "...",
      user: "TUTOR" as UserType,
    };
    const newThreadState = [...chatThread, userMessage, loadingMessage];
    setChatThread(newThreadState);

    fetchTutorResponse(userInput).then((response) => {
      const tutorMessage = {
        body: response,
        user: "TUTOR" as UserType,
      };
      console.log(chatThread);

      setChatThread([...newThreadState.slice(0, -1), tutorMessage]);
    });
    event.currentTarget.userInput.value = "";
  };

  return (
    <Box>
      <Stack>
        <Box
          sx={{ height: "5vh", backgroundColor: "#01918A", display: "flex" }}
        ></Box>
        <Box>
          <Stack
            component="ul"
            spacing="1em"
            sx={{ height: "80vh", overflow: "scroll", padding: ".5em" }}
          >
            {chatThread.map((message) => {
              const isTutor = message.user === "TUTOR";

              return (
                <div
                  style={{
                    display: "flex",
                    justifyContent: isTutor ? "left" : "right",
                  }}
                >
                  <Message
                    body={message.body}
                    isTutor={isTutor}
                    key={message.body}
                  />
                </div>
              );
            })}
          </Stack>
        </Box>
        <Box sx={{ border: "1px solid black", padding: "1em", height: "5vh" }}>
          <form
            onSubmit={handleSubmit}
            style={{
              display: "flex",
              justifyContent: "space-between",
              padding: ".5em",
            }}
          >
            <div style={{ width: "70%" }}>
              <Input name="userInput" placeholder="Ask for Help" fullWidth />
            </div>
            <Button type="submit">submit</Button>
          </form>
        </Box>
      </Stack>
    </Box>
  );
};

const Message = ({ body, isTutor }) => {
  const styles = {
    backgroundColor: isTutor ? "#F7F2ED" : "#01918A",
    textAlign: isTutor ? "left" : "right",
    justifySelf: isTutor ? "flexStart" : "flexEnd",
    color: isTutor ? "black" : "white",
    padding: "1em",
    width: "50%",
  };

  return (
    <Card sx={styles} component="li">
      {body}
    </Card>
  );
};
