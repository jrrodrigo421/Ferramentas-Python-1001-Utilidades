from pytube import YouTube

link = input('Digite o link do video: ')

video = YouTube(link)

print('Selecione um formato: ')
for stream in video.streams:
    print(stream)

opcao = int(input())

video.streams[opcao].download()
print('Download concluido')
