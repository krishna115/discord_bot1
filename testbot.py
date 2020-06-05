import discord
client = discord.Client()
name=["wait"]
number=[]
@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hello " + str(message.author))
    if message.content.startswith("I would like to register"):
        st = str(message.author)
        for key in name:
            if key==st:
                await message.channel.send(st+" , You are already registered")
            else:
                name.append(st)
                await message.channel.send("For Registration we would like to have your paytm number")
                await message.channel.send("Enter your number: ")

        print(name)
       # await message.channel.send("Enter your number: ")
       # number.append(message.content)

    if message.content.startswith("bye"):
         await message.channel.send("good bye have a good time")
   # if message.content.startswith("hello"):
    #    await message.channel.send("hello")
client.run("NzE4MDM5NjgxMTQ4NjQ5NDgz.XtkmeQ.5imtmZjAX6dG17CDxlFS2ifPpJQ")

