# [+] discontinued [+]
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio
import aiohttp
import os
import subprocess
import json
import time


with open("settings.json") as f:
    config = json.load(f)


prefix = config.get('prefix')
client = commands.Bot(command_prefix = prefix)
token = config.get('token')
client.remove_command('help')


@client.event
async def on_ready():
 print(f'''
 ============================
 Discord Amp fixes
 prefix: {prefix}
 Token: {token}
 ============================
 		''')
	
@client.event
async def on_command_error(ctx,error):
     if isinstance(error,commands.MissingPermissions):
          await ctx.send("[!] U aint got no perms scid")
          print(f"[38;2;233;48;8m[[38;2;233;48;8mE[38;2;233;48;8mR[38;2;233;47;8mR[38;2;233;47;8mO[38;2;233;46;8mR[38;2;233;46;8m] [38;2;233;45;8m| [38;2;234;44;8mU[38;2;234;43;8mS[38;2;234;43;8mE[38;2;234;42;8mR[38;2;234;42;8mN[38;2;234;41;8mA[38;2;234;41;8mM[38;2;234;40;8mE[0m:{ctx.author} [38;2;236;33;8m|[0m [38;2;236;32;8mU[38;2;237;32;8mS[38;2;237;31;8mE[38;2;237;31;8mR [38;2;237;30;8mI[38;2;237;29;8mD[0m:{ctx.author.id} [38;2;239;21;8m|[0m [38;2;239;20;8mE[38;2;240;19;8mr[38;2;240;19;8mr[38;2;240;18;8mo[38;2;240;18;8mr [38;2;240;17;8mT[38;2;240;17;8my[38;2;240;16;8mp[38;2;241;16;8me[38;2;241;15;8m: [38;2;241;14;8mN[38;2;241;14;8mo [38;2;241;13;8mP[38;2;241;12;8me[38;2;241;12;8mr[38;2;242;11;8mm[38;2;242;11;8mi[38;2;242;10;8ms[38;2;242;10;8ms[38;2;242;9;8mi[38;2;242;9;8mo[38;2;242;8;8mn[38;2;242;8;8ms[0m")
     elif isinstance(error,commands.CommandNotFound):
          await ctx.send("[?] 404 Comannd Not Found")
          print(f"[38;2;233;48;8m[[38;2;233;48;8mE[38;2;233;48;8mR[38;2;233;47;8mR[38;2;233;47;8mO[38;2;233;46;8mR[38;2;233;46;8m] [38;2;233;45;8m| [38;2;234;44;8mU[38;2;234;44;8mS[38;2;234;43;8mE[38;2;234;43;8mR[38;2;234;43;8mN[38;2;234;42;8mA[38;2;234;42;8mM[38;2;234;41;8mE[0m:{ctx.author} [38;2;236;35;8m|[0m [38;2;236;34;8mU[38;2;236;34;8mS[38;2;236;33;8mE[38;2;236;33;8mR [38;2;237;32;8mI[38;2;237;31;8mD[0m:{ctx.author.id} [38;2;238;25;8m|[0m {ctx.message.content} [38;2;241;15;8mC[38;2;241;14;8mo[38;2;241;14;8mm[38;2;241;13;8mm[38;2;241;13;8ma[38;2;241;13;8mn[38;2;241;12;8md [38;2;242;11;8mN[38;2;242;11;8mo[38;2;242;10;8mt [38;2;242;10;8mF[38;2;242;9;8mo[38;2;242;9;8mu[38;2;242;8;8mn[38;2;242;8;8md[0m")
     elif isinstance(error, commands.MissingRequiredArgument):
          await ctx.send(f"[!] Missing argument pussio: <{error.param}>")
          print(f"[38;2;233;48;8m[[38;2;233;48;8mE[38;2;233;48;8mR[38;2;233;47;8mR[38;2;233;47;8mO[38;2;233;47;8mR[38;2;233;46;8m] [38;2;233;46;8m| [38;2;233;45;8mU[38;2;234;44;8mS[38;2;234;44;8mE[38;2;234;44;8mR[38;2;234;43;8mN[38;2;234;43;8mA[38;2;234;43;8mM[38;2;234;42;8mE[0m:{ctx.author} [38;2;235;37;8m| [38;2;236;36;8mU[38;2;236;35;8mS[38;2;236;35;8mE[38;2;236;35;8mR [38;2;236;34;8mI[38;2;236;34;8mD[0m:{ctx.author.id} [38;2;238;27;8m|[0m {ctx.message.content} [38;2;240;18;8mM[38;2;240;18;8mi[38;2;240;17;8ms[38;2;240;17;8ms[38;2;240;16;8mi[38;2;240;16;8mn[38;2;241;16;8mg [38;2;241;15;8mA[38;2;241;15;8mr[38;2;241;14;8mg[38;2;241;14;8ms[0m [38;2;241;13;8m<[0m{error.param}[38;2;242;8;8m>[0m")

#help command
@client.command()
@commands.has_role("scanning")
async def help(ctx):
	await ctx.message.delete()
	helpembed = discord.Embed(title="**AmpBot**", description="All Commands", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	helpembed.add_field(name=".scan <scannername> <ip start range> <ip end range> <outputfile> <threads> <scandelay>", value="Uses bot server to scan for amps with desired amp", inline=True)
	helpembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	helpembed.add_field(name=".list <outputfile>", value="Sends ur fresh amp list")
	helpembed.add_field(name=".amps", value="Shows all amp scanning options")
	helpembed.add_field(name="Bot Made By", value="Archs#1337 & xplode#1337")
	await ctx.send(embed=helpembed)

#List of amps and shi
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
	listamp.add_field(name="Bot Made By", value="Archs#1337 & xplode#1337")
	await ctx.send(embed=listamp)
	time.sleep(5)
	await ctx.send(file=discord.File(f"/root/{outputfile}"))
	
#scanning command
@client.command()
@commands.has_role("scanning")
async def scan(ctx, scannername, ipstart, ipend, outputfile, threads, scandelay,):
	scanning = discord.Embed(title="**AmpBot**", description="Starting Amp Scanner!", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
	scanning.add_field(name="Starting Amp Scanner Bot", value=f"Scanning Using {scannername} with {threads} threads")
	scanning.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
	scanning.add_field(name="Bot Made By", value="Archs#1337 & xplode#1337")
	await ctx.send(embed=scanning)
	subprocess.getoutput(f"screen -dmS {scannername} ./{scannername} {ipstart} {ipend} {outputfile} {threads} {scandelay}")

#listinfo command h
@client.command()
@commands.has_role("scanning")
async def info(ctx, filename):
 filename=f"{filename}"
 linescount=0
 with open (filename,'r') as files:
    for i in files:
      linescount=linescount+1
 info = discord.Embed(title="**AmpBot**", description="List Info", thumbnail="https://cdn.discordapp.com/attachments/865298305554317342/887536964578992128/unknown.png",color=0xff0000, inline=False)
 info.add_field(name="IPS:", value=linescount, inline=True)
 info.add_field(name="File Name:", value=filename, inline=True)
 info.set_thumbnail(url="https://cdn.discordapp.com/attachments/865298305554317342/887566686675410954/scanboticon.png")
 info.add_field(name="Bot Made By", value="Archs#1337 & xplode#1337")
 await ctx.send(embed=info)

client.run(token)
