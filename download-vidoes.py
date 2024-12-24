
from yt_dlp import YoutubeDL
import tkinter 
import customtkinter as ct

ct.set_appearance_mode('system')

ct.set_default_color_theme('blue')
app =ct.CTk()
app.title('YooTube_110')
app.geometry('700x400')

def download_audio():
    link = enter1.get()
    with YoutubeDL({'extract_audio': True,
                            'format': 'bestaudio',
                            'outtmpl': '%(title)s.mp3'}) as video:
        

        info_dict = video.extract_info(link, download = True)
        video_title = info_dict['title']
        title2.configure(text=video_title)
        video.download(link)    
        flabel.configure(text='.. we done man have fun ..', text_color='green')
        c()



def c ():
    title1.configure(text='download onther one')
    enter1.delete(0,'end')

def startdownload():
    
    yt_dlp_link = enter1.get()
    if not yt_dlp_link.strip():
        flabel.configure(text="Error: The URL cannot be empty." ,text_color='red')
        return
    try:
        # Configuration for YoutubeDL
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as yt_dlp_object:
            info = yt_dlp_object.extract_info(yt_dlp_link)
            t =  info['title']
            title2.configure(text=t)
            yt_dlp_object.download([yt_dlp_link])
       
        flabel.configure(text='.. we done man have fun ..', text_color='green')
        c()
    except Exception as e:
        print('sorry', e)




title1 =ct.CTkLabel(app, text='Welcome to YouTube Downloader',width=400)
title1.pack(pady=20)

title2 =ct.CTkLabel(app, text='',width=400)
title2.pack(pady=20)


link= tkinter.StringVar()
enter1 =ct.CTkEntry(app,placeholder_text='put the link donw here ',width=400,height=40,textvariable=link )
enter1.pack(pady=10)

flabel= ct.CTkLabel(app, text='',text_color='green')
flabel.pack()

# prg= ct.CTkProgressBar(app, width=400)
# prg.set(0)
# prg.pack(pady=10)

b1 = ct.CTkButton(app,text='Get it as video' ,command=startdownload)
b1.pack(pady=10)
b2 = ct.CTkButton(app,text='Get it  as Mp3' ,command=download_audio)
b2.pack()




app.mainloop()