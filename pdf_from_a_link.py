import requests
import PyPDF2
import io
import time
import cProfile
import re



PDF_LINKS = ["http://file.allitebooks.com/20181202/Amazon%20Web%20Services%20in%20Action,%202nd%20Edition.pdf","http://file.allitebooks.com/20190212/Android%203.0%20Application%20Development%20Cookbook.pdf"]
PDF_NAMES = ["Amazon Web Services in Action, 2nd Edition"]





def get_number_of_lines(pdf_info):
    # This function takes as input a pdf and returns the number of lines found in that pdf
    number_of_lines = 0
    #cProfile.run('re.compile("get_number_of_lines|pdg_info")')
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

# This is just for testing
#dissabling proxy
# we probably need  from multiprocessing import Pool
app_start = time.time()
start = time.time()
for link in PDF_LINKS:

    # Request the file
    print("request time")
    start = time.time()
    req = requests.get(link)
    end = time.time()
    print(end - start)

    # Open the file
    print("time to open pdf with byteIO")
    start = start = time.time()
    with io.BytesIO(req.content) as open_pdf:
        end = time.time()
        print(end - start)
        print(get_number_of_lines(open_pdf))

    print("all the app time")
    print(time.time() - app_start)

