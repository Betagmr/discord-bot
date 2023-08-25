import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")
DISCORD_PREFIX: str = os.getenv("DISCORD_PREFIX")
