from twitchio.ext import commands
import os
import logging
import sys


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.environ['TWITCH_IRC_TOKEN'],
            client_id=os.environ['TWITCH_CLIENT_ID'],
            nick='CheeseBoard_Bot',
            prefix='!',
            initial_channels=list(os.environ['TWITCH_CHANNELS'].split(',')))

    async def event_ready(self):
        logger.info(f'Ready | {self.nick}')

    async def event_message(self, message):
        logger.info(' '.join([
            str(message.author.name),
            str(message.author.id),
            str(message.author.tags),
            str(message.content)]))
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.tags["display-name"]}!')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
bot = Bot()
bot.run()
