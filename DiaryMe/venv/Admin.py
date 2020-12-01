import tkinter
import Main
import pymysql
import Showlist
import Showlist_admin
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from math import *

conn = pymysql.connect(
    user='root',
    passwd='mysql',
    host='127.0.0.1',
    db='diaryme',
    charset='utf8'
)

class Admin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        # 답변 수정하기
        frame1 = Frame(self)
        frame1.pack(fill=X)

        fontStyle = tkFont.Font(family="궁서체", size=20)
        lbl = tkinter.Label(frame1, text="질문 등록하기", font=fontStyle)
        lbl.pack(side=TOP, pady=20)

        # 답변
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand = True)

        lbl_question = Label(frame2, text="질문", width=5)
        lbl_question.pack(side=LEFT, anchor=N, padx=10, pady=10)

        text_question = Text(frame2)
        text_question.insert(tkinter.CURRENT, "질문을 등록해주세요")
        text_question.pack(side=LEFT, padx=10, pady=10)

        # 저장
        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_insert = Button(frame3, text="질문등록하기", command=lambda: self.onClick_edit(text_question))
        btn_insert.pack(side=LEFT, padx=210)

        frame5 = Frame(self)
        frame5.pack(fill=X)

    def onClick_edit(self, text_question):
        insert_answer = text_question.get('1.0', 'end')
        cursor1 = conn.cursor()
        sql1 = f"insert into `diaryme`.`question` (`question`) values ('{insert_answer}')"
        # INSERT INTO `diaryme`.`question` (`question`) VALUES ('살면서 들어본 칭찬 중 가장 기억에 남는 것은?');
        cursor1.execute(sql1)
        conn.commit() # insert에서 꼭 필요 !!!!!!!!!!

        tkinter.messagebox.showinfo("Diary Me",
        "질문이 정상적으로 등록되었습니다. \n 프로그램 재실행 후 수정된 내용이 적용됩니다.")
        conn.close() # 짝 맞춰서 닫기

    def onClick_show(self):
        Showlist_admin.main(conn)

def main():

    root = Tk()
    root.geometry("500x500+400+400") # 뒷 숫자는 초기화면 위치
    root.resizable(False, False)
    app = Admin(root)
    root.mainloop()

if __name__ == '__main__':
    main()


