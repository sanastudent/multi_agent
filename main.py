
from agent import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Welcome to the Multi-Agent system! How can i assist you today?").send()
    
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = asyncio.run(myAgent(user_input))
    await cl.Message(
        content=f"{response}"
    ).send()


