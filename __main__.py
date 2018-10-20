import discord
import json
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="!bat ")

@client.event
async def on_message(message):
    with open('members.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_exp(users, message.author, message.channel, 1)

    with open('members.json', 'w') as f:
        json.dump(users, f)

    await client.process_commands(message)


@client.event
async def on_ready():
    print("Batcomputer is now online!")
    await client.change_presence(game=discord.Game(name="Use '!bat bat' for help"))

@client.command()
async def rules():
    await client.say("Please check the #rules!")

@client.command()
async def report():
    await client.say("Please use this form to make an issue report: https://goo.gl/forms/Cn4p2LM0ci8TBhys1")

@client.command()
async def upcoming():
    await client.say("This is a work in progress, an announcement will be made when this feature is available.")

@client.command()
async def bat():
    await client.say("Commands\nrules: tells you where rules are\nreport: give you a link for the report form\nupcoming: Gives you a list of upcoming events (Not Implemented)")



async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1
        users[user.id]['currency'] = 0

async def add_exp(users, user, channel, amount):
    users[user.id]['experience'] += amount

    experience = users[user.id]['experience']
    level_now = users[user.id]['level']
    level_next = int(level_now * 8)

    if experience >= level_next:
        await client.send_message(channel, '{} has leveled up to level: {}'.format(user.mention, str(int(level_now + 1))))
        users[user.id]['level'] += 1



tokenFile = open("token.txt","r")
token = tokenFile.read()
tokenFile.close()

client.run(token)
