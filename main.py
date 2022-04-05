import discord
import re
import random

token_file = open('token.txt', 'r')
TOKEN = token_file.readline()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$#'):
            col = message.content[1::].upper()

            # quangbuiid = 420809158170902528;
            # if message.author.id == quangbuiid:
            #     await message.channel.send('del cho, haha')
            #     return
            
            print(col)

            if (col == '#RANDOM'):
                user = message.author

                # delete previous roles
                to_be_deleted = []
                for r in user.roles:
                    if (re.match(r"^[0-9A-F]{6}$", r.name.upper())):
                        to_be_deleted.append(r)

                for r in to_be_deleted:
                    await user.remove_roles(r)

                # create and assign new role
                r = lambda: random.randint(0,255)
                col = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())[1::]
                rid = -1
                for r in message.guild.roles:
                    if r.name == col:
                        rid = r.id
                
                if rid == -1:
                    role = await message.guild.create_role(name=col, permissions=discord.Permissions(0), colour=discord.Colour(int('0x' + col, 16)))
                    rid = role.id

                await user.add_roles(message.guild.get_role(rid))
            elif (re.match(r"^#[0-9A-F]{6}$", col)):
                user = message.author

                # delete previous roles
                to_be_deleted = []
                for r in user.roles:
                    if (re.match(r"^[0-9A-F]{6}$", r.name.upper())):
                        to_be_deleted.append(r)

                for r in to_be_deleted:
                    await user.remove_roles(r)

                # create and assign new role
                col = col[1::]
                rid = -1
                for r in message.guild.roles:
                    if r.name == col:
                        rid = r.id
                
                if rid == -1:
                    role = await message.guild.create_role(name=col, permissions=discord.Permissions(0), colour=discord.Colour(int('0x' + col, 16)))
                    rid = role.id

                await user.add_roles(message.guild.get_role(rid))
            else:
                await message.channel.send('#random or a valid hex color plz 🥺')

client = MyClient()
client.run(TOKEN)