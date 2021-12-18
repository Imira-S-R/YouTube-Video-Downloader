from pytube import YouTube
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--url', '-u', type=str, help="URL of the video you want to download", default='no')
parser.add_argument('--path', '-p', type=str, help="location where you want to download the video", default='no')
parser.add_argument('--res', '-r', type=str, help="resolution [do not include p at the end]", default='no')
args = parser.parse_args()

if args.url != 'no' and args.path != 'no' and args.res != 'no':
    try:
        yt = YouTube(args.url)
    except:
        print('Connection Error. Downloading Failed')

    print('Downloading video...')
    yt.streams.filter(res=f'{args.res}p', progressive=True).first().download(args.path)
    exit()

print('Enter URL of the video you want to download: ')
link = input('> ')
print('Enter location where you want to download the video: ')
path = input('> ')
print('Enter the resolution [do not include p at the end]: ')
res = input('> ')

try:
    yt = YouTube(link)
except:
    print('Connection Error. Downloading Failed')

print('Downloading video...')
yt.streams.filter(res=f'{res}p', progressive=True).first().download(path)
