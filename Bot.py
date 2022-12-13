# Libs
import sys
import logging
import os
import discord
from ensurepip import version
from colorama import Back, Fore, Style
from dotenv import load_dotenv
from discord.ext import commands

# Logging
logging.basicConfig(level=logging.INFO, filename="events.log", format="%(asctime)s | %(levelname)s | %(message)s")

# Imort env
load_dotenv()
bot = discord.Bot()

# Start bot
@bot.event
async def on_ready ():
    print("\nMyTanks Discord Bot ONLINE\n")
    logging.warning('MyTanks Discord Bot ONLINE')

##### Commands #####
class comands:  
# Help
    @bot.command (name = "help", description = "Information about bot")
    async def help (ctx):
        author = str(ctx.author.id)
        
        #Embed
        help=discord.Embed(                                                                                                                                                 #Embed text
            title="Помощь  |  Help",
            description=
            """
            **Команды бота  |  Bot commands**
            `/help` - Помощь  |  Help
            `/ping` - Текущая задержка бота  |  Current bot latency
            `/hello` - Поздороваться с ботом  |  Say hello to the bot
            `/stop` - Остановить бота. Нужно быть разработчиком  |  Stop the bot. You need to be a developer
            
            **Нужна помощь?  | Need help?**
            <#847887130415595561>
            
            **Есть идея?  |  Got an idea?**
            <#847887630024573048>
            
            
            """, 
            color=0x38f11a
        )
        help.add_field(name="Website", value="http://mytanks.net/", inline=True)                                                                                            #Description
        help.add_field(name="VK", value="https://vk.com/mytanksonline_official", inline=True)                                                                               #Description
        help.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png')   #Embed author
        help.set_footer(text = f"ver.:{os.getenv('version')}.{os.getenv('build')}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")                          #Embed sign
        
        await ctx.respond(embed=help)
        print(f" * help использовал пользователь {author}")
        logging.info(f"Command 'help' using by {author}")
        
# Hello        
    @bot.command (name = "hello", description = "Say hello to the bot!")
    async def hello(ctx):
        author = str(ctx.author.id)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        print(f" * hello использовал пользователь {author}")
        logging.info(f"Command 'hello' using by {author}")

# Ping
    @bot.command(name = "ping", description="Returns the bot delay") 
    async def ping(ctx): 
        author = str(ctx.author.id)
        latency = round(bot.latency*1000)
        latency=str(latency)
        logging.info(f"Latency is {latency} ms")
        
        #Embed
        ping=discord.Embed(                                                                                                                                                 #Embed text
            title="Current latency",
            description=
            f"""
            **{latency} ms**
            """, 
            color=0x38f11a
        )
        ping.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png')   #Embed author
        ping.set_footer(text = f"ver.:{os.getenv('version')}.{os.getenv('build')}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")                          #Embed sign
        
        await ctx.respond(embed=ping)
        print(f" * ping использовал пользователь {author}")
        logging.info(f"Command 'ping' using by {author}")

# Stop    
    @bot.command(name = "stop", description="Stops the bot. To use it, you must have bot administration rights", hidden=True)
    async def stop (ctx):
        author = str(ctx.author.id)
        if author==os.getenv("admin_id"):
            print ("MyTanks Discord Bot OFFLINE")
            logging.warning("MyTanks Discord Bot OFFLINE")
            
            #Embed
            stop=discord.Embed(                                                                                                                                             #Embed text
                title="**MyTanks Discord Bot OFFLINE**", 
                color=0xff0000
            )
            stop.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png')   #Embed author
            stop.set_footer(text = f"ver.:{os.getenv('version')}.{os.getenv('build')}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")                          #Embed sign
            await ctx.respond(embed=stop)
            sys.exit()
        else:
            await ctx.respond("Your not my daddy!")
            print(f" * stop использовал пользователь {author}")
            logging.warning(f"Command 'stop' using by {author}")
        

bot.run(os.getenv('TOKEN'))