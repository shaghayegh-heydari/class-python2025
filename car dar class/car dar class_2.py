class Book :
    def __init__(self , title , author ,pages) :
        self.title = title
        self.author = author
        self.pages = pages

    def info (self) :
        print(f"nevisndh {self.author} , onvan {self.title} , pages {self.pages}")

if __name__=="__main__" :
    p1 = Book("gnayat va mocafat","dasta ufsci",400)
    
    p1.info()