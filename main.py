#!/usr/bin/env python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
global message_counter

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)
	return filelist

my_id = 312292633978339329
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

message_counter = 0
@client.event
async def on_message(message):
    async def unvist():
        if not (visitor in message.author.roles):
            return
        await message.author.remove_roles(visitor,reason="leaving")
        print('leaving')

    if message.channel.category.id == 736788095667666985:
        return
    if message.author.bot:
        return
    global message_counter
    message_counter += 1
    if message_counter == 10:
        await message.channel.send("gara")
        print (f'sending gara to {message.channel.name} in {message.guild.name}')
        message_counter = 0
    if not (message.author.id == my_id):
        return

    if message.author == client.user:
        return

    visitor = discord.utils.get(message.guild.roles, id = 737149499364999179)

    if message.content.startswith('brightside attack'):
        await message.channel.send('gararararararara')
        print(f'attacking {message.mentions[0]}')
    if message.content.startswith('Mr. Brightside'):
        await message.channel.send('gara!')
    if message.content.startswith('brightside retreat'):
        await message.channel.send('gara...')
    if message.content.startswith('?echo'):
        images = await attachments_to_files(message.attachments,True)
        await message.delete()
        await message.channel.send(message.content[5:],files=images)
        message_counter -= 1
        print(f'repeating {message.content[5:]}')
    
    if message.content.startswith('brightside visit'):
        await message.author.add_roles(visitor,reason="crossed over")
        print('crossing over')
        await asyncio.sleep(30)
        await unvist()
    if message.content.startswith('brightside return'):
        await unvist()


client.run('NzEzNDM2NzcyNTI4NDIyOTMz.XsgFxQ.0e3UuCeLKr5IpHH8UN3cpBKp7eM')