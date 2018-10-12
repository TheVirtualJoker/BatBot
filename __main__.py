import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix="!bat ")

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

tokenFile = open("token.txt","r")
token = tokenFile.read()
tokenFile.close()

client.run(token)
