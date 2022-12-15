# Libs
import logging
import os
import discord
from colorama import Fore, Style
from dotenv import load_dotenv
from discord.ext import commands

# Logging
logging.basicConfig(level=logging.WARNING, filename="events.log", format="%(asctime)s: %(message)s")

# Import env
load_dotenv()

# var
bot = discord.Bot()
ver = (os.getenv('version') + os.getenv('build') )
event = "USED:      Command "

# Start bot
@bot.event
async def on_ready ():
    print(Fore.GREEN, "\n====================== MyTanks Discord Bot ONLINE ======================\n", Style.RESET_ALL)
    logging.error('\n\n====================== MyTanks Discord Bot ONLINE ======================\n')
    

##### Commands #####
class comands:  
# Help
    @bot.command (name = "help", description = "Information about bot")
    async def help (ctx):
        author = str(ctx.author.id)
        
        #Embed
        help=discord.Embed(             #Embed text
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
        help.add_field(name="Website", value="http://mytanks.net/", inline=True)    #Description
        help.add_field(name="VK", value="https://vk.com/mytanksonline_official", inline=True)   #Description
        help.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png')   #Embed author
        help.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")    #Embed sign
        
        await ctx.respond(embed=help)
        
        # Logging
        print(Fore.YELLOW, f" * help использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'help' by {author}")
        
# Hello        
    @bot.command (name = "hello", description = "Say hello to the bot!")
    async def hello(ctx):
        author = str(ctx.author.id)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        
        # Logging
        print(Fore.YELLOW, f" * hello использовал пользователь {author}")
        logging.warning(f"{event} 'hello' by {author}")

# Ping
    @bot.command(name = "ping", description="Returns the bot delay") 
    async def ping(ctx): 
        author = str(ctx.author.id)
        latency = round(bot.latency*1000)
        latency=str(latency)
        print(Fore.MAGENTA, f'Current latency {latency}', Style.RESET_ALL)
        logging.warning(f"Latency is {latency} ms")
        
        #Embed
        ping=discord.Embed(             #Embed text
            title="Current latency",
            description=
            f"""
            **{latency} ms**
            """, 
            color=0x38f11a
        )
        ping.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png') #Embed author
        ping.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}") #Embed sign
        
        await ctx.respond(embed=ping)
        
        # Logging
        print(Fore.YELLOW, f" * ping использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'ping' by {author}")

# Stop    
    @bot.command(name = "stop", description="Stops the bot. To use it, you must have bot administration rights", hidden=True)
    async def stop (ctx):
        author = str(ctx.author.id)
        if author==os.getenv("admin_id"):
            # Logging
            print (Fore.RED, "\n====================== MyTanks Discord Bot OFFLINE ======================\n", Style.RESET_ALL)
            logging.warning("\n\n====================== MyTanks Discord Bot OFFLINE ======================\n")
            
            #Embed
            stop=discord.Embed(                                                                                                                                                 #Embed text
                title="**MyTanks Discord Bot OFFLINE**", 
                color=0xff0000
            )
            stop.set_author(name = "MyTanks", url="http://mytanks.net", icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png')   #Embed author
            stop.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")                                                            #Embed sign
            await ctx.respond(embed=stop)
            await bot.close()
        else:
            await ctx.respond("Your not my daddy!")
            
            # Logging
            print(Fore.YELLOW, f" * stop использовал пользователь {author}", Style.RESET_ALL)
            logging.error(f"{event} 'stop' by {author}")
        

bot.run(os.getenv('TOKEN'))