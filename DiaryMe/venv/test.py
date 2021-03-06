import tkinter
import Main
import pymysql
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *

conn = pymysql.connect(
    user='root',
    passwd='mysql',
    host='127.0.0.1',
    db='diaryme',
    charset='utf8'
)

class ShowList(Frame):
    # 생성자
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Diary Me")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        img = PhotoImage(file='background.png')
        lblImage = Label(frame1, image=img)
        lblImage.image = img
        lblImage.place(x=0, y=0)

        fontStyle = tkFont.Font(family="궁서체", size=20)
        lbl = tkinter.Label(frame1, text="질문목록", font=fontStyle)
        lbl.pack(side=TOP, pady=20)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        img1 = PhotoImage(file='background.png')
        lblImage1 = Label(frame2, image=img1)
        lblImage1.image = img1
        lblImage1.place(x=0, y=0)

        # 표
        treeview = tkinter.ttk.Treeview(frame2, columns=["one"],
                                        displaycolumns=["one"],
                                        height=50) # height default=10

        vsb = tkinter.ttk.Scrollbar(frame2, orient="vertical",
                                command=treeview.yview)
        vsb.pack(side='right', fill=Y)

        treeview.configure(yscrollcommand=vsb.set)

        treeview.column("#0", width=50, anchor="w")
        treeview.heading("#0", text="번호", anchor="center")

        treeview.column("#1", width=360, anchor="center")
        treeview.heading("one", text="질문", anchor="center")

        question_list = ['-'] * 50

        for i in range(1, number + 1):
            cursor1 = conn.cursor()

            # 질문
            sql1 = f"select question from diaryme.question where id = {i}"
            # 답변
            sql2 = f"select content from diaryme.member where id = {i}"
            # 답변일시
            sql3 = f"select date from diaryme.member where id = {i}"

            cursor1.execute(sql1)
            cursor2.execute(sql2)
            cursor3.execute(sql3)

            question_list[i - 1] = cursor1.fetchone()[0]
            answer_list[i - 1] = cursor2.fetchone()[0]
            # 날짜까지로 변환
            date = cursor3.fetchone()[0]
            short_date = str(date)[0:10]
            date_list[i - 1] = short_date

        conn.close()

        # 리스트에 tuple을 초기화 이후에 어떻게 더하는지 몰라서...
        treelist = [("-", "-", "-"),
                    (question_list[0], answer_list[0], date_list[0]),
                    (question_list[1], answer_list[1], date_list[1]),
                    (question_list[2], answer_list[2], date_list[2]),
                    (question_list[3], answer_list[3], date_list[3]),
                    (question_list[4], answer_list[4], date_list[4]),
                    (question_list[5], answer_list[5], date_list[5]),
                    (question_list[6], answer_list[6], date_list[6]),
                    (question_list[7], answer_list[7], date_list[7]),
                    (question_list[8], answer_list[8], date_list[8]),
                    (question_list[9], answer_list[9], date_list[9]),

                    (question_list[10], answer_list[10], date_list[10]),
                    (question_list[11], answer_list[11], date_list[11]),
                    (question_list[12], answer_list[12], date_list[12]),
                    (question_list[13], answer_list[13], date_list[13]),
                    (question_list[14], answer_list[14], date_list[14]),
                    (question_list[15], answer_list[15], date_list[15]),
                    (question_list[16], answer_list[16], date_list[16]),
                    (question_list[17], answer_list[17], date_list[17]),
                    (question_list[18], answer_list[18], date_list[18]),
                    (question_list[19], answer_list[19], date_list[19]),

                    (question_list[20], answer_list[20], date_list[20]),
                    (question_list[21], answer_list[21], date_list[21]),
                    (question_list[22], answer_list[22], date_list[22]),
                    (question_list[23], answer_list[23], date_list[23]),
                    (question_list[24], answer_list[24], date_list[24]),
                    (question_list[25], answer_list[25], date_list[25]),
                    (question_list[26], answer_list[26], date_list[26]),
                    (question_list[27], answer_list[27], date_list[27]),
                    (question_list[28], answer_list[28], date_list[28]),
                    (question_list[29], answer_list[29], date_list[29]),

                    (question_list[30], answer_list[30], date_list[30]),
                    (question_list[31], answer_list[31], date_list[31]),
                    (question_list[32], answer_list[32], date_list[32]),
                    (question_list[33], answer_list[33], date_list[33]),
                    (question_list[34], answer_list[34], date_list[34]),
                    (question_list[35], answer_list[35], date_list[35]),
                    (question_list[36], answer_list[36], date_list[36]),
                    (question_list[37], answer_list[37], date_list[37]),
                    (question_list[38], answer_list[38], date_list[38]),
                    (question_list[39], answer_list[39], date_list[39]),

                    (question_list[40], answer_list[40], date_list[40]),
                    (question_list[41], answer_list[41], date_list[41]),
                    (question_list[42], answer_list[42], date_list[42]),
                    (question_list[43], answer_list[43], date_list[43]),
                    (question_list[44], answer_list[44], date_list[44]),
                    (question_list[45], answer_list[45], date_list[45]),
                    (question_list[46], answer_list[46], date_list[46]),
                    (question_list[47], answer_list[47], date_list[47]),
                    (question_list[48], answer_list[48], date_list[48]),
                    (question_list[49], answer_list[49], date_list[49])]

        print(len(treelist))
        for i in range(1, len(treelist)):
            treeview.insert('', 'end', text=i,
                            values=treelist[i], iid=str(i) + "번")

        treeview.pack(pady=30)

def main():
    conn = pymysql.connect(
        user='root',
        passwd='mysql',
        host='127.0.0.1',
        db='diaryme',
        charset='utf8'
    )

    root = Tk()
    root.geometry("1000x500+100+100")
    root.resizable(False, False)
    app = ShowList(root)
    root.mainloop()


if __name__ == '__main__':
    main()