from pyrogram import Client, filters
import os
import time

# Configuração do bot
API_ID = int(os.getenv("27698619"))
API_HASH = os.getenv("910ab6da6964e3b86b20e561f823ebf")
BOT_TOKEN = os.getenv("7843820539:AAHGj-bhPmwCwWHKGGXqTwtjfu_oYtdqMOA")
CANAL_ID = int(os.getenv("-1002421357308"))  # ID do canal onde a transmissão acontecerá
ADMIN_ID = int(os.getenv("7820632930"))  # Seu ID para receber notificações no privado

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
    
    # Simula o início da transmissão ao vivo
    await client.send_video(CANAL_ID, video_id, caption="🔴 Transmissão ao vivo iniciada!")
    
    # Tempo de transmissão (simulação)
    time.sleep(10)  # Substitua pelo tempo real do vídeo se necessário
    
    # Finaliza a transmissão
    await client.send_message(CANAL_ID, "Espero que tenha gostado meu amor, me conta o que achou no pv amor <3")
    await client.send_message(ADMIN_ID, "✅ A transmissão terminou com sucesso!")

app.run()
