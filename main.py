from spider import Spider

search = str(input("Search> "))

spider = Spider(search)
spider.gather_pdfs()
spider.sort_pdfs()
