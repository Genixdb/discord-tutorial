import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command()
async def topup(ctx):
    embed=nextcord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
    embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
    embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
    await ctx.message.delete()
    await ctx.send(embed=embed)





bot.run("token")