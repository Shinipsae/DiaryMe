import tkinter
import Question
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.font as tkFont

# html_head ='''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title> Diary Me </title>
# </head>
# '''
#
# html_body = '''
# <body>
#     <li>{questionNo}</li>
#     <li>{question}</li>
# </body>
# '''

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
print(rows)
conn.close()

class DiaryMain(Frame):
    # 생성자
    def __init__(self, master):
        # 이미지
        img = PhotoImage(file='diary.png')
        lblImage = Label(image=img)
        lblImage.image = img
        lblImage.place(x=0, y=0)

        # 오늘의 질문은?
        fontStyle = tkFont.Font(family="궁서체", size=20)
        lblText = Label(text='오늘의 질문은?', font=fontStyle)
        lblText.pack()
        lblText.place(x=160, y=150)

        # 오늘의 질문 보러가기
        lblButton1 = Button(text='오늘의 질문 보러가기', command=onClick_question)
        lblButton1.pack()
        lblButton1.place(x=200, y=240)

        # 전 답변 목록
        lblButton2 = Button(text='전 답변 목록들 보러가기')
        lblButton2.pack()
        lblButton2.place(x=192, y=290)

        # 도움말
        lblButton3 = Button(text='Diary Me?', command=onClick_info)
        lblButton3.pack()
        lblButton3.place(x=390, y=15)

# 도움말
def onClick_info():
    tkinter.messagebox.showinfo("Diary Me?",
    "여러분은 '나'라는 사람에 대해서 얼마나 잘 알고 계신가요? \n"+
    "행복은 나 자신을 아는 것으로부터 시작된다는 말이 있습니다.\n"+
    "Diary Me는 진정한 '나'를 알 수 있는 질문들로 여러분들에게 \n" +
    "진정한 힐링을 제공합니다. \n\n" +
    "1. 오늘의 질문을 확인하고, 답장할 수 있어요. \n"+
    "2. 자신이 답변한 질문들을 확인할 수 있어요. \n"+
    "3. 하루하루 자신을 알아가면서 힐링을 누리세요.")

def onClick_question():
    Question.main()

def onClick_show():
    pass
    # f = open('showList.html', 'w', encoding='utf-8')
    # f.write(html_head + html_body.format(
    #     questionNo=a, question=b))
    # f.close()

def main():
    root= Tk()
    root.title('Diary Me')
    root.geometry("500x500+100+100")
    root.resizable(False, False)
    app = DiaryMain(root)
    root.mainloop()

if __name__ == '__main__':
    main()


