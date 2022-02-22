import discord

def main(mess):

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as user {}'.format(client.user.name))
        channel = client.get_channel(796477959766278264)
        await channel.send(mess)

    client.run("Nzk2MDEyMDQ3OTUxMjAwMzM4.X_Rt_Q.K8lT1vL5sDTPLyQCosc8smn3Dt8")

