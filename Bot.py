# Libs
import logging
import os
import discord
from colorama import Fore, Style
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import view



# Logging
logging.basicConfig(level=logging.WARNING, filename="events.log", format="%(asctime)s: %(message)s")



# Import env
load_dotenv()



##### VAR #####
intents = discord.Intents.all()
activity = discord.Game(name=f"/help | mytanks.net")
bot = discord.Bot(command_prefix="/", activity=activity, status=discord.Status.idle, intents = intents)

ver = (os.getenv('version') +"."+ os.getenv('build') )
event = "USED:      Command "



##### Embeds #####
class embeds:
    
    # Help
    help=discord.Embed(
        title="Помощь  |  Help",
        description=
        """
        **Команды бота  |  Bot commands**
        `/help` - Помощь  |  Help
        `/faq` - Ответы на частые вопросы по игре | Answers to frequently asked questions about the game
        `/ping` - Текущая задержка бота  |  Current bot latency
        `/hello` - Поздороваться с ботом  |  Say hello to the bot
        `/stop` - Остановить бота. Нужно быть разработчиком  |  Stop the bot. You need to be a developer
                
        **Нужна помощь в игре?  | Need help in the game?**
        <#847887130415595561>
                
        **Есть идея?  |  Got an idea?**
        <#847887630024573048>
        """, 
        color=0x38f11a
    )
    help.set_author(
        name = "MyTanks", 
        url=f"{os.getenv('site')}", 
        icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png'
    )
    help.set_footer(
        text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}"
    ) 

    # FAQ
    faq=discord.Embed(
        title="FAQ", 
        description="""
        **Здесь представлены ответы на частые вопросы**
        **Here are answers to frequently asked questions**
        """,
        color=0x38f11a
    )
    faq.add_field(
        name="В игре читер, игра сломалась, забыл пароль и т.д.", 
        value="Напиши в канал <#847887130415595561>. Там тебе помогут", 
        inline=False
    )
    faq.add_field(
        name="--------------------------------------------------",
        value="                         EN"
    )
    faq.add_field(
        name="The game is a cheater, the game broke, forgot the password, etc.", 
        value="Write to the channel <#847887130415595561>. They'll help you there", 
        inline=False
    )
    faq.set_author(
        name = "MyTanks", 
        url=f"{os.getenv('site')}", 
        icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png'
    )
    faq.set_footer(
        text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}"
    )
    
    # Stop
    stop=discord.Embed(
        title="**MyTanks Discord Bot OFFLINE**", 
        color=0xff0000
    )
    stop.set_author(
        name = "MyTanks", 
        url=f"{os.getenv('site')}", 
        icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png'
    )
    stop.set_footer(
        text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}"
    ) 

# Start bot
@bot.event
async def on_ready ():
    print(Fore.GREEN, "\n====================== MyTanks Discord Bot ONLINE ======================\n", Style.RESET_ALL)
    logging.error('\n\n====================== MyTanks Discord Bot ONLINE ======================\n')



##### Buttons ##### 
class faq_button(discord.ui.View): 
        def __init__(self, *, timeout=1800):
            super().__init__(timeout=timeout)
        @discord.ui.button(label="FAQ",style=discord.ButtonStyle.red,emoji="❔")
        async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction,custom_id = "faq"):
            await interaction.response.send_message(content='/faq')

class button(discord.ui.View): 
        def __init__(self, *, timeout=1800):
            super().__init__(timeout=timeout)    



##### Commands #####
class comands:

# Help
    @bot.command (name = "help", description = "Информация о боте и помощь | Information about bot and help")
    async def help (ctx):
        author = str(ctx.author.id)

        # Buttons
        view=faq_button()
        view.add_item(discord.ui.Button(label="Oficial Website",style=discord.ButtonStyle.link,url=f"{os.getenv('site')}"))
        view.add_item(discord.ui.Button(label="VK",style=discord.ButtonStyle.link,url="https://vk.com/mytanksonline_official"))
        
        await ctx.respond(embed=embeds.help,view=view)
        
        # Logging
        print(Fore.YELLOW, f" * help использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'help' by {author}")    
        
# FAQ
    @bot.command(name = "faq", description = "Часто задаваемые вопросы | Frequently asked questions")
    async def faq(ctx):
        author = str(ctx.author.id)
        bfaq=button()
        bfaq.add_item(discord.ui.Button(label="x32 Client",style=discord.ButtonStyle.link,url="https://cdn.discordapp.com/attachments/847886330301907014/900783835103514654/MyTanks.exe"))
        await ctx.respond(embed=embeds.faq,view=bfaq)      
        
# Hello        
    @bot.command (name = "hello", description = "Скажи привет боту! | Say hello to the bot!")
    async def hello(ctx):
        author = str(ctx.author.id)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        
        # Logging
        print(Fore.YELLOW, f" * hello использовал пользователь {author}")
        logging.warning(f"{event} 'hello' by {author}")

# Ping
    @bot.command(name = "ping", description="Возвращает задержку бота | Returns the bot delay") 
    async def ping(ctx): 
        author = str(ctx.author.id)
        latency = round(bot.latency*1000)
        latency=str(latency)
        print(Fore.MAGENTA, f'Current latency {latency}', Style.RESET_ALL)
        logging.warning(f"Latency is {latency} ms")
        
        await ctx.respond(f"Current latency is **{latency} ms**")
        
        # Logging
        print(Fore.YELLOW, f" * ping использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'ping' by {author}")

# Stop    
    @bot.command(name = "stop", description="Останавливает бота | Stops the bot")
    async def stop (ctx):
        author = str(ctx.author.id)
        if author==os.getenv("admin_id"):
            # Logging
            print (Fore.RED, "\n====================== MyTanks Discord Bot OFFLINE ======================\n", Style.RESET_ALL)
            logging.warning("\n\n====================== MyTanks Discord Bot OFFLINE ======================\n")
            
            await ctx.respond(embed=embeds.stop)
            await bot.close()
        else:
            await ctx.respond("You\'re not my daddy!")
            
            # Logging
            print(Fore.YELLOW, f" * stop использовал пользователь {author}", Style.RESET_ALL)
            logging.error(f"{event} 'stop' by {author}")


bot.run(os.getenv('TOKEN'))