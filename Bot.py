#Lib
import datetime
import sys
import logging
import os
from ensurepip import version

import discord
from colorama import Back, Fore, Style
from dotenv import load_dotenv

#Logging
logging.basicConfig(level=logging.INFO, filename="events.log", format="%(asctime)s : %(levelname)s : %(message)s")

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready ():
    print("\nMyTanks Discord Bot ONLINE\n")
    logging.warning('MyTanks Discord Bot ONLINE')

#Help
help = (os.getenv('help') + "v.: "  + os.getenv('version') + "." + os.getenv('build'))

#Commands
class comands:
    @bot.command (name = "hello", description = "Say hello to the bot!")
    async def hello(ctx):
        author = str(ctx.author.id)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        print(f" * hello использовал пользователь {author}")
        logging.info(f"Command 'hello' using by {author}")

    @bot.command (name = 'help', descripton = 'Information about bot')
    async def help(ctx):
        author = str(ctx.author.id)
        await ctx.respond(help)
        print(f" * help использовал пользователь {author}")
        logging.info(f"Command 'help' using by {author}")

    @bot.command(name = 'ping', description="Возвращает задержку бота") 
    async def ping(ctx): 
        author = str(ctx.author.id)
        latency = round(bot.latency*1000)
        latency=str(latency)
        logging.info(f"Latency is {latency} ms")
        await ctx.respond(f"Ping!\nLatency is **{latency} ms**!")
        print(f" * ping использовал пользователь {author}")
        logging.info(f"Command 'ping' using by {author}")
    
    @bot.command(name = 'stop', description='Останавливает бота. Для использования надо иметь права администрирования бота')
    async def stop (ctx):
        author = str(ctx.author.id)
        if author==os.getenv("BRid"):
            print ("MyTanks Discord Bot OFFLINE")
            logging.warning("MyTanks Discord Bot OFFLINE")
            await ctx.respond('MyTanks Discord Bot OFFLINE')
            sys.exit()
        else:
            await ctx.respond('Your not my daddy!')
            print(f" * stop использовал пользователь {author}")
            logging.warning(f"Command 'stop' using by {author}")
        

bot.run(os.getenv('TOKEN'))