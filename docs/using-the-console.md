# Using the console

## Starting the server with a console so you can reload cogs

```
$ python -i bot.py
2023-03-31 19:45:03 INFO     discord_bot Loaded extension 'foo'
2023-03-31 19:45:03 INFO     discord_bot Loaded extension 'bar'
...
>>> asyncio.run(bot.reload_extension("cogs.foo"))
```

## Using the console to interact with the database

```
$ python
Python 3.10
Type "help", "copyright", "credits" or "license" for more information.
>>> import bot
2023-03-31 18:20:45 INFO     discord_bot Loaded extension 'template'
2023-03-31 18:20:45 INFO     discord_bot Loaded extension 'fun'
2023-03-31 18:20:45 INFO     discord_bot Loaded extension 'owner'
2023-03-31 18:20:45 INFO     discord_bot Loaded extension 'general'
>>> bot
<module 'bot' from '/home/jack/code/challenge-bot/bot.py'>
>>> bot.bot
<discord.ext.commands.bot.Bot object at 0x7faf43408c40>
>>>
>>> import asyncio
>>> import helpers.db_manager as db_manager
>>> asyncio.run(db_manager.get_activities_for_user(42))
[('42', 'walk', '1680304538'), ('42', 'run', '1680304553'), ('42', 'yoga', '1680304555')]
```