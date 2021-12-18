from pytube import YouTube

links = []

print('Enter the number of video\'s you have: ')
video_counter = int(input('> '))
print('Enter location where you want to download the videos: ')
path = input('> ')
print('Enter the resolution [include p at the end]: ')
res = input('> ')

counter = 0
while counter < video_counter:
    print('Enter video URL: ')
    url = input('> ')
    links.append(url)
    counter += 1

for link in links:
    try:
        print('Downloading Video...')
        yt = YouTube(link)
        yt.streams.filter(res=res).first().download(path)
    except:
        print('Connection Error. Downloading Failed')