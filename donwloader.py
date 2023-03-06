from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Entrada do Link
link = input("Digite o link do vídeo que deseja baixar: ")

# Entrada do path para o download
# input("Digite o diretório que deseja salvar o vídeo: ") --opção para deixar o usuário escolher o arquivo
path = "C:\Downloads"

yt = YouTube(link)

print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo!")

# Conversão do arquivo MP3
print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucesso! Salvo em C:\Downloads')
