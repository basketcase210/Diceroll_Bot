import discord
from discord.ext import commands
import random

#Set Intents 
intents = discord.Intents.default()
intents.message_content = True


#Create bot object with prefix of ! for commands. Setting Help command to None
bot = commands.Bot(intents=intents,command_prefix = "!" ,help_command = None)

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
#Start of group of command of roll
@bot.group()
async def roll(ctx):
    pass
#roll d20
@roll.command()
async def d20(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,20)
    await ctx.channel.send(username +' Rolled ' + str(roll)) 
#roll d12
@roll.command()
async def d12(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,12)
    await ctx.channel.send(username +' Rolled ' + str(roll)) 
#roll d10
@roll.command()
async def d10(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,10)
    await ctx.channel.send(username +' Rolled ' + str(roll)) 
#roll d8
@roll.command()
async def d8(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,8)
    await ctx.channel.send(username +' Rolled ' + str(roll)) 
#roll d6
@roll.command()
async def d6(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,6)
    await ctx.channel.send(username +' Rolled ' + str(roll))     
#roll d4
roll.command()
async def d4(ctx):
    username =ctx.author.display_name
    roll = random.randint(1,4)
    await ctx.channel.send(username +' Rolled ' + str(roll))     


#set custom help command. 
@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description = "These are the Commands that you can use to roll",color = discord.Colour.dark_purple())
    MyEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/513Jy8Lk2UL.jpg")
    MyEmbed.add_field(name = "!roll d20", value = "This Command allows you roll a d20", inline = False)
    MyEmbed.add_field(name = "!roll d12", value = "This Command allows you roll a d12", inline = False)
    MyEmbed.add_field(name = "!roll d10", value = "This Command allows you roll a d10", inline = False)
    MyEmbed.add_field(name = "!roll d8", value = "This Command allows you roll a d8", inline = False)
    MyEmbed.add_field(name = "!roll d6", value = "This Command allows you roll a d6", inline = False)
    MyEmbed.add_field(name = "!roll d4", value = "This Command allows you roll a d4", inline = False)
    await ctx.send(embed = MyEmbed)
 
#API Token 
bot.run("")