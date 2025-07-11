'''
sort the input by the published year

we can do this by having a key file that returns
the intger of the string for "published"

we then do sorted(key=published_function)
'''
def publish_function(string):
    return int(string["published"])



books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

sorted_books = sorted(books, key=publish_function)
print(sorted_books)