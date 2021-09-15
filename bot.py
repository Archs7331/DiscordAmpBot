#shitty discord amp scanner bot by archs | @ttl.hax on insta | https://github.com/TTL-ovpn/DiscordAmpBot | if u need support > Archs#1337
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
token = "ur bot token" #replace wit yo bot token skeed
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
	helpembed.add_field(name=".amps", value="Shows all amp scanning options")
	helpembed.add_field(name="Bot Made By", value="Archs#1337")
	await ctx.send(embed=helpembed)
	
#showing amps command
@client.command()
@commands.has_role("scanning")
async def amps(ctx):
	await ctx.message.delete()
	ampnaming = discord.Embed(title="**AmpBot**", description="All Amps", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	ampnaming.add_field(name="MDNSSCANNER", value="```Multicast DNS```", inline=True)
	ampnaming.add_field(name="WSDSCANNER", value="```Web Server for Device```", inline=True)
	ampnaming.add_field(name="DNSSCANNER", value="```Domain Name System```", inline=True)
	ampnaming.add_field(name="LDAPSCANNER", value="```Lightweight Directory Access Protocol```", inline=True)
	ampnaming.add_field(name="STUNSCANNER", value="```Session Traversal Utilities for NAT```", inline=True)
	ampnaming.add_field(name="SNMPSCANNER", value="```Simple Network Management Protocol```", inline=True)
	ampnaming.add_field(name="NETBIOSSCANNER", value="```NetBios```", inline=True)
	ampnaming.add_field(name="NTPSCANNER", value="```Network Time Protocol```", inline=True)
	ampnaming.add_field(name="CHARGENSCANNER", value="```Character Generator Protocol```", inline=True)
	ampnaming.add_field(name="RIPSCANNER", value="```Routing Information Protocol```", inline=True)
	ampnaming.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	await ctx.send(embed=ampnaming)

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
	scanning.add_field(name="Starting Amp Scanner Bot", value=f"Scanning Using {scannername} with {threads} threads")
	scanning.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	scanning.add_field(name="Bot Made By", value="Archs#1337")
	await ctx.send(embed=scanning)
	os.system(f"./{scannername} {ipstart} {ipend} {outputfile} {threads} {scandelay}")

client.run(token)
