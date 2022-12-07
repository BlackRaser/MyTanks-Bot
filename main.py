#Lib
import datetime
import logging
import os
from ensurepip import version

import discord
from colorama import Back, Fore, Style
from dotenv import load_dotenv

#Logging
logging.basicConfig(level=logging.INFO, filename="events.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready ():
    print("\nMyTanks Discord Bot ONLINE\n")

#Help
help = (os.getenv('help') + "v.: "  + os.getenv('version') + "." + os.getenv('build'))

#Commands
class comands:
    @bot.command (name = "hello", description = "Say hello to the bot!")
    async def hello(ctx):
        author = str(ctx.author.id)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        print(f" * hello использовал пользователь " + author)
        logging.info(f"Command 'hello' using by " + author)

    @bot.command (name = 'help', descripton = 'Information about bot')
    async def help(ctx):
        author = str(ctx.author.id)
        await ctx.respond(help)
        print(f" * help использовал пользователь " + author)
        logging.info(f"Command 'help' using by " + author)

    @bot.command(name = 'ping', description="Возвращает задержку бота") 
    async def ping(ctx): 
        author = str(ctx.author.id)
        await ctx.respond(f"Ping!\nLatency is **{round(bot.latency * 1000)} ms**!")
        print(f" * ping использовал пользователь " + author)
        logging.info(f"Command 'ping' using by " + author)

bot.run(os.getenv('TOKEN'))