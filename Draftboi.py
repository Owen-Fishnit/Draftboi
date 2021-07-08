## Draftboi - Rewrite 3
## Owen M. (Fishnit)

## clean stuff up idk
##CORVUS, KOGA, TIBERIUS

import discord
import asyncio
import sys
from PIL import Image
import random

client = discord.Client()

# good to go
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='!help'))
    print('Ready to go!')
    print('------')
    global CHAMPIONS
    CHAMPIONS = ["ash", "atlas", "barik", "fernando", "inara", "khan", "makoa", "raum", "ruckus", "terminus", "torvald", "corvus", "furia", "grohk", "grover", "io", "jenos", "mal damba", "pip", "seris", "ying", "bomb king", "cassie", "drogoz", "dredge", "imani", "kinessa", "lian", "sha lin", "strix", "tiberius", "tyra", "viktor", "vivian", "willo", "androxus", "buck", "evie", "koga", "lex", "maeve", "moji", "skye", "talus", "zhin"]
    global MAPS
    MAPS = ['Ascension Peak', 'Bazaar', 'Frog Isle', 'Jaguar Falls', 'Serpent Beach', 'Fish Market', 'Timber Mill', 'Frozen Guard', 'Ice Mines', 'Stone Keep', 'Brightmarsh', 'Splitstone Quarry', 'Shattered Desert']
    global DRAFTING_CHANNEL_IDS
    DRAFTING_CHANNEL_IDS = {}

# ['10','20','10','20','11','21','22','12','13','23','24','14','15','25']

