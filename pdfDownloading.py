import io
import PyPDF2
import requests
import time


s = requests.Session()

PDF_LINKS = ["http://file.allitebooks.com/20181202/Amazon%20Web%20Services%20in%20Action,%202nd%20Edition.pdf","http://file.allitebooks.com/20190212/Android%203.0%20Application%20Development%20Cookbook.pdf","http://file.allitebooks.com/20190222/PostGIS%20Cookbook.pdf","http://file.allitebooks.com/20190222/Beginning%20REALbasic.pdf","http://file.allitebooks.com/20190222/DNS%20in%20Action.pdf"]
PDF_NAMES = ["Amazon Web Services in Action, 2nd Edition","Another name","PostGIS Cookbook","Beginning REALbasic","DNS in Action"]


NAME_LIST = []  # names of the pdfs
SIZE_LIST = []  # size of words inside pdf


def download_file(pdf_link):
    print("request time")
    start = time.time()
    req = s.get(pdf_link)

    end = time.time()
    print(end - start)
    return req


def get_number_of_lines(pdf_info):
    # This function takes as input a pdf and returns the number of lines found in that pdf
    number_of_lines = 0
    # cProfile.run('re.compile("get_number_of_lines|pdg_info")')
    print("time to open pdf")
    start = time.time()
    pdf_info = PyPDF2.PdfFileReader(pdf_info)
    end = time.time()
    print(end-start)
    print("time to execute tast")
    start = time.time()
    for page in range(pdf_info.getNumPages()):
        file_info = pdf_info.getPage(page)
        content = file_info.extractText()
        count_escape_char = content.count('\n')
        number_of_lines = number_of_lines + count_escape_char
    end = time.time()
    print(end - start)

    return number_of_lines

"""
if __name__ == '__main__':
    print("App starts")
    app_start = time.time()
    index = 0
    for link in PDF_LINKS:
        with io.BytesIO(download_file(link).content) as response:
            SIZE_LIST.append(get_number_of_lines(response))
            NAME_LIST.append(PDF_NAMES[index])
            index += 1
    print(SIZE_LIST)
    print(NAME_LIST)

    SIZE_LIST, NAME_LIST = (list(t) for t in zip(*sorted(zip(SIZE_LIST, NAME_LIST))))
    SIZE_LIST.reverse()
    NAME_LIST.reverse()
    print(SIZE_LIST)
    print(NAME_LIST)

    end = time.time()
    print("app ends")
    app_end = time.time()
    print(app_end-app_start)
    print(SIZE_LIST)
"""