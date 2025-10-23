def area (length,width):
    return length * width

def perimeter (length,width):
    return 2 * (length + width)

length = float(input("tuol mostatil ra vared conid :"))
width = float(input("arz mostatil ra vared conid :"))
choice = input("aya mihkid mohit ia masahat ra hesab conid ?").strip()

if choice == "mohit" :
    result = perimeter(length,width)
    print("mohit va masahat =",result)

elif choice == "masahat" :
    result = area(length,width)
    print("masahat mostatil =", result)

else :
    print("nemitavanid vared shavid ! lotfan faghat mohit va masahat ra vared knid")