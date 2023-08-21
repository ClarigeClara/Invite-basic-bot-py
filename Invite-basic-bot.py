import discord
import asyncio
from discord.commands import Option, OptionChoice
from discord.ext import tasks, commands

# alle intents sind aktiviert
intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready() -> None:
    print("Ich gehe nun Online als:")
    print(f"{bot.user.name} - {bot.user.id}")
    status_task.start()


@tasks.loop()  # STATUS
async def status_task() -> None:
    await bot.change_presence(activity=discord.Game("Game1"),
                              status=discord.Status.online)
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game("Game2"),
                              status=discord.Status.online)
    await asyncio.sleep(10)

# Gehe auf dem Discord-Server und tippe "/invite" ein!
@bot.slash_command(name="invite", description="Erstelle dir einen Invite")
@commands.has_permissions(ban_members=True)
async def invite(ctx):
    link = await ctx.channel.create_invite(reason=None, max_age=0, max_uses=0, temporary=False, unique=True)
    await ctx.respond(f"Ich habe dir einen Infinity-Invite erstellt\n{link}")

# BITTE ERSTELLE DIR EINEN DISCORD BOT-TOKEN.
bot.run("TOKEN")
