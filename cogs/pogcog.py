""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍
 __________
< POGGERS! >
 ----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Version: 5.5.0
"""

from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


# Here we name the cog and create a new class for the cog.
class Pog(commands.Cog, name="pogcog"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="pog",
        description="The only command you need!",
    )
    # This will only allow non-blacklisted members to execute the command
    # @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    # @checks.is_owner()
    async def pog(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Do your stuff here
        user_id = context.author.id
        # print("user ID: "user_id)
        await context.send(user_id + " says poggers")
        # await context.send("f<@{user_id} says poggers", tts=True)


        # Don't forget to remove "pass", I added this just because there's no content in the method.




# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Pog(bot))
