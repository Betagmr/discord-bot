from discord.ext.commands import Context, command


@command(name="hello")
async def execute_command(ctx: Context) -> None:
    await ctx.send("Has ejecutado el comando hello, felicidades")
