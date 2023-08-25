from src.bot import get_bot
from src.settings import DISCORD_PREFIX, DISCORD_TOKEN

bot = get_bot(DISCORD_PREFIX)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Number of commands loaded: {len(bot.commands)}")


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
