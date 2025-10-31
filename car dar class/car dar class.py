class student :
    def __init__(self , name , grade) :
        self.name = name
        self.grade = grade

    def show_info (self):
        print(f"{self.name} is {self.grade}")


if __name__=="__main__":
    p1= student("nima",12)

    p1.show_info()
        
