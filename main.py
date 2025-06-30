import edge_tts
import asyncio

text = input('Digite um texto:')
lang = "pt-BR"
voice = "AntonioNeural"

async def generate_audio(text, lang, voice):
    communicate = edge_tts.Communicate(text, "{}-{}".format(lang, voice))
    
    # async for chunk in communicate.stream():
    #     if chunk['type'] == 'audio':
    #         with open('output.mp3', 'wb') as audio_file:
    #             audio_file.write(chunk['data'])
    
    await communicate.save("output.mp3")

asyncio.run(generate_audio(text, lang, voice))