@client.event       
async def on_message(message):
    def shorthand(name):
        name = name.lower()
        if name in ['rik', 'rick']:
            return 'barik'
        elif name == 'nara':
            return 'inara'
        elif name in ['shalin', 'sha']:
            return 'sha lin'
        elif name in ['bombking', 'bk']:
            return 'bomb king'
        elif name in ['tony', 'tiger']:
            return 'tiberius'
        elif name == 'vik':
            return 'viktor'
        elif name == 'corv':
            return 'corvus'
        elif name in ["damba", "snek", "mal'damba"]:
            return 'mal damba'
        elif name == 'tree':
            return 'grover'
        elif name in ['andro', 'andy']:
            return 'androxus'
        elif name in ['kin', 'nessa']:
            return 'kinessa'
        elif name == 'drog':
            return 'drogoz'
        elif name == 'torv':
            return 'torvald'
        elif name == 'nando':
            return 'fernando'
        elif name == 'koa':
            return 'makoa'
        elif name == 'term':
            return 'terminus'
        elif name == 'viv':
            return 'vivian'
        elif name in ['willow', 'moth']:
            return 'willo'
        elif name == 'ruck':
            return 'ruckus'
        else:
            return name

    async def photos(msg, done):
    ## big try except for PermissionError
        try:
            channel_id = msg.channel.id
            draft = DRAFTING_CHANNEL_IDS[channel_id]
            for champ in draft:
                champ += '.png'
            new_im = Image.new('RGB', (125, 75))
            try:
                new_im.paste(Image.open(draft[0] + '.png'), (0, 0))
                new_im.paste(Image.open(draft[1] + '.png'), (75, 0))
                new_im.paste(Image.open(draft[2] + '.png'), (25, 0))
                new_im.paste(Image.open(draft[3] + '.png'), (100, 0))
                new_im.paste(Image.open(draft[4] + '.png'), (0, 25))
                new_im.paste(Image.open(draft[5] + '.png'), (0, 50))
                new_im.paste(Image.open(draft[6] + '.png'), (25, 50))
                new_im.paste(Image.open(draft[7] + '.png'), (25, 25))
                new_im.paste(Image.open(draft[8] + '.png'), (50, 25))
                new_im.paste(Image.open(draft[9] + '.png'), (50, 50))
                new_im.paste(Image.open(draft[10] + '.png'), (75, 50))
                new_im.paste(Image.open(draft[11] + '.png'), (75, 25))
                new_im.paste(Image.open(draft[12] + '.png'), (100, 25))
                new_im.paste(Image.open(draft[13] + '.png'), (100, 50))
            except FileNotFoundError:
                pass
            if done:
                new_im.save('lineup_done.png')
                await msg.channel.send(file=discord.File('lineup_done.png'))
            else:
                new_im.save('lineup.png')
                await msg.channel.send(file=discord.File('lineup.png'))
        except PermissionError:
            print('PERMISSION ERROR IN DEF PHOTOS')
            result = ''
            L = ['10','20','10','20','11','21','22','12','13','23','24','14','15','25']
            for x in range(0, len(DRAFTING_CHANNEL_IDS[message.channel.id])):
                # sometimes this will send team m enter pick a for makoa if entering two picks super quickly but it's not a big deal
                result = result +('Team ' + L[x][0] + ' pick ' + L[x][1] + ' ' + DRAFTING_CHANNEL_IDS[message.channel.id][x] + '\n')
            await msg.channel.send("ErrorCode: PermissionError. The bot can't send photos right now. Sending raw data instead.\n" + result)
        

    def to_purge(msg):  # purge check
        try:
            if msg.attachments[0].filename in ['lineup.png', 'roster.png', 'roster_grey.png']:
                return True
        except IndexError:  # no attachment
            pass
        if shorthand(msg.content) in CHAMPIONS:  # draft pick
            return True
        elif msg.content[:4] in ['!dra', '!ros', '!qui', 'Team', 'Cham', 'Draf', 'No d']:  # bot/command
            return True
        return False
        
    # don't reply to bot
    if message.author.bot:
        return

    message.content = message.content.lower()
    if message.content.startswith('!help'):  # help
        await message.channel.send("!draft   - starts a draft (do !draft mapname for a specific map)\n!roster - displays the game's roster, with picked or banned champions in grey\n!quit     - exits a draft")

    if message.content.startswith('!draft'):  # draft start
        if message.channel.id in DRAFTING_CHANNEL_IDS:
            await message.channel.send('Draft already started in this channel.')
            return
        DRAFTING_CHANNEL_IDS[message.channel.id] = ['10','20','10','20','11','21','22','12','13','23','24','14','15','25']
        if message.content in ['!draft', '!draft ']:
            await message.channel.send('```Draft started - Map: ' + MAPS[random.randint(0, len(MAPS)-1)] + '```')
        else:
            await message.channel.send('```Draft started - Map: ' + message.content[7:] + '```')
        await message.channel.send('Team 1 enter pick 0 (bans are currently described as pick 0).')

    if message.content.startswith('!roster'):  # roster
        if message.channel.id not in DRAFTING_CHANNEL_IDS:  # no draft, just send normal roster
            await message.channel.send(file=discord.File('roster.png'))
        else:  # in draft, send grey roster
            picks = DRAFTING_CHANNEL_IDS[message.channel.id]
            new_im = Image.new('RGB', (325, 100))  # change this if lines are too short
            x, y  = 0, 0
            for champ in CHAMPIONS:
                if champ in picks:
                    new_im.paste(Image.open(champ + '_grey.png'), (x, y))
                else:
                    new_im.paste(Image.open(champ + '.png'), (x, y))
                x += 25
                if champ in ['torvald', 'ying', 'willo']:  # change this if a charcter with a lower letter comes out
                    x = 0
                    y += 25
            new_im.save('roster_grey.png')
            await message.channel.send(file=discord.File('roster_grey.png'))

    if message.content.startswith('!quit'):  # quit
        if message.channel.id in DRAFTING_CHANNEL_IDS:
            await message.channel.send('Draft quit.')
            try:
                await message.channel.purge(check=to_purge)  # purge
            except discord.errors.Forbidden:
                pass
            await photos(message, True)
            DRAFTING_CHANNEL_IDS.pop(message.channel.id)
        else:
            await message.channel.send('No draft has been started in this channel. !help / !draft')

    if shorthand(message.content) in CHAMPIONS:  # draft picks
        if message.channel.id in DRAFTING_CHANNEL_IDS:  # draft confirmed, put it in
            picks = DRAFTING_CHANNEL_IDS[message.channel.id]  # picks variable
            if shorthand(message.content) in picks:
                await message.channel.send('Champion is already picked/banned.')
                return
            for i in range(0, len(picks)):  # put pick in
                if picks[i].isdigit():
                    picks[i] = shorthand(message.content)
                    await photos(message, False)
                    try:
                        await message.channel.send('Team ' + picks[i+1][0] + ' enter pick ' + picks[i+1][-1])  # might crash and be end condition for draft, still doesn't give second thing
                        return
                    except IndexError:  # draft done
                        await message.channel.send('Draft completed.')
                        try:
                            await message.channel.purge(check=to_purge)  # purge
                            await photos(message, True)
                        except discord.errors.Forbidden:
                            pass
                        DRAFTING_CHANNEL_IDS.pop(message.channel.id)
                        return
        else:
            await message.channel.send('No draft has been started in this channel. !help / !draft')


client.run('NDIwNDE5ODQ4Nzc5MjAyNTg0.DX-aDw.RANGwcVRDriJiyyLPXg3uESiuq8')
