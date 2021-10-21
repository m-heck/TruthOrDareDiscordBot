import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online)
    print('A wild bot appeared!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

truths = []
dares = []

def reloadTruths():
    truthList = open('truth.txt', 'r')
    for line in truthList:
        truths.append(line)
    truthList.close()

@client.command(aliases = ['t', 'T', 'Truth'])
async def truth(ctx):
    if len(truths) == 0:
        reloadTruths()
    truth = random.choice(truths)
    truths.remove(truth)
    await ctx.send(truth)

def reloadDares():
    dareList = open('dare.txt', 'r')
    for line in dareList:
        dares.append(line)
    dareList.close()

@client.command(aliases = ['d', 'D', 'Dare'])
async def dare(ctx):
    if len(dares) == 0:
        reloadDares()
    dare = random.choice(dares)
    dares.remove(dare)
    await ctx.send(dare)

@client.command(aliases = ['rt', 'ResetTruths', 'resettruths', 'RT'])
async def resetTruths(ctx):
    reloadTruths()
    await ctx.send('Truths have been reset.')

@client.command(aliases = ['rd', 'ResetDares', 'resetdares', 'RD'])
async def resetDares(ctx):
    reloadDares()
    await ctx.send('Dares have been reset.')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

client.run(os.environ['token'])

#miyakos-truth-or-dare