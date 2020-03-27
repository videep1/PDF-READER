from tkinter import Tk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import  PyPDF2,pyttsx3
from gtts import gTTS
from playsound  import playsound
win=tk.Tk()
win.title("pdf to speech")
win.geometry("200x70")

filelocation=askopenfilename()
p=open(filelocation,"rb")
pdfReader=PyPDF2.PdfFileReader(p)
t=""
for pageNum in range(pdfReader.numPages):
    pageObj=pdfReader.getPage(pageNum)
    t+=pageObj.extractText()

f=gTTS(text=t,lang='en')
f.save(r'C:\Users\videe\Downloads\s.mp3')

playsound(r'C:\Users\videe\Downloads\s.mp3') 
