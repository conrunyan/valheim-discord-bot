#!/usr/bin/env python
import discord
import os

from dotenv import load_dotenv
load_dotenv()

BOT_KEY = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Hi there!")

client.run(BOT_KEY)