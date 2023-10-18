class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def displayinfo(self):
        print("title =",self.title)
        print("author = ",self.author)
        print("price = ",self.price)
b1=book("yes","me","1000")
b2=book("bye","you","999")
b1.displayinfo()
b2.displayinfo()