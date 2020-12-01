import tkinter
import Main
import pymysql
import Showlist
import Showlist_admin
import Admin
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from math import *

class Admin_check(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        # 답변 수정하기
        frame1 = Frame(self)
        frame1.pack(fill=X)

        fontStyle = tkFont.Font(family="궁서체", size=20)
        lbl = tkinter.Label(frame1, text="관리자 로그인", font=fontStyle)
        lbl.pack(side=TOP, pady=20)

        # 답변
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand = True)

        lbl_pw = Label(frame2, text="비밀번호", width=10)
        lbl_pw.pack(side=LEFT, padx=10, pady=10)

        entry_pw = Entry(frame2)
        entry_pw.pack(fill=X, padx=10, expand=True)

        # 저장
        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_insert = Button(frame3, text="로그인", command=lambda: self.onClick_login(entry_pw))
        btn_insert.pack(side=LEFT, padx=220, pady=10)

    def onClick_login(self, entry_pw):
        pw = entry_pw.get()
        if pw == '12341234':
            Showlist_admin.main()
        else:
            tkinter.messagebox.showerror("Get out", "당신, 관리자 아니지!!! \n 들어오지마세요...")
            Main.main()

def main():

    root = Tk()
    root.geometry("500x500+200+200") # 뒷 숫자는 초기화면 위치
    root.resizable(False, False)
    app = Admin_check(root)
    root.mainloop()

if __name__ == '__main__':
    main()


