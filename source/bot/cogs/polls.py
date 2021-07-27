import discord
from bot import bot, numList, emojiDict
from discord.ext import commands
import logging

logger = logging.getLogger('PollCog')

class Polls(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def _createPoll(self, ctx, arg, message: str = ''):
        if arg is None:
            await ctx.send('Command requires poll options. Input each parameter as a comma-separated list(e.g. /poll option one, option-two, third option !?@).')
            return None

        optionsList = arg.split(',') 
        if len(optionsList) > 10:
            await ctx.send('Too many options. Maximum of 10 options')
            return None
        
        if message:
            message += '\n'

        for idx, option in enumerate(optionsList):
            addedOption = f'{emojiDict[numList[idx]]} -> {option}'
            if idx < len(optionsList)-1:
                addedOption += '\n\n'
            message += addedOption

        messageObj = await ctx.send(message)

        for reaction in range(len(optionsList)):
            addedEmoji = emojiDict[numList[reaction]]
            await messageObj.add_reaction(addedEmoji)


    @commands.command()
    async def poll(self, ctx, *, arg=None):
        try:
            await self._createPoll(ctx, arg)
        except Exception as e:
            await ctx.send(str(e))
            logger.error(f'poll command error: {e}')
        else:
            logger.info('poll command complete')

    @commands.command()
    async def polleveryone(self, ctx, *, arg=None):
        try:
            await self._createPoll(ctx, arg, message='@everyone')
        except Exception as e:
            await ctx.send(str(e))
            logger.error(f'poll command error: {e}')
        else:
            logger.info('polleveryone command complete')

    @commands.command()
    async def pollscrim(self, ctx, mention=''):
        try:
            await self._createPoll(ctx, 'Scrimmers, Non-Scrimmers', message=mention)
        except Exception as e:
            await ctx.send(str(e))
        else:
            logger.info('pollscrim command complete')

    @commands.command()
    async def pollgroup(self, ctx, mention, *, arg=None):
        try:
            await self._createPoll(ctx, arg, message=mention)
        except Exception as e:
            await ctx.send(str(e))
        else:
            logger.info('pollgroup command complete')

def setup(bot):
    bot.add_cog(Polls(bot))