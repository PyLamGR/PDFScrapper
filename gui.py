from tkinter import *
from spider import Spider
import webbrowser

"""
Note: print all PDFs as hyperlinks after the app is done

import webbrowser

def callback(event):
    webbrowser.open_new(r"http://www.google.com")

root = Tk()
link = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()

OR

from tkinter import *
import webbrowser

root = Tk()
link = Label(root, text="http://stackoverflow.com", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))
root.mainloop()
"""


def run():

    root = Tk()
    root.title("PDF-Scrapper")
    root.geometry("800x300")    # original: 300x100

    # methods
    def search():
        data = str(search_data.get())
        spider = Spider(data)
        spider.gather_pdfs()
        # spider.sort_pdfs()

        notification_label = Label(root, text="You Can Copy the Links")
        notification_label.grid(row=3)

        pdf_text = Text(root, fg="blue")

        for pdf in spider.pdfs:
            pdf_text.insert(END, '- ' + pdf + '\n\n')

        pdf_text.grid(row=4)

    # entries
    search_data = StringVar()

    search_entry = Entry(root, textvariable=search_data)

    # labels
    search_label = Label(root, text='Enter the PDF you want to search here')

    # buttons
    search_button = Button(root, text="Search", command=search)

    # grid layout
    search_label.grid(row=0, column=0)
    search_entry.grid(row=1, column=0)
    search_button.grid(row=1, column=1)

    root.mainloop()


if __name__ == '__main__':
    run()
