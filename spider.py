from googlesearch import GoogleSearch
import files


class Spider:

    def __init__(self, search):
        self.search = search
        self.pdfs = list()
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
