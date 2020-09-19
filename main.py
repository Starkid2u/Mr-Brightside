#!/usr/bin/env python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()

async def attachments_to_files(attached,spoiler=False):
    filelist = []
    for i in attached:
        file = await i.to_file()
        filelist.insert(len(filelist),file)
    return filelist

my_id = 525495267537977344
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

ragecooldown = 0
raged_at = 0
enterrage = 0
@client.event
async def on_message(message):
    # linking status
    standowner = discord.utils.get(message.guild.members, id = my_id)
    try:
        if standowner.activity.name == "Spotify":
            await client.change_presence(status=standowner.status, activity=discord.Activity(name=standowner.activity.name, type=discord.ActivityType.listening))
    except AttributeError:
        await client.change_presence(status=standowner.status, activity=standowner.activity)

    async def unvist():
        if not (visitor in message.author.roles or dead_visitor in message.author.roles):
            return
        await message.author.remove_roles(visitor,reason="leaving")
        if dead_visitor in message.author.roles:
            await message.author.remove_roles(dead_visitor,reason="leaving")
            await message.author.add_roles(dead,reason="leaving")
        print('leaving')
        
    if message.channel.category.id == 736788095667666985:
        return
    if message.author == client.user:
        return

    maxhealth = discord.utils.get(message.guild.roles, id = 714534974916919349)
    health9 = discord.utils.get(message.guild.roles, id = 714535185273847871)
    health8 = discord.utils.get(message.guild.roles, id = 714535298729640047)
    health7 = discord.utils.get(message.guild.roles, id = 714535324759621712)
    health6 = discord.utils.get(message.guild.roles, id = 714535348046266449)
    health5 = discord.utils.get(message.guild.roles, id = 714535379675644054)
    health4 = discord.utils.get(message.guild.roles, id = 714535405843775518)
    health3 = discord.utils.get(message.guild.roles, id = 714535436143558788)
    health2 = discord.utils.get(message.guild.roles, id = 714535460860330066)
    health1 = discord.utils.get(message.guild.roles, id = 714535481928319016)
    visitor = discord.utils.get(message.guild.roles, id = 737149499364999179)
    dead = discord.utils.get(message.guild.roles, id = 714535509279637525)
    dead_visitor = discord.utils.get(message.guild.roles, id = 747460046333673573)
    enraged = discord.utils.get(message.guild.roles, id = 749824364618186844)
    enraged_victim = discord.utils.get(message.guild.roles, id = 749824617648226326)

    if message.content.startswith('brightside attack'):
        if message.author.id != my_id:
            return
        await message.channel.send('gararararararara')
        print(f'attacking {message.mentions[0]}')
        if (enraged in message.author.roles and enraged_victim in message.mentions[0].roles):
            await asyncio.sleep(0.5)
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health9,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 9 health")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health8,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 8 health")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 7 health")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 6 health")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 5 health")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 4 health")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 3 health")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 2 health")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
                print(f"{message.author.name} hit {message.mentions[0].name} with a stand and brought them down to 1 health")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
                print(f"{message.author.name} killed {message.mentions[0].name} with a stand")

    if message.content.startswith('?echo'):
        if message.author.id != my_id:
            return
        images = await attachments_to_files(message.attachments,True)
        await message.delete()
        await message.channel.send(message.content[5:],files=images)
        print(f'repeating{message.content[5:]}')

    #otherworldly visitor code 
    if message.content.startswith('brightside visit'):
        if message.author.id != my_id:
            return
        if not dead in message.author.roles:
            await message.author.add_roles(visitor,reason="crossed over to dead realm")
            print('crossing over to dead realm')
            await asyncio.sleep(30)
        else:
            await message.author.add_roles(dead_visitor,reason="crossed over to living realm")
            await message.author.remove_roles(dead,reason="crossed over to living realm")
            print('crossing over to living realm')
            await asyncio.sleep(30)
        await unvist()
    if message.content.startswith('brightside unvisit'):
        if message.author.id != my_id:
            return
        await unvist()

    #blindrage code
    global ragecooldown
    global raged_at
    global enterrage
    if (f"<@!{my_id}>" in message.content):
        if ragecooldown == 1:
            return
        enterrage = 1
        raged_at = message.author
        await asyncio.sleep(120)
        raged_at = 0
        enterrage = 0
    if message.content.startswith("enter rage"):
        if message.author.id != my_id:
            return
        await message.delete()
        if ragecooldown == 1:
            return
        if enterrage == 1:
            enterrage = 0
            await raged_at.add_roles(enraged_victim, reason="enraged")
            await message.author.add_roles(enraged, reason="enraged")
            await asyncio.sleep(30)
            await raged_at.remove_roles(enraged_victim, reason="unenraged")
            await message.author.remove_roles(enraged, reason="unenraged")
            raged_at = 0
            ragecooldown = 1
            await asyncio.sleep(5*60)
            ragecooldown = 0

    
@client.event
async def on_member_update(before, after):
    if after.id == my_id:
        try:
            if after.activity.name == "Spotify":
                await client.change_presence(status=after.status, activity=discord.Activity(name=after.activity.name, type=discord.ActivityType.listening))
        except AttributeError:
            await client.change_presence(status=after.status, activity=after.activity)

            
client.run(token)