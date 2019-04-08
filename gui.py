from tkinter import *
from spider import Spider



def run():

    root = Tk()
    root.title("PDF-Scrapper")
    root.geometry("300x100")

    # methods
    def search():
        data = str(search_data.get())
        print(data)
        spider = Spider(data)
        spider.gather_pdfs()
        spider.sort_pdfs()

        notification_label = Label(root, text="Check The Program's Folder for the PDFs!")
        notification_label.grid(row=3)

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
