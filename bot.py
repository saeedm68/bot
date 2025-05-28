from pyrogram import Client

api_id = 23437892
api_hash = "6546553056c918361f944748211325d3"

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

@app.on_message()
def handle(client, message):
    message.reply("سلام! من فعال هستم.")

app.run()