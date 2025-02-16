from pyrogram import Client, filters
import os
import time

# Configuração do bot
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dicionário para armazenar vídeos
videos = {}

@app.on_message(filters.private & filters.video)
async def salvar_video(client, message):
    global videos
    video_id = message.video.file_id
    file_name = f"video_{len(videos) + 1}"
    videos[file_name] = video_id
    await message.reply(f"✅ Vídeo salvo como {file_name}.\nUse /play {file_name} para reproduzir.")

@app.on_message(filters.command("play") & filters.group)
async def tocar_video(client, message):
    global videos
    args = message.text.split(" ", 1)
    
    if len(args) < 2:
        await message.reply("❌ Use /play nome_do_video para escolher um vídeo salvo.")
        return
    
    video_name = args[1]
    
    if video_name not in videos:
        await message.reply("❌ Esse vídeo não está salvo.")
        return

    video_id = videos[video_name]
    await client.send_video(message.chat.id, video_id, caption="▶️ Transmitindo agora!")

@app.on_message(filters.command("stop") & filters.group)
async def encerrar_transmissao(client, message):
    await message.reply("⏹️ Transmissão encerrada.")
    # Simulação de encerramento
    time.sleep(3)

app.run()