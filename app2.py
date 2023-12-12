import discord
from discord.ext import commands
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join_voice(ctx):
    guild_id = '1170003093056929798'  # Replace with your guild (server) ID
    channel_name = 'The Safe Space'  # Replace with the voice channel name

    guild = discord.utils.get(bot.guilds, id=guild_id)

    if guild:
        voice_channel = discord.utils.get(guild.voice_channels, name=channel_name)

        if voice_channel:
            await voice_channel.connect()
            return 'Joined voice channel successfully.'

    return 'Error: Voice channel not found.'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join-voice', methods=['POST'])
def join_voice_route():
    bot.loop.create_task(bot.get_command('join_voice')(None))
    return jsonify({'message': 'Connecting to the voice channel...'})

if __name__ == '__main__':
    bot.run('MTE2OTk5NzUxOTA3MDE4MzU1Ng.GsHAVi.wUc7LzkJPnbCW4qzM6vGwoLf8O4q6ASpVF2DAs')
