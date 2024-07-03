import pandas as pd
import numpy as np


class BookLover:
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})



    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        num_books = 0
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self, book_name, book_rating):
        if book_name not in self.book_list["book_name"].values:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books +=1
        else:
            print("Book is already in book list")

    def has_read(self, book_name):
        return book_name in self.book_list["book_name"].values

    
    def num_books_read(self):
        print(self.num_books)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]


if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()



    # And so forth