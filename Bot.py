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
bot = discord.Bot(command_prefix=".", activity=activity, status=discord.Status.idle, intents = intents)

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
    help.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}") 

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
        name="--------------------------------------------------",
        value=":flag_ru:"
    )
    faq.add_field(
        name="В игре читер, игра сломалась, забыл пароль и т.д.", 
        value="Напиши в канал <#847887130415595561>. Там тебе помогут", 
        inline=False
    )
    faq.add_field(
        name="--------------------------------------------------",
        value=":flag_gb:"
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
    faq.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")
    
    # Connection closed by server
    connection_closed=discord.Embed(
        title="Connection closed by server!",
        description="""
        :flag_ru:
        1. Откройте Диспетчер задач и посмотрите, не открыт ли у вас второй клиент игры, как на скриншоте ниже. Если открыт - завершите оба процесса и запустите игру
        2. Закройте игру и подождите 5 минут
        3. Если по истечению 5 минут ошибка не пропала, напишите в личные сообщения игрового модератора, или упомяните его в <#847887130415595561> с просьбой кикнуть вас с сервера, написав свой ник
        4. Если кик с сервера также не помог - попросите игрового модератора проверить наличие бана (в том числе по IP)
        
        :flag_gb:
        1. Open the Task Manager and see if you have a second game client open, as in the screenshot below. If it is open, complete both processes and start the game
        2. Close the game and wait for 5 minutes
        3. If the error has not disappeared after 5 minutes, write to the game moderator's direct messages, or mention him in the <#847887130415595561> with a request to kick you from the server by writing your nickname
        4. If the kick from the server also did not help - ask the game moderator to check for a ban (including by IP) 
        """,
        color=0xff0000
    )
    connection_closed.set_author(
        name = "MyTanks", 
        url=f"{os.getenv('site')}", 
        icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png'
    )
    connection_closed.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}") 
    
    # File not found
    error_404=discord.Embed(
        title="Не удаётся найти указанный файл | The specified file cannot be found",
        description="""
        :flag_ru:
        1. Найдите файл "version" по пути `%appdata%\mytanks.client.Standlone\Local Store\cache`
        2. В файле "version" удалите все значения и установите значение `1`
        3. Сохраните изменения и перезапустите клиент игры
        
        :flag_gb:
        1. Find the file "version" on folder `%appdata%\mytanks.client.Standlone\Local Store\cache`
        2. In the file "versoin" delete all values and set value to `1`
        3. Save changes and restart the game client
        """,
        color=0xff0000
    )
    error_404.set_author(
        name = "MyTanks", 
        url=f"{os.getenv('site')}", 
        icon_url='https://cdn.discordapp.com/attachments/942924556555927612/1052299135669243924/MyTanks.png'
    )
    error_404.add_field(
        name="Видеогайд | Videoguide", 
        value="https://youtu.be/h_0eKh1IJm4", 
        inline=False
    )
    error_404.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}")     

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
    stop.set_footer(text = f"ver.:{ver}  |  Powered by MyTanks  |  Last update {os.getenv('upd_date')}") 



##### Buttons #####
class faq_buttons (discord.ui.View):
        def __init__(self, *, timeout=1800):
            super().__init__(timeout=timeout)

        @discord.ui.button(label="Connection closed by server", style=discord.ButtonStyle.primary)
        async def button_connect(self,button:discord.ui.Button,interaction:discord.Interaction,custom_id = "connection_closed"):    
            await interaction.response.send_message(embed=embeds.connection_closed)
            
        @discord.ui.button(label="Не удаётся найти указанный файл | The specified file cannot be found", style=discord.ButtonStyle.primary)
        async def button_404(self,button:discord.ui.Button,interaction:discord.Interaction,custom_id = "404"):   
            await interaction.response.send_message(embed=embeds.error_404)
       
