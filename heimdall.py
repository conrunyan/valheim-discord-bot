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
import logging
import os
import sys

from dotenv import load_dotenv

from valheim_server_tools import (
    get_active_players,
    format_active_player_message,
    get_server_status,
    get_server_info
)


SYS_LOG = "/var/log/syslog"
client = discord.Client()
logger = logging.getLogger(__name__)


def main():
    load_dotenv()
    start_logger()
    bot_key = os.getenv("TOKEN")
    logger.info("Starting up Heimdall discord bot!")
    client.run(bot_key)


@client.event
async def on_ready():
    logger.info(f"Bot logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    clean_content = message.content.lower().strip()
    if clean_content.startswith("$valheim"):
        logger.info(f"Received message '{clean_content}'' from user '{message.author}'")
        output_message = handle_input(clean_content)
        logger.info(f"Responding with '{output_message}'")
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
            try:
                active_players = get_active_players(SYS_LOG)
            except PermissionError as e:
                msg = f"Could not access file '{SYS_LOG}'\nThe bot did not have permission to read this file, which contains player activity information."
                logger.error(msg, e)
                return msg
            if active_players:
                return format_active_player_message(active_players)
            return "No souls currently walk these lands..."
        elif action == "status":
            return get_server_status()
        elif action == "info":
            return get_server_info()
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
    info - Shows current server name and ip address.
    help - Shows this message.

Example:
    $valheim players
"""


def start_logger():
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)


if __name__ == "__main__":
    main()
