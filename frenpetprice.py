import os
import requests
import json
import nextcord
from nextcord.ext import commands

# Enable all necessary Intents for the bot
intents = nextcord.Intents.all()

# Create a bot instance with specified intents and changed prefix
bot = commands.Bot(command_prefix='?', intents=intents)

# Specific channel ID (replace this with the actual channel ID)
SPECIFIC_CHANNEL_ID = 1175995133259415645

# Function to fetch the token price
def get_your_token_price():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=frenpet&vs_currencies=usd')
        if response.status_code == 200:
            price_info = response.json()
            return price_info['frenpet']['usd']
        else:
            print(f"Error fetching the price. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception in fetching the price: {e}")
        return None

# Command to send the current token price
@bot.command()
async def price(ctx):
    if ctx.channel.id == SPECIFIC_CHANNEL_ID:
        try:
            price = get_your_token_price()
            if price is not None:
                message = f"The current price of $FP is: {price} USD."  # Updated text
            else:
                message = "There was an error fetching the price."
            await ctx.send(message)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            print(f"Error in 'price' command: {e}")
    else:
        await ctx.send("This command can only be used in the specific channel.")

# Event called when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Start the bot with the given token
bot.run("") 
