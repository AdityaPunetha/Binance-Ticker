import requests
import discord
import json


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


# message.channel.send(name)
#message.guild.me.edit(nick=name)

@client.event
async def on_message(message):
    name = get_eth_price()
    # if message.content.startswith('e'):
    await message.guild.me.edit(nick=name)


client.run(tk)
