#Библиоеки
from ensurepip import version
import discord 
import os
from colorama import Fore, Back, Style
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready ():
    print("\n\n################################\n\n#  MyTanks Discord Bot ONLINE  #\n\n################################\n\n")

help = ("Это пока тестовая версия бота. Команды:\n" # Информация о боте
"`/ping` - Текущая задержка бота\n"
"`/help` - Команда, которую вы использовали для получения информации\n"
"`/hello` - Поздороваться с ботом\n\n"
"Версия: "  + os.getenv('version'))

class comands: # Команды
    @bot.slash_command (name = "hello", description = "Скажи привет боту!")
    async def hello(ctx):
        await ctx.respond(f"Привет, {ctx.author} !")
        print(f" * hello использовал пользователь {ctx.author}")

    @bot.slash_command (name = 'help', descripton = 'Информация о боте')
    async def help(ctx):
        await ctx.respond(help)
        print(f" * version использовал пользователь {ctx.author}")

    @bot.command(name = 'ping', description="Возвращает задержку бота") 
    async def ping(ctx): 
        await ctx.respond(f"Ping!\nLatency is **{round(bot.latency * 1000)} ms**!")
        print(f" * ping использовал пользователь {ctx.author}")

bot.run(os.getenv('TOKEN'))