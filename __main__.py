import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix= "!bat")

@client.event
async def on_ready():
    print("Batcomputer is online!")

tokenFile = open("token.txt","r")
token = tokenFile.read()
tokenFile.close()

client.run(token)