class faq_button(discord.ui.View): 
        def __init__(self, *, timeout=1800):
            super().__init__(timeout=timeout)
            
        @discord.ui.button(label="FAQ",style=discord.ButtonStyle.red,emoji="❔")
        async def button(self,button:discord.ui.Button,interaction:discord.Interaction,custom_id = "faq"):
            buttons=faq_buttons()
            buttons.add_item(discord.ui.Button(label="x32 Client",style=discord.ButtonStyle.link,url="https://cdn.discordapp.com/attachments/847886330301907014/900783835103514654/MyTanks.exe"))
            await interaction.response.send_message(embed=embeds.faq, view=buttons)
       


# Start bot
@bot.event
async def on_ready ():
    print(Fore.GREEN, "\n====================== MyTanks Discord Bot ONLINE ======================\n", Style.RESET_ALL)
    logging.error('\n\n====================== MyTanks Discord Bot ONLINE ======================\n')



##### Commands #####
class comands:

# Help
    @bot.command(name = "help", description = "Информация о боте и помощь | Information about bot and help")
    async def help (ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)

        # Buttons
        faq=faq_button()
        faq.add_item(discord.ui.Button(label="Oficial Website",style=discord.ButtonStyle.link,url=f"{os.getenv('site')}"))
        faq.add_item(discord.ui.Button(label="VK",style=discord.ButtonStyle.link,url="https://vk.com/mytanksonline_official"))
        
        await ctx.respond(embed=embeds.help,view=faq)
        
        # Logging
        print(Fore.YELLOW, f" * help использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'help' by {author}")    
        
# FAQ
    @bot.command(name = "faq", description = "Часто задаваемые вопросы | Frequently asked questions")
    async def faq(ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)
        bfaq=faq_buttons()
        bfaq.add_item(discord.ui.Button(label="x32 Client",style=discord.ButtonStyle.link,url="https://cdn.discordapp.com/attachments/847886330301907014/900783835103514654/MyTanks.exe"))
        await ctx.respond(embed=embeds.faq,view=bfaq)
        
        #Logging
        print(Fore.YELLOW, f" * faq использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'faq' by {author}")       

# Connection closed
    @bot.command(name = "connection", description= 'Ошибка "Connection closed by server!" | Error "Connection closed by server!"')
    async def faq(ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)    
        await ctx.respond(embed=embeds.connection_closed)
        
        #Logging
        print(Fore.YELLOW, f" * Connection использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'connection' by {author}")
        
# File not found     
    @bot.command(name = "file", description= 'Ошибка "Не удаётся найти указанный файл" | Error "The specified file cannot be found"')
    async def faq(ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)    
        await ctx.respond(embed=embeds.error_404)
        
        #Logging
        print(Fore.YELLOW, f" * File использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'file' by {author}")
        
# Hello        
    @bot.command (name = "hello", description = "Скажи привет боту! | Say hello to the bot!")
    async def hello(ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)
        await ctx.respond(f"Hi, {ctx.author.mention}")
        
        # Logging
        print(Fore.YELLOW, f" * hello использовал пользователь {author}")
        logging.warning(f"{event} 'hello' by {author}")

# Ping
    @bot.command(name = "ping", description="Возвращает задержку бота | Returns the bot delay") 
    async def ping(ctx): 
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)
        latency = round(bot.latency*1000)
        latency=str(latency)
        print(Fore.MAGENTA, f'Current latency {latency}', Style.RESET_ALL)
        logging.warning(f"Latency is {latency} ms")
        
        await ctx.respond(f"Current latency is **{latency} ms**")
        
        # Logging
        print(Fore.YELLOW, f" * ping использовал пользователь {author}", Style.RESET_ALL)
        logging.warning(f"{event} 'ping' by {author}")

# Stop    
    @bot.command(name = "stop", description="Останавливает бота | Stops the bot", hidden=True)
    async def stop (ctx):
        author_id = str(ctx.author.id)
        author_name=str(ctx.author.name)
        author=str(author_id + " | " + author_name)
        if author_id==os.getenv("admin_id"):        #check
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
            
#Wiki 


bot.run(os.getenv('TOKEN'))