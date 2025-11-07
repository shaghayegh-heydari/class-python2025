class Food :
    def __init__(self, color , taste ,type) :
        self.color = color
        self.taste = taste
        self.type = type

    def info (self):
        print (f"my food is {self.type}  it is {self.taste} and {self.color}")

if __name__=="__main__" :
    food1 = Food ("dark brown","sour","fesengan") 

    food1.info()