import importlib.util as dynamic_import
from pathlib import Path

import discord
from discord.ext import commands
from discord.ext.commands import Bot


def get_bot(discord_prefix: str) -> Bot:
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix=discord_prefix, intents=intents)
    _load_commands(bot)

    return bot


def _load_commands(bot: Bot) -> None:
    command_folder = Path().cwd() / "src" / "commands"

    for group_folder in command_folder.iterdir():
        if group_folder.is_dir() and group_folder.name != "__pycache__":
            for command_file in group_folder.iterdir():
                if (
                    command_file.is_file()
                    and command_file.name.endswith(".py")
                    and command_file.name != "__init__.py"
                ):
                    file_name = command_file.name[:-3]
                    command = _import_command(file_name, str(command_file))
                    bot.add_command(command)


def _import_command(module_name: str, file_path: str) -> callable:
    spec = dynamic_import.spec_from_file_location(module_name, file_path)
    module = dynamic_import.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.execute_command
