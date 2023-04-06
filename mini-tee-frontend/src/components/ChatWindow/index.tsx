import { Input, Box, Container, Stack, Button, Card } from '@mui/material'
import React, { SyntheticEvent } from 'react'
import useSWR from "swr"

type Message = {
    user: UserType;
    body: string;
}

type UserType = 'USER'|'TUTOR'

const fetchTutorResponse = async (input: string):Promise<string> => {
    console.log("request - ", input)
    return await fetch("http://localhost:8888/messages", {
        method: "POST",
        body: JSON.stringify(input),
        headers: {
            "Content-Type": "application/json",
          },
    }).then((res) => res.text());
}

export const ChatWindow = () => {
    const [chatThread, setChatThread] = React.useState<Message[]>([])
    const [isLoading, setIsLoading] =  React.useState<boolean>(false)

 
    
    const handleSubmit = async (event: SyntheticEvent<HTMLFormElement>) => {
        event.preventDefault()
        
        const userInput = event.currentTarget.userInput.value
        const userMessage = {
            body: userInput,
            user: "USER" as UserType
        }
    
        const awaitTutorMessage = {
            body: "...",
            user: "TUTOR" as UserType
        }
        setChatThread([...chatThread, userMessage, awaitTutorMessage])

        const response = await fetchTutorResponse(userInput)
        const tutorMessage = {
            body: response,
            user: "TUTOR" as UserType
        }

        const thread = chatThread.slice(0, -1)

        setChatThread([...thread, tutorMessage])
        console.log(response)

    }

    return (
        <Box>
            <Stack>
                <Box>header</Box>
                <Box>
                    <Stack component="ul">
                        {chatThread.map((message) => {
                            return <Card component="li" key={message.body}>{message.body}</Card>
                        })}
                    </Stack>
                </Box>
                <Box sx={{border:"1px solid black", padding: "1em"}}>
                    <form onSubmit={handleSubmit}>
                    <Input name="userInput" placeholder="Ask for Help"/>
                    <Button type="submit">submit</Button>
                    </form>
                </Box>
            </Stack>
        </Box>
    ) 
}


