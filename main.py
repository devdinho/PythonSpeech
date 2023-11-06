from gtts import gTTS

text = input('Digite um texto:')
lang = "pt"
tld = "com.br"

tts = gTTS(text,lang=lang,tld=tld)

tts.save(f'{text[:20].strip()}.mp3')