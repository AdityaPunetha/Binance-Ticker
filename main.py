import requests
import discord
import json
from discord.ext.tasks import loop


def get_price():
    a = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
    json_data = json.loads(a.text)
    price = round(float(json_data['price']), 3)
    return price


def get_change():
    a = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT')
    json_data = json.loads(a.text)
    per = str(
        "{0} ({1}%)".format(round(float(json_data['priceChange']), 3), round(float(json_data['priceChangePercent']), 2)))
    return per


client = discord.Client()
print(get_price())
tk = ''


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    name = "ETH $" + str(get_price())
    global guildinf
    guildinf = message.guild.me
    # print(name)

    # if message.content.startswith('e'):
    set_name.start()
    set_status.start()


@loop(count=None, seconds=1)
async def set_name():
    name = "ETH $" + str(get_price())
    # print(name)
    await guildinf.edit(nick=name)


@loop(count=None, seconds=1)
async def set_status():
    st = get_change()
    print(st)
    await client.change_presence(activity=discord.Game(st))


client.run(tk)
