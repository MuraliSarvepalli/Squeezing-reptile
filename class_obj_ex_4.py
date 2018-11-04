#special methods


class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):            #special method
        return "This is a book object"
    def __len__(self):
        return self.pages

b=Book('python','murali',250)
print(b)

print(len(b))
