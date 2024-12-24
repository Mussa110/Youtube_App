from pytube import YouTube 

try:
    link = input ('https://www.youtube.com/shorts/ZqS_lnqSgeY')

    y = YouTube(link)
    video = y.streams.get_lowest_resolution()

    video.download
except:
    print('oh sorry there is an error man ')
print('wow is done enjoy by your video ma man ')