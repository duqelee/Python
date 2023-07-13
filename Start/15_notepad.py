#from tkinter import *
#
#top = Tk() # top이라는 변수에 Tk 생성자로 윈도우 객체 저장
#top.mainloop() # 윈도우창 유지

from tkinter import *
from tkinter.filedialog import *
import os

def newFile():
    top.title("제목없음 - 노트패드")
    ta.delete(1,0,END) #1=Y좌표, 0=X좌표, Y줄은  1부터 시작임.
def openFile():
    file=askopenfilename(initialdir="/", title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
    top.title(os.path.basename(file) + " - 노트패트")
    ta.delete(1.0,END)
    f=open(file, "r")
    ta.insert(1.0,f.read())
    f.close()
def saveFile():
    f=asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    ts=str(ta.get(1.0,END))
    f.write(ts)
    f.close()

top=Tk()
top.title("노트패드")
top.geometry("400x400")

ta=Text(top) #text의 오른쪽위의 객체 top
sb=Scrollbar(ta) #스크롤바의 상위객체 ta(text)
sb.config(command=ta.yview)
top.grid_rowconfigure(0, weight=1) #줄을 전체 크기로
top.grid_columnconfigure(0, weight=1) #열을 전체 크기로
sb.pack(side=RIGHT, fill=Y)
ta.grid(sticky=N+E+S+W)

mb=Menu(top)
fi=Menu(mb, tearoff=0)
fi.add_command(label="새파일", command=newFile)
fi.add_command(label="열기", command=openFile)
fi.add_command(label="저장", command=saveFile)
fi.add_separator()
fi.add_command(label="종료", command=top.destroy)
fi.add_cascade(label="파일", menu=fi) #파일 메뉴를 메뉴바에 붙이기

top.config(menu=mb)
top.mainloop()