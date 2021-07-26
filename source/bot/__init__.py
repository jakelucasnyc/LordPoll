import discord
from discord.ext import commands
import logging
from emoji import emojize, demojize
import os

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()

bot = commands.Bot('poll.', intents=intents)
numList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
emojiDict = {num: emojize(f':{num}:', use_aliases=True) for num in numList} 

@bot.event
async def on_ready():
    logger.info('Bot Ready')

# @bot.event
# async def on_command_error(ctx, error):
#     if error == commands.errors.CommandNotFound:
#         await ctx.send('Invalid Command.')


@bot.command()
async def reload(ctx, extension: str):
    try:
        bot.unload_extension(f'bot.cogs.{extension}')
        bot.load_extension(f'bot.cogs.{extension}')
    except Exception as e:
        await ctx.send(str(e))
    else:
        await ctx.send('Reload Successful.')

for filename in os.listdir('./bot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'bot.cogs.{filename[:-3]}')
    


    


        






