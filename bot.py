from pyrogram import Client, filters
import os
import time

# Configuração do bot
API_ID = os.getenv("API_ID")
print(f"API_ID lido: {API_ID}")
API_ID = int(API_ID)  # Converter depois de garantir que não está None

API_HASH = os.getenv("API_HASH")
print(f"API_HASH lido: {API_HASH}")

BOT_TOKEN = os.getenv("BOT_TOKEN")
print(f"BOT_TOKEN lido: {BOT_TOKEN}")

CANAL_ID = os.getenv("CANAL_ID")
print(f"CANAL_ID lido: {CANAL_ID}")
CANAL_ID = int(CANAL_ID)  # Converter depois de garantir que não está None

ADMIN_ID = os.getenv("ADMIN_ID")
print(f"ADMIN_ID lido: {ADMIN_ID}")
ADMIN_ID = int(ADMIN_ID)  # Converter depois de garantir que não está None

# Configurações do Restream
RTMP_URL = "rtmp://live.restream.io:1935/live"  # URL RTMP do Restream
STREAM_KEY = "re_9233211_57fe94b181ddc2990e45"  # Substitua pela chave de transmissão do Restream

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dicionário para armazenar vídeos
videos = {}

@app.on_message(filters.private & filters.video)
async def salvar_video(client, message):
    global videos
    video_id = message.video.file_id
    file_name = f"video_{len(videos) + 1}"
    videos[file_name] = video_id
    await message.reply(f"✅ Vídeo salvo como **{file_name}**.\nUse `/play {file_name}` para iniciar a transmissão ao vivo no canal.")

@app.on_message(filters.command("play") & filters.private)
async def iniciar_transmissao(client, message):
    global videos
    args = message.text.split(" ", 1)
    
    if len(args) < 2:
        await message.reply("❌ Use `/play nome_do_video` para escolher um vídeo salvo.")
        return
    
    video_name = args[1]
    
    if video_name not in videos:
        await message.reply("❌ Esse vídeo não está salvo.")
        return

    video_id = videos[video_name]
    await message.reply("🎥 Iniciando transmissão ao vivo no canal...")

        # Iniciar a transmissão para o Restream com FFmpeg
    command = [
        'ffmpeg',
        '-re', 
        '-i', downloaded_file, 
        '-c:v', 'libx264',
        '-preset', 'fast', 
        '-c:a', 'aac', 
        '-f', 'flv', 
        f'{rtmp://live.restream.io:1935/live}/{re_9233211_57fe94b181ddc2990e45}'
    ]

    # Simula o início da transmissão ao vivo
    await client.send_video(CANAL_ID, video_id, caption="🔴 Transmissão ao vivo iniciada!")
    
    # Tempo de transmissão (simulação)
    time.sleep(10)  # Substitua pelo tempo real do vídeo se necessário
    
    # Finaliza a transmissão
    await client.send_message(CANAL_ID, "Espero que tenha gostado meu amor, me conta o que achou no pv amor <3")
    await client.send_message(ADMIN_ID, "✅ A transmissão terminou com sucesso!")

app.run()
