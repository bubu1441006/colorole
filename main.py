import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$#'):
            col = message.content[2::]
            print(col)
            user = message.author
            role = await message.guild.create_role(name=col, permissions=discord.Permissions(0), colour=discord.Colour(int('0x' + col, 16)))
            await user.add_roles(message.guild.get_role(role.id))

client = MyClient()
client.run('OTYwNDIwNjgyMzg1MjIzNjgw.YkqLdg.kmW0WthTW6eSbYFqjtuhEPSj8d0')