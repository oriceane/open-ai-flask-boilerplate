import { Input, Box, Container, Stack, Button, Card, createTheme } from '@mui/material'
import React, { SyntheticEvent } from 'react'
import useSWR from "swr"

export const InfoBoard = () => {

    return (
        <Box
            sx={{
                height: "100vh",
                backgroundColor: '#FFE8DE',
            }}
        >
            <Box sx={{
                padding: "15% 0 0 0"
            }}>
                <img src="/lung.png" alt="lung" width="500" />
            </Box>
            
        </Box>
    )
}


