# -*- coding: utf-8 -*-


from tkinter import *
import tkinter.messagebox
import tkinter as tk

main_window=Tk()
main_window.geometry("850x850")
main_window.title("Youtube Downloader")

window=Frame(main_window)
window.place(relwidth=1,relheight=1)
L_window=Frame(main_window,bg='#2bd0ed',bd=10)
L_window.place(x=160,y=250,height=300,width=540)
#label
background=PhotoImage(file="youtube.png")
back=Label(window,image=background)
back.place(relwidth=1,relheight=1)
l=Label(window,text="Convert and download youtube videos for free",font=("Algerian",15))
l.place(x=200,y=20)
l1=Label(window,text="Choose the resolution of the video you want to download",font=("Calibri",13))
l1.place(x=237,y=120)
infbox=Label(L_window,font=('Calibri',12))
infbox.place(height=278,width=520)

#entries
link_text=StringVar()
e1=Entry(window,textvariable=link_text,font=("Arial",15))
e1.place(x=230,y=70,height=35,width=420)


#defining functions for resolution
def dwld_vid1():
     from pytube import YouTube 
     e1=Entry(window,textvariable=link_text,font=("Arial",15))
     st=e1.get()
     try: 
      #YouTube(st).streams.first().download()
      video = YouTube(st)
      video1=video.streams.filter(progressive=True, file_extension='mp4',res='360p')
      video1.order_by('resolution').desc().first().download()
      infbox['text']="video title:"+video.title,'\n video downloaded!'
      
     
     except:        
         error=tkinter.Tk("error")
         tkinter.messagebox.showinfo('error','error occurred while downloading')
         infbox['text']=''
         error.mainloop()
                  
   

def dwld_vid4():
     from pytube import YouTube 
     e1=Entry(window,textvariable=link_text,font=("Arial",15))
     st=e1.get()
     try: 
      #YouTube(st).streams.first().download()
      video = YouTube(st)
      video1=video.streams.filter(progressive=True, file_extension='mp4',res="720p")
      video1.order_by('resolution').desc().first().download()
      infbox['text']="video title:"+video.title,'\n video downloaded!'
      
      
     except Exception as error :
         print(error)
         error=tkinter.Tk("error")
         tkinter.messagebox.showinfo('error','error occurred while downloading')
         infbox['text']=''
         error.mainloop()
         
     


#button


var=StringVar()
#rb1=Radiobutton(window,text="144p",height=2,width=8,indicator=0,selectcolor="light blue",variable=var,command=dwld_vid1)
#rb1.place(x=250,y=155)

# rb2=Radiobutton(window,text="240p",height=2,width=8,indicator=0,selectcolor="light blue",variable=var,command=dwld_vid2)
# rb2.place(x=320,y=155)

rb3=Radiobutton(window,text="360p",height=2,width=8,indicator=0,selectcolor="light blue",variable=var,command=dwld_vid1)
rb3.place(x=320,y=155)

rb4=Radiobutton(window,text="720p",height=2,width=8,indicator=0,selectcolor="light blue",variable=var,command=dwld_vid4)
rb4.place(x=400,y=155)

rb5=Radiobutton(window,text="Cancel",height=2,width=8,indicator=0,selectcolor="light blue",variable=var,command=main_window.destroy)
rb5.place(x=480,y=155)
# b1=Button(window,text="Search",font=("Arial",13),bg="red",fg="white")
# b1.place(x=670,y=70)

main_window.resizable(False,False)
main_window.mainloop()