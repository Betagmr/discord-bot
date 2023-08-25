from discord.ext.commands import Context, command


@command(name="ping")
async def execute_command(ctx: Context) -> None:
    await ctx.send("pong")
