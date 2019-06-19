from googlesearch import GoogleSearch
import files
from pdfDownloading import *
import threading
import io


class Spider:

    def __init__(self, search):
        self.search = search
        self.pdfs = list()
        self.size_list = list()
        self.threads_list = list()
        files.create_search_folder(self.search)
        files.clear_file_data(self.search + "/PDFs.txt")

    def gather_pdfs(self):
        google = GoogleSearch()
        google.query(self.search)
        google.get_results()
        self.pdfs = google.get_pdfs()
        print(self.pdfs)

        count = 0
        for pdf in self.pdfs:
            if count == 10:
                break

            files.append_data(pdf, self.search + "/PDFs.txt")
            count += 1

    def work(self, pdf_link):
        #with io.BytesIO(pdfDownloading.download_file(pdf_link).content) as response:
            #self.size_list.append(pdfDownloading.get_number_of_lines(response))
        for link in pdf_link:
            with io.BytesIO(download_file(link).content) as response:
                self.size_list.append(get_number_of_lines(response))
        print(self.size_list)
        print(self.pdfs)

    def sort_pdfs(self):
        # pdf_links = files.file_to_list(self.search + "/PDFs.txt")

        self.work(self.pdfs)
    

        self.size_list, self.pdfs = (list(t) for t in zip(*sorted(zip(self.size_list, self.pdfs))))
        self.size_list.reverse()
        self.pdfs.reverse()

        print(self.pdfs)
        print(self.size_list)
