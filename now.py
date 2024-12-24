from yt_dlp import YoutubeDL



def startdownload():

    try:
        yt_dlp_link ='https://www.youtube.com/shorts/ZqS_lnqSgeY'
        # Configuration for YoutubeDL
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([yt_dlp_link])

        print("Download Complete!")
    except Exception as e:
        print("Error:", e)


def startaudo():

    try:
        yt_dlp_link ='https://www.youtube.com/shorts/3sSSMX2PK_g?feature=share'
        # Configuration for YoutubeDL
        ydl_opts = {
            'extract_audio': True,
            'format': 'bestaudo',
            'outtmpl': '%(title)s.mp3'
        }

        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([yt_dlp_link])

        print("Download Complete!")
    except Exception as e:
        print("Error:", e)