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
    t = ""
    if float(json_data['priceChangePercent']) >= 0:
        t = "+"
    else:
        t = ""
    per = str(
        "{2}{0} ({2}{1}%)".format(round(float(json_data['priceChange']), 3),
                                  round(float(json_data['priceChangePercent']), 2), t))

    return per, t


client = discord.Client()
print(get_price())
tk = ''
color = "-"


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    set_name.start()


@loop(count=None, seconds=1)
async def set_name():
    name = "ETH $" + str(get_price())
    global color
    change = get_change()
    st = change[0]
    if color != change[1]:
        color = change[1]
        if color == "+":
            for x in client.guilds:
                rrole = x.get_role(846495911135936542)
                grole = x.get_role(846495878130958406)
                try:
                    await x.me.add_roles(grole)
                    await x.me.remove_roles(rrole)
                except:
                    pass
        else:
            for x in client.guilds:
                rrole = x.get_role(846495911135936542)
                grole = x.get_role(846495878130958406)

                try:
                    await x.me.add_roles(rrole)
                    await x.me.remove_roles(grole)

                except:
                    pass

    await client.change_presence(activity=discord.Game(st))
    for i in client.guilds:
        await i.me.edit(nick=name)


client.run(tk)
