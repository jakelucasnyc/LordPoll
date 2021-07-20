import discord
from discord.ext import commands
import logging
from emoji import emojize, demojize

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

intents = discord.Intents.default()

bot = commands.Bot('/', intents=intents)
numList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
emojiDict = {num: emojize(f':{num}:', use_aliases=True) for num in numList} 

@bot.event
async def on_ready():
    logger.info('Bot Ready')

@bot.command()
async def poll(ctx, *, arg=None):
    logger.info('Poll Command Ran')
    if arg is None:
        await ctx.send('Command requires poll options. Input each parameter as a comma-separated list(e.g. /poll option one, option-two, third option !?@).')
        return

    optionsList = arg.split(',') 
    if len(optionsList) > 10:
        await ctx.send('Too many options. Maximum of 10 options')
        return

    message = ''
    for idx, option in enumerate(optionsList):
        addedOption = f'{emojiDict[numList[idx]]} -> {option}'
        if idx < len(optionsList)-1:
            addedOption += '\n\n'
        message += addedOption

    messageObj = await ctx.send(message)
    messageId = messageObj.id
    for reaction in range(len(optionsList)):
        addedEmoji = emojiDict[numList[reaction]]
        await messageObj.add_reaction(addedEmoji)

    


        






