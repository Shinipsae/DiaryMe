import tkinter
import Main
import pymysql
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

# 마지막 answer의 번호를 가져옴
cursor1 = conn.cursor()
sql1 = "select max(id) from member"
cursor1.execute(sql1)
max_no = cursor1.fetchone()  # 튜플
max = max_no[0] + 1 #  4 를 질문 번호에 넣는다.

# 새로운 질문을 가져옴
cursor2 = conn.cursor()
sql2 = f"select question from question where id={max}"
cursor2.execute(sql2)
question = cursor2.fetchone()[0]

class Diary(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        # 질문번호
        frame1= Frame(self)
        frame1.pack(fill=X)

        lbl_no = Label(frame1, text="질문번호", width=10)
        lbl_no.pack(side=LEFT, padx = 10, pady = 10)

        entry_no = Entry(frame1)
        entry_no.insert(0, max)
        entry_no.configure(state='readonly')
        entry_no.pack(fill=X, padx =10, expand=True)

        # 질문
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl_question = Label(frame2, text="질문", width=10)
        lbl_question.pack(side=LEFT, padx=10, pady=10)

        entry_question = Entry(frame2)
        entry_question.insert(0, question)
        entry_question.configure(state='readonly')
        entry_question.pack(fill=X, padx=10, expand=True)

        # 답변
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand = True)

        lbl_answer = Label(frame3, text="답변", width=10)
        lbl_answer.pack(side=LEFT, anchor=N, padx=10, pady=10)

        text_answer = Text(frame3)
        text_answer.insert(tkinter.CURRENT, "자신만의 답변을 입력하세요 :)")
        text_answer.pack(fill=X, padx=10, pady=10)

        # 저장
        frame4 = Frame(self)
        frame4.pack(fill=X)
        btn_save = Button(frame4, text="저장", command=lambda: self.onClick_save(text_answer))
        btn_save.pack(side=LEFT, padx=220, pady=10)

    def onClick_save(self, text_answer):
        answer = text_answer.get('1.0', 'end')
        cursor3 = conn.cursor()
        sql3 = f"insert into `diaryme`.`member` (`content`) values ('{answer}')"
        cursor3.execute(sql3)
        conn.commit() # insert에서 꼭 필요 !!!!!!!!!!
        conn.close() # 짝 맞춰서 닫기
        tkinter.messagebox.showinfo("Diary Me",
        "오늘도 '나'와 한걸음 더 가까워지셨네요! ♥")
        Main.main()


def main():

    root = Tk()
    root.geometry("500x500+200+200") # 뒷 숫자는 초기화면 위치
    root.resizable(False, False)
    app = Diary(root)
    root.mainloop()

if __name__ == '__main__':
    main()


