import numpy as np
import pandas as pd
import unittest 
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("er",4.0)
        assert 'er' in test_object.book_list["book_name"].values


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object1.add_book("er", 4.0)
        test_object1.add_book("er", 4.0)
        assert test_object1.book_list["book_name"].value_counts()['er'] == 1
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object3.add_book("er", 4.0)
        testValue = test_object3.has_read("er")
        message = "Test value works."
        self.assertTrue(testValue, message)

        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object4.add_book("er", 4.0)
        testValue = test_object4.has_read("long")
        message = "Test value is not false."
        self.assertFalse( testValue, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object5.add_book("er", 4.0)
        test_object5.add_book("yu", 1.0)
        test_object5.add_book("po", 4.1)
        test_object5.add_book("goo", 3.0)
        assert test_object5.num_books_read() == 4


    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object6 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object6.add_book("er", 4.0)
        test_object6.add_book("yu", 1.0)
        test_object6.add_book("po", 4.1)
        test_object6.add_book("goo", 3.0)
        fav_books_df = test_object6.fav_books()
        assert all(fav_books_df['book_rating'] > 3)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)