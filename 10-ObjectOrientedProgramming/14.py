class Ebook():
    def __init__(self):
        self.is_opened=False
        self.title='Wiedzmin'
        self.author='Sapkowski'
        self.numbers_of_pages=271
        self.current_page=0

    def open(self):
        self.is_opened=True

    def close(self):
        self.is_opened=False
        
    def read(self,read_pages):
        if self.is_opened==True:
            self.current_page+=read_pages
        else:
            print("Book is closed, cant read")

    def status(self):
        if self.is_opened==True:
            print(f'The book is opened on the page: {self.current_page}')
        else:
            print(f'Book is closed. You were on page: {self.current_page}')



book1=Ebook()
book1.open()
book1.read(5)
book1.status()
book1.close()
book1.status()
book1.read(10)
book1.status()