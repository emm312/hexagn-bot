
# initialise the library
from discord.ext import commands
import os

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
        await ctx.send("Please provide code to compile or put your code in codeblocks.")


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
        


#run the bot with the token in the.env file
import dotenv
dotenv.load_dotenv()
print(os.getenv("DISCORD_TOKEN"))
bot.run(os.getenv("DISCORD_TOKEN"))
