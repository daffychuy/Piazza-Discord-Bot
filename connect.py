import os, discord, piazza
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['GUILD']
EMAIL = os.environ['EMAIL']
PASSWD = os.environ['PASSWD']
CUR_CLASS = os.environ['CUR_CLASS']
REG_PATTERN = "((?:https|http):\/\/(?:www\.)*piazza\.com\/class\/(.*?)\?cid=(\d+))"
client = discord.Client()

@client.event
async def on_message(message):
    '''
    For every new message on the server, on_message() is called
    with the messaged passed in.
    '''

    # Ignore the bots own messages to the server
    if message.author == client.user:
        return

    # If message is a piazza link, call piazza.piazza_parse()
    # Then send piazza post to server
    urls = re.findall(REG_PATTERN, message.content)
    if urls:
        for url in urls:
            full_url = url[0]
            class_hash = url[1]
            _ = url[2] # post id
            if class_hash == '*' or class_hash == CUR_CLASS:
                response = piazza.piazza_parse(full_url, EMAIL, PASSWD, message.author)
                await message.channel.send(embed=response)
    
    # ? Todo: Implment with @number
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_ready():
    '''
        Prints to console when bot is connected to Discord and server.
    '''
    print(f'{client.user} has connected to Discord!\n')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to the following guild: {guild.name}(id: {guild.id})')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Piazza's Code"))
client.run(TOKEN)