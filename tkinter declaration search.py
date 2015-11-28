import re
import webbrowser
import Tkinter as Tk

final_results = [(u"yahoo", "https://tw.yahoo.com/"), (u"google",
                                              "http://www.google.com.tw/"), (u"youtube", "https://www.youtube.com/")]

#final_results = [(u"中文字", "「中文字的內容」"), (u"中文符號", "「中文符號的內容」"), (u"中文標點", "「中文標點的內容」")]


class App(object):

    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Declaration Search")
        self.root.geometry("600x400")
        self.root.bind('<Return>', self.search)  # 按enter執行

        # space to read more comfortable
        self.label = Tk.Label(self.root, text="   ")
        self.label.pack()

        self.label = Tk.Label(
            self.root, text="Enter the word you want search.", font=("Helvetica", 14))
        self.label.pack()

        self.var = Tk.StringVar()
        Tk.Entry(self.root, textvariable=self.var).pack()

        self.button = Tk.Button(self.root, text="submit",
                                command=self.search, font=("Helvetica", 10))
        self.button.pack()

        # space to read more comfortable
        self.label = Tk.Label(self.root, text="   ")
        self.label.pack()

        self.root.mainloop()

    def openlink(self, event, link):
        webbrowser.open_new("{}".format(link))

    def search(self, *args):
        keyword = self.var.get()

        if not keyword:  # if nothing input
            pass

        else:
            trans_keyword = keyword.encode('utf-8')

            for item in final_results:
                declaration = item[0].encode('utf-8')

                if re.search(r'{}'.format(trans_keyword), declaration, re.I):

                    Title = Tk.Label(text=item[0], foreground="blue")
                    link = item[1]
                    Title.pack()
                    Title.bind("<Button-1>", lambda event,
                               arg=link: self.openlink(event, arg))

App()
