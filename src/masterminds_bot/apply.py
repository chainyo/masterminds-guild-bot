"""The apply command for the bot."""

import discord
from discord import app_commands


@app_commands.command(name="apply", description="Start an apply to Masterminds EU.")
async def apply_command(interaction: discord.Interaction) -> None:
    """Apply command."""
    pass
