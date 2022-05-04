import gtts
from playsound import playsound

palavras = ''
print('Digite seu texto: ')
while palavras != 'sair':
  palavras = input('$ ')
  frase = gtts.gTTS(palavras,lang='pt')
  frase.save('frase.mp3')
  playsound('frase.mp3')

