from googlesearch import GoogleSearch
import files
import pdfDownloading
import threading
import io


THREADS_NUM = 10


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

        count = 0
        for pdf in self.pdfs:
            if count == 10:
                break

            files.append_data(pdf, self.search + "/PDFs.txt")
            count += 1

    def work(self, pdf_link):
        with io.BytesIO(pdfDownloading.download_file(pdf_link).content) as response:
            self.size_list.append(pdfDownloading.get_number_of_lines(response))

    def sort_pdfs(self):
        pdf_links = files.file_to_list(self.search + "/PDFs.txt")

        # threads go here
        for i in range(0, THREADS_NUM):
            self.threads_list.append(threading.Thread(target=self.work, args=(pdf_links[i],)))

        for thread in self.threads_list:
            thread.daemon = True
            thread.start()
        """
        for pdf in pdf_links:
            self.work(pdf)
        """

        self.size_list, self.pdfs = (list(t) for t in zip(*sorted(zip(self.size_list, self.pdfs))))
        self.size_list.reverse()
        self.pdfs.reverse()

        print(self.pdfs)
        print(self.size_list)
