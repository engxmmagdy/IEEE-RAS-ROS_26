
class Book:
    def __init__(self, auther, title):
        self.auther = auther
        self.title = title
        self.is_available = True
        
    def borrow_book(self):
        if self.is_available:
            print("Sure")
            self.is_available = False
        else:
            print("already out")

novel = Book("Orwell", "1984")
novel.borrow_book()
novel.borrow_book()
novel.borrow_book()