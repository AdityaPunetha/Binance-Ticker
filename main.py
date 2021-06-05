import requests
import discord
import json
from discord.ext import commands


def get_eth_price():
    a = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
    json_data = json.loads(a.text)
    return json_data['price']


client = discord.Client()
print(get_eth_price())
tk = ''


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


'''
@client.event

async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    if message.content.startswith('$o'):
        await message.channel.send(message.author)
    if message.content.startswith('$n'):
        await message.channel.send(client.user)
    if message.content.startswith('$k'):
        await message.channel.send(client.guilds)
    if message.content.startswith('$g'):
        await client.change_presence(status="get_eth_price()")
'''
bot = commands.Bot(command_prefix="!!")


@bot.command()
async def run(ctx):
    while True:
        change = get_eth_price()
        # name="S&P500: \n$"+ str(round(si.get_live_price("StockSymbol"),2))+ "("+str(round(change["regularMarketChangePercent"],2))+")"+"%"
        await ctx.guild.me.edit(nick=change)


client.run(tk)
