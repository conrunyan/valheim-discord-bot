#!/usr/bin/env python
"""
MIT License

Copyright (c) 2021 Connor Runyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import discord
import os

from dotenv import load_dotenv

load_dotenv()

BOT_KEY = os.getenv("TOKEN")
client = discord.Client()


def main():
    client.run(BOT_KEY)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    clean_content = message.content.lower().strip()
    if clean_content.startswith("$valheim"):
        output_message = handle_input(clean_content)
        await message.channel.send(output_message)


def handle_input(message: str) -> str:
    """Generates an output message depending on what is received.

    Args:
        message (str): Raw message received straight from Discord.

    Returns:
        str: Output message to be sent back to discord.
    """
    message_pieces = message.split()
    if len(message_pieces) > 1:
        action = message_pieces[1]
        if action == "help":
            return usage()
        elif action == "players":
            return "Players!"
        elif action == "status":
            return "Status!"
        else:
            return "By Odin's beard... your language confuses me. (Try '$valheim help' for a list of actions)"
    # Input isn't in the right format! better display the help message
    else:
        return usage()

def usage() -> str:
    return """
Usage: $valheim [action]

Valid actions:
    players - Shows a list of players currently online.
    status - Shows current server status.
    help - Shows this message.

Example:
    $valheim players
"""

if __name__ == "__main__":
    main()
