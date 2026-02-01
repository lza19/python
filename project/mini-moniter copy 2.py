
def types():
    print("1 : gmaing")
    print("2 : Work & Office")
    print("3 : Graphic & Design")
    print("Q : Quit")
    n2 = input("เลือก ประเภทของจอ (1-3): ") #str
    return n2

Store = {
    "Samsung": {
        "Gaming Monitor": {
            "MONITOR ดูทั้งหมด": [1001, 1002, 1003],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
    },
        "Office or Working Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        },
        "Professional or Graphic Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        }
    },
    "Dell": {
            "Gaming Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
    },
        "Office or Working Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        },
        "Professional or Graphic Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        }
    },
    "LG": {
                "Gaming Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
    },
        "Office or Working Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        },
        "Professional or Graphic Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        }
    },
    "ASUS": {
            "Gaming Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
    },
        "Office or Working Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        },
        "Professional or Graphic Monitor": {
            "MONITOR ดูทั้งหมด": [],
            "ขนาด 15'' - 19.5''": [],
            "ขนาด 21.5'' - 22''": [],
            "ขนาด 23'' - 25''": [],
            "ขนาด 34'' - 40''": []
        }
    }
}

def sizes():
    print("1 : MONITOR ดูทั้งหมด")
    print("2 : MONITOR 15'' - 19.5''")
    print("3 : MONITOR 21.5'' - 22''")
    print("4 : MONITOR 23'' - 25''")
    print("5 : MONITOR 34'' - 40''")
    print("Q : Quit")
    n3 = input("เลือก ขนาดของจอ (1-5): ") #str
    return n3

n1 = ""
n2 = ""
n3 = ""

brand = ""
type_monitor = ""
size = ""

while True:
    print("--- CS monitor hub---")
    print("Welcome to the CS monitor hub!")
    print("---- Brand ----")
    print("1 : Samsung")
    print("2 : Dell")
    print("3 : LG")
    print("4 : ASUS")
    print("Q : Quit")       
    n1 = input("เลือก แบรนด์สินค้า (1-4): ") #str

    if n1 == "1":
        brand = "Samsung"
        break
    elif n1 == "2":
        brand = "Dell"
        break
    elif n1 == "3":
        brand = "LG"
        break
    elif n1 == "4":
        brand = "ASUS"
        break
    elif n1 == "Q":
        print("Exiting Goodbye!")
        break
    else:
        print("\n\n\n")
        print("ใส่ค่าผิด กรุณาใส่ใหม่")

print("\n\n\n\n")
if n1 != "Q":
    while True:
        print(f"สินค้าที่เลือก : {brand}")
        print("--- ประเภทของจอ ---")
        n2 = types()
        if n2 == "1":
            type_monitor = "Gaming Monitor"
            break
        elif n2 == "2":
            type_monitor = "Office or Working Monitor"
            break
        elif n2 == "3":
            type_monitor = "Professional or Graphic Monitor"
            break
        elif n2 == "Q":
            print("Exiting Goodbye!")
            break
        else:
            print("\n\n\n\nใส่ค่าผิด กรุณาใส่ใหม่")

print("\n\n\n\n")

if n2 != "Q":
    while True:
        print(f"สินค้าที่เลือก : {brand} / {type_monitor}")
        n3 = sizes()
        if n3 == "1":
            size = "MONITOR ดูทั้งหมด"
            break
        elif n3 == "2":
            size = "ขนาด 15'' - 19.5''"
            break
        elif n3 == "3":
            size = "ขนาด 21.5'' - 22''"
            break
        elif n3 == "4":
            size = "ขนาด 23'' - 25''"
            break
        elif n3 == "5":
            size = "ขนาด 34'' - 40''"
            break
        elif n3 == "Q":
            print("Exiting Goodbye!")
            break
        else:
            print("\n\n\n\nใส่ค่าผิด กรุณาใส่ใหม่")
 

if n3 != "Q":
    print("\n\n\n\n")
    print(f"สินค้าที่เลือก : {brand} / {type_monitor} / {size}")
    if brand == "Samsung" and type_monitor == "Gaming Monitor" and size == "MONITOR ดูทั้งหมด":
        pass
    elif brand == "Samsung" and type_monitor == "Gaming Monitor" and size == "ขนาด 15'' - 19.5''":
        pass
    elif brand == "Samsung" and type_monitor == "Gaming Monitor" and size == "ขนาด 21.5'' - 22''":
        pass
    elif brand == "Samsung" and type_monitor == "Gaming Monitor" and size == "ขนาด 23'' - 25''":
        pass
    elif brand == "Samsung" and type_monitor == "Gaming Monitor" and size == "ขนาด 34'' - 40''":
        pass

#print(brand)
#print(type(n1))
#print(n1)