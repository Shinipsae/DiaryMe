import tkinter
import Main
import pymysql
import Admin
import tkinter.font as tkFont
import Edit
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

        fontStyle = tkFont.Font(family="궁서체", size=20)
        lbl = tkinter.Label(frame1, text="질문목록", font=fontStyle)
        lbl.pack(side=TOP, pady=10)

        lblButton = Button(frame1, text='질문등록하기', command=onClick_insert)
        lblButton.pack(side=RIGHT, padx = 50)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        # 표
        treeview = tkinter.ttk.Treeview(frame2, columns=["one"],
                                        displaycolumns=["one"],
                                        height=100) # height default=10

        vsb = tkinter.ttk.Scrollbar(frame2, orient="vertical",
                                command=treeview.yview)
        vsb.pack(side='right', fill=Y)

        treeview.configure(yscrollcommand=vsb.set)

        treeview.column("#0", width=50, anchor="w")
        treeview.heading("#0", text="번호", anchor="center")

        treeview.column("#1", width=360, anchor="center")
        treeview.heading("one", text="질문", anchor="center")

        question_list = ["-"] * 100

        cursor = conn.cursor()
        sql = f"select max(id) from question"
        cursor.execute(sql)
        number = cursor.fetchone()[0]

        for i in range(1, number + 1):
            cursor1 = conn.cursor()

            sql1 = f"select question from diaryme.question where id = '{i}'"

            cursor1.execute(sql1)

            question_list[i - 1] = cursor1.fetchone()

        # 리스트에 tuple을 초기화 이후에 어떻게 더하는지 몰라서...
        treelist = [("-"),
                    (question_list[0]),
                    (question_list[1]),
                    (question_list[2]),
                    (question_list[3]),
                    (question_list[4]),
                    (question_list[5]),
                    (question_list[6]),
                    (question_list[7]),
                    (question_list[8]),
                    (question_list[9]),

                    (question_list[10]),
                    (question_list[11]),
                    (question_list[12]),
                    (question_list[13]),
                    (question_list[14]),
                    (question_list[15]),
                    (question_list[16]),
                    (question_list[17]),
                    (question_list[18]),
                    (question_list[19]),

                    (question_list[20]),
                    (question_list[21]),
                    (question_list[22]),
                    (question_list[23]),
                    (question_list[24]),
                    (question_list[25]),
                    (question_list[26]),
                    (question_list[27]),
                    (question_list[28]),
                    (question_list[29]),

                    (question_list[30]),
                    (question_list[31]),
                    (question_list[32]),
                    (question_list[33]),
                    (question_list[34]),
                    (question_list[35]),
                    (question_list[36]),
                    (question_list[37]),
                    (question_list[38]),
                    (question_list[39]),

                    (question_list[40]),
                    (question_list[41]),
                    (question_list[42]),
                    (question_list[43]),
                    (question_list[44]),
                    (question_list[45]),
                    (question_list[46]),
                    (question_list[47]),
                    (question_list[48]),
                    (question_list[49]),

                    (question_list[50]),
                    (question_list[51]),
                    (question_list[52]),
                    (question_list[53]),
                    (question_list[54]),
                    (question_list[55]),
                    (question_list[56]),
                    (question_list[57]),
                    (question_list[58]),
                    (question_list[59]),

                    (question_list[60]),
                    (question_list[61]),
                    (question_list[62]),
                    (question_list[63]),
                    (question_list[64]),
                    (question_list[65]),
                    (question_list[66]),
                    (question_list[67]),
                    (question_list[68]),
                    (question_list[69]),

                    (question_list[70]),
                    (question_list[71]),
                    (question_list[72]),
                    (question_list[73]),
                    (question_list[74]),
                    (question_list[75]),
                    (question_list[76]),
                    (question_list[77]),
                    (question_list[78]),
                    (question_list[79]),

                    (question_list[80]),
                    (question_list[81]),
                    (question_list[82]),
                    (question_list[83]),
                    (question_list[84]),
                    (question_list[85]),
                    (question_list[86]),
                    (question_list[87]),
                    (question_list[88]),
                    (question_list[89]),

                    (question_list[90]),
                    (question_list[91]),
                    (question_list[92]),
                    (question_list[93]),
                    (question_list[94]),
                    (question_list[95]),
                    (question_list[96]),
                    (question_list[97]),
                    (question_list[98]),
                    (question_list[99])]

        for i in range(1, len(treelist)):
            treeview.insert('', 'end', text=i,
                            values=treelist[i], iid=str(i) + "번")

        treeview.pack(pady=30)

        conn.close()

def main():

    root = Tk()
    root.geometry("500x500+300+300")
    root.resizable(False, False)
    app = ShowList(root)
    root.mainloop()

def onClick_insert():
    Admin.main()

def onClick_main():
    Main.main()

if __name__ == '__main__':
    main()