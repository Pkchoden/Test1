# initialize empty list, set and dictonary
book_list= []
author_set= set()
books_dict = {}
# add books
book_list.append('Python Programming')
author_set.add('John Smith')
books_dict['Python Programming']= 'John Smith'

book_list.append('Data Structure and Algorithms')
author_set.add("Jane Doe")
books_dict['Data Structure and Algorithms']= 'Jane Doe'

book_list.append("Machine learning basics")
author_set.add('Alice Johnson')
books_dict['Machine learning basics']= 'Alice Johnson'

#search for a book
search_title = input('Enter the title of the book to search:')
if search_title in book_list:
    print(f'Book found! Author: {books_dict[search_title]}')
else:
    print('Book not found!')

# display all books
print('list of books:')
for book in book_list:
    print(book)  

# remove a book
remove_title= input('Enter the name of the book to remove:')
if remove_title in book_list:
    remove_author = books_dict[remove_title]   
    book_list.remove(remove_title)
    author_set.remove(remove_author)
    del books_dict[remove_title] 
    print('book removed successfully!')
    print('books available:', book_list)  
else:
    print('book not found!')

