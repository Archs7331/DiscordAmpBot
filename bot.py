#shitty discord amp scanner bot by archs | @ttl.hax on insta | https://github.com/TTL-ovpn/DiscordAmpBot
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio
import aiohttp
import os
import subprocess

prefix = "." #bot prefix
client = commands.Bot(command_prefix = prefix)
token = "bot token skeed" #replace wit yo bot token skeed
client.remove_command('help')
@client.event
async def on_ready():
	print("Bot running")

#help command
@client.command()
@commands.has_role("scanning")
async def help(ctx):
	await ctx.message.delete()
	helpembed = discord.Embed(title="**AmpBot**", description="All Commands", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	helpembed.add_field(name=".scan <scannername> <ip start range> <ip end range> <outputfile> <threads> <scandelay>", value="Uses bot server to scan for amps with desired amp")
	helpembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	helpembed.add_field(name=".list <outputfile>", value="Sends ur fresh amp list")
	helpembed.add_field(name="Bot Made By", value="Archs#1337")
	await ctx.send(embed=helpembed)

#sending list command
@client.command()
@commands.has_role("scanning")
async def list(ctx, outputfile):
	listamp = discord.Embed(title="**AmpBot**", description="Sending Amp List", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	listamp.add_field(name="Sending ur amp list....", value="Gathering list")
	listamp.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	listamp.add_field(name="Bot Made By", value="Archs#1337")
	await ctx.send(embed=listamp)
	time.sleep(5)
	await ctx.send(file=discord.File(f"/root/{outputfile}"))
	
#scanning command
@client.command()
@commands.has_role("scanning")
async def scan(ctx, scannername, ipstart, ipend, outputfile, threads, scandelay):
	scanning = discord.Embed(title="**AmpBot**", description="Starting Amp Scanner! , Running a new command will make the bot go offline , it will come back online automaticly after scanning is finished!", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	scanning.add_field(name="Starting Amp Scanner Bot", value=f"Scanning {scannername} with {threads} threads")
	scanning.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	scanning.add_field(name="Bot Made By", value="Archs#1337")
	await ctx.send(embed=scanning)
	os.system(f"./{scannername} {ipstart} {ipend} {outputfile} {threads} {scandelay}")

client.run(token)
