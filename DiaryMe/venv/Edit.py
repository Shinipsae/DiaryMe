import tkinter
import Main
import pymysql
import Showlist
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

class Edit(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        # 답변 수정하기
        frame1 = Frame(self)
        frame1.pack(fill=X)

        fontStyle = tkFont.Font(family="궁서체", size=20)
        lbl = tkinter.Label(frame1, text="답변 수정하기", font=fontStyle)
        lbl.pack(side=TOP, pady=20)

        # 질문
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl_question = Label(frame2, text="수정하고 싶은 답변의 번호를 적어주세요.", width=35)
        lbl_question.pack(side=LEFT, pady=10)

        entry_no = Entry(frame2)
        entry_no.insert(0, '해당 번호를 정확하게 적어주세요.')
        entry_no.pack(fill=X, padx=10, expand=True)

        # 답변
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand = True)

        lbl_answer = Label(frame3, text="수정하고 싶은 답변의 내용을 적어주세요.", width=35)
        lbl_answer.pack(side=LEFT, anchor=N, pady=10)

        text_answer = Text(frame3)
        text_answer.insert(tkinter.CURRENT, "답변을 수정해주세요 :)")
        text_answer.pack(fill=X, padx=10, pady=10)

        # 저장
        frame4 = Frame(self)
        frame4.pack(fill=X)

        btn_edit = Button(frame4, text="수정하기", command=lambda: self.onClick_edit(entry_no, text_answer))
        btn_edit.pack(side=LEFT, padx=220, pady=10)

    def onClick_edit(self, entry_no, text_answer):
        cursor = conn.cursor()
        sql = f"select max(id) from member"
        cursor.execute(sql)
        number = int(cursor.fetchone()[0])

        edit_no = int(entry_no.get())
        edit_answer = text_answer.get('1.0', 'end')

        if number >= edit_no:
            cursor1 = conn.cursor()
            sql1 = f"update `diaryme`.`member` set `content`='{edit_answer}' where(`id` = '{edit_no}')"
            cursor1.execute(sql1)
            conn.commit() # insert에서 꼭 필요 !!!!!!!!!!
            conn.close()
            tkinter.messagebox.showinfo("Diary Me",
                                        "답변이 정상적으로 수정되었어요. ♡" +
                                        " \n 프로그램 재실행 후 수정된 내용이 적용돼요 !!")

        else:
            tkinter.messagebox.showerror("Error", "아직 답변하지 않은 질문들은 수정할 수 없어요.")

def main():


    root = Tk()
    root.geometry("500x500+1200+200") # 뒷 숫자는 초기화면 위치
    root.resizable(False, False)
    app = Edit(root)
    root.mainloop()

if __name__ == '__main__':
    main()


