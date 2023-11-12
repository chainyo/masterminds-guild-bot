"""Main module for the masterminds_bot package."""

import asyncio
import logging
import logging.handlers
import os
from typing import Union

import discord
from aiohttp import ClientSession
from discord import app_commands
from dotenv import load_dotenv

from .apply import apply_command
from .weekly_goals import weekly_goals_command

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MastermindsBot(discord.Client):
    """Masterminds discord bot."""
    def __init__(
        self,
        web_client: ClientSession,
        intents: Union[discord.Intents, None] = None,
    ):
        """Client initialization."""
        if intents is None:
            intents = discord.Intents.default()
        intents.members = True

        super().__init__(intents=intents)

        self.web_client = web_client
        self.tree = app_commands.CommandTree(self)


    async def on_ready(self) -> None:
        """On ready event."""
        await self.wait_until_ready()
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

    async def on_guild_join(self, guild: discord.Guild) -> None:
        """On guild join."""
        await self.tree.sync(guild=guild)

    async def setup_hook(self) -> None:
        """Setup Hook."""
        # self.tree.add_command(login)
        await self.tree.sync()


async def main():
    """Main function."""
    async with ClientSession() as web_client:
        async with MastermindsBot(
            web_client=web_client,
        ) as client:
            await client.start(os.getenv("DISCORD_TOKEN", ""))


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
