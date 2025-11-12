import csv

name_file = "library_book.csv"

def add_book():
    title = input("onvan ktab :")
    author = input("navisnde :")
    year = input("sale entashar :")
    with open(name_file , "a" , newline="" , encoding="utf-8") as f :
        writer = csv.writer(f)
        writer.writerow([title , author , year])
print(f"ketab azafe shod")

def show_books():
    try:
        with open(name_file , "r" , encoding="utf-8") as f :
            reader = csv.reader(f)
            print(f"\n list ktab ha:")
            for row in reader :
                print(f"onvan : {row[0]} , navisnde : {row[1]} , sale : {row[2]}") 
    except FileNotFoundError :
        print(f"ktabi sabt nashode")

def find_book():
    search_title = input("name ktabi kh mikhanid :")
    found = False
    try:
        with open(name_file , "r" , encoding="utf-8") as f :
            reader = csv.reader(f)
            for row in reader :
                if row[0].strip().lower() == search_title.strip().lower():
                    found = True
                    break

        if found:
            print(f"in ktabe dar ktabkhane ast")
        else:
            print(f"in ktabe peydanashod")
    except FileNotFoundError :
        print(f"ktabe hanoz sabt nashode")

def main():
    while True :
        print(f"\n entakhab con :")
        print(f"1.ezafe cardan ktabha")
        print(f"2.didan hame ktabha")
        print(f"3.peyda cardan ktabha")
        print(f"4.khorug")

    choice = input("shomare kozinh: ")
    if choice == "1":
        add_book()
    elif choice == "2" :
        show_books()
    elif choice == "3" :
        find_book()
    elif choice =="4" :
        print("khodafez")
        break
    else :
        print(f"gozine namoetabar")

main()