import tkinter
import Question
import Showlist
import pymysql
import datetime
import test
import Admin
import Admin_check
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

conn = pymysql.connect(
    user='root',
    passwd='mysql',
    host='127.0.0.1',
    db='diaryme',
    charset='utf8'
)

cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)

rows = cursor.fetchall()
# fetchone()은 한 줄, fetchmany(n)은 n줄

class DiaryMain(Frame):
    # 생성자
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        # 이미지
        img = PhotoImage(file='diary.png')
        lblImage = Label(image=img)
        lblImage.image = img
        lblImage.place(x=0, y=0)

        # 오늘의 질문은?
        fontStyle = tkFont.Font(family="궁서체", size=20)
        lblText = Label(text='   Diary Me   ', font=fontStyle)
        lblText.pack()
        lblText.place(x=160, y=150)

        # 오늘의 질문 보러가기
        lblButton1 = Button(text='오늘의 질문 보러가기', command=onClick_question)
        lblButton1.pack()
        lblButton1.place(x=200, y=240)

        # 전 답변 목록
        lblButton2 = Button(text='이전 답변 목록들 보러가기', command=onClick_show)
        lblButton2.pack()
        lblButton2.place(x=185, y=290)

        # 도움말
        lblButton3 = Button(text='Diary Me?', command=onClick_info)
        lblButton3.pack()
        lblButton3.place(x=390, y=15)

        lblButton4 = Button(text='admin', command=onClick_admin)
        lblButton4.pack()
        lblButton4.place(x=390, y=45)

# 도움말
def onClick_info():
    tkinter.messagebox.showinfo("Diary Me?",
    "여러분은 '나'라는 사람에 대해서 얼마나 잘 알고 계신가요? \n"+
    "행복은 나 자신을 아는 것으로부터 시작된다는 말이 있습니다.\n"+
    "Diary Me는 '나'에 대해서 알아보는 질문들로 \n" +
    "여러분들에게 진정한 행복을 찾을 수 있도록 도와줍니다.\n\n" +
    "1. 오늘의 질문을 확인하고, 답장할 수 있어요. \n"+
    "2. 자신이 답변한 질문들을 확인할 수 있어요. \n"+
    "3. 나에 대한 질문은 하루에 한 개씩만 제공됩니다. \n"+
    "4. 하루하루 자신을 알아가면서 힐링을 누리세요.")

def onClick_question():
    now = str(datetime.datetime.now())
    # 현재 날짜를 숫자화한것
    now_int = int(now[0:4]) * 365 + int(now[5:7]) * 30 + int(now[8:10])

    # 어디까지 질문이 나갔는지
    cursor1 = conn.cursor()
    sql1 = f"select max(id) from member"
    cursor1.execute(sql1)
    number = cursor1.fetchone()[0]

    # 가장 마지막 질문 날짜 구함
    cursor2 = conn.cursor()
    sql2 = f"select date from diaryme.member where id = {number}"
    cursor2.execute(sql2)
    date = cursor2.fetchone()[0]
    short_date = str(date)[0:10]

    conn.close()

    # 마지막 질문 날짜를 숫자화 한것
    short_date_int = int(short_date[0:4]) * 365 + int(short_date[5:7]) * 30 + int(short_date[8:10])

    # 오늘이 마지막 질문 날짜보다 많으면(24시간이 지났으면)
    if now_int > short_date_int:
        Question.main()
    else:
        tkinter.messagebox.showinfo("Diary Me",
        "Diary Me의 질문들은 하루에 한 번씩 제공됩니다.\n"+
        f"마지막 답변 일시는 {date} 이에요. \n"
        f"조금만 기다려주세요 :) ♡")

def onClick_show():
    Showlist.main()

def onClick_admin():
    msg = tkinter.messagebox.askquestion("Admin page", "당신은 관리자이십니까?")
    if msg == 'yes':
        Admin_check.main()
    else:
        pass

def main():

    root= Tk()
    root.title('Diary Me')
    root.geometry("500x500+100+100")
    root.resizable(False, False)
    app = DiaryMain(root)
    root.mainloop()

if __name__ == '__main__':
    main()


