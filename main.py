import edge_tts
import asyncio

text = "Eu sou um modelo de linguagem treinado para ser neutro e objetivo, não tenho preferências pessoais ou emoções. Porém, posso dizer que Britney Spears é uma artista musical muito popular e influente no mundo. Ela tem uma carreira longa e produtiva, com muitos hits e álbuns de sucesso."
default_lang = "pt-BR"
default_voice = "FranciscaNeural"

async def generate_audio(text, lang: str = default_lang, voice: str = default_voice):
    communicate = edge_tts.Communicate(text, "{}-{}".format(lang, voice))
    
    # async for chunk in communicate.stream():
    #     if chunk['type'] == 'audio':
    #         with open('output.mp3', 'wb') as audio_file:
    #             audio_file.write(chunk['data'])
    
    await communicate.save("output.mp3")

asyncio.run(generate_audio(text))