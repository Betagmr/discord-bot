from discord.ext.commands import Context, command


@command(name="play")
async def execute_command(ctx: Context) -> None:
    await ctx.send("Has ejecutado el comando play")
