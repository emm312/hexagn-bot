
# initialise the library
from discord.ext import commands
import os

# initialise the bot with the token OTQ3OTYxMzcwMjExNjU5Nzc2.Yh030g.Msw8EpuDwo4H-XlAGk9tOF_EqYk
bot = commands.Bot(command_prefix='!')

@bot.command("compile-to-urcl")
async def compile_to_urcl(ctx):
    try:
        code = ctx.message.content.split("```")[1]
        await ctx.send("Compiling to URCL")
        with open("code.hxgn", "w") as file:
            file.write(code)
        os.system("hexagn.exe code.hxgn")
        with open("out.urcl", "r") as file:
            await ctx.send("```"+file.read()+"```")
    except IndexError:
        await ctx.send("Please provide code to compile")


@bot.command("emulate-hexagn")
async def emulate_hexagn(ctx):
    # first, compile the code to URCL
    try:
        code = ctx.message.content.split("```")[1]
        await ctx.send("Compiling to URCL")
        with open("code.hxgn", "w") as file:
            file.write(code)
        os.system("hexagn.exe code.hxgn")
        with open("out.urcl", "r") as file:
            urcl = file.read()
        await ctx.send("Compiled to URCL, now emulating")
        ctx.send("```not added```")
    except IndexError:
        await ctx.send("Please provide code to compile")
        


bot.run("OTQ3OTYxMzcwMjExNjU5Nzc2.Yh030g.Msw8EpuDwo4H-XlAGk9tOF_EqYk")