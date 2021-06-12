import discord
from discord.ext import commands
import requests
import json
import asyncio
import random

client = commands.Bot(command_prefix='*', case_insensitive=True)
client.remove_command('help')

message__id = 0
channel_id = 0
member_id = 0
member = ''

@client.event
async def on_ready():
    print('Bot Is Ready')
    await client.change_presence(activity=discord.Game(name='Made by warsnoop#0755'))

@client.command()
async def setup(ctx):
    global member
    global message__id
    global channel_id
    channel_id = (ctx.channel.id)
    member = ctx.message.author
    embed = discord.Embed(title="Ables Cod Services", color=0x03fc14)
    embed.add_field(name=f"Verification!", value=('React to this message to get verified!'), inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    mesg = await ctx.send(embed=embed)
    await mesg.add_reaction("✔️")
    message__id = mesg.id
    


@client.event
async def on_reaction_add(reaction, user):
    global message__id
    global channel_id
    if str(reaction.emoji) == "✔️":
        channel = client.get_channel(channel_id)
        try:
            role = discord.utils.get(member.guild.roles, name="verified")
            await user.add_roles(role)
        except:
            print('error')
            await channel.send('Unknown error occured, Try again later!')

@commands.has_permissions(administrator=True)
@client.command()
async def verify(ctx, user: discord.User):
    role = discord.utils.get(ctx.message.guild.roles, name="verified")
    await user.add_roles(role)
    embed = discord.Embed(title="Verification System!", color=0x03fc14)
    embed.add_field(name=f"Success!", value=('SuccessFully Verified user!'), inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Verification System!", color=0xff0000)
    embed.add_field(name=f"*Setup", value=('Sets The channel for verification!'), inline=False)
    embed.add_field(name=f"*verify (tag user)", value=('Verifies the user!'), inline=False)
    embed.add_field(name=f"*help", value=('This command!'), inline=False)
    embed.set_footer(text='Resellers for bulk prices spend 250+', icon_url=ctx.author.avatar_url)
    mesg = await ctx.send(embed=embed)


client.run('Token Here')