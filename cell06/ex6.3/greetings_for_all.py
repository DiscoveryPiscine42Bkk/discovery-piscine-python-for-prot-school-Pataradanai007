#!/usr/bin/env python3

# การกำหนดฟังก์ชัน greetings
def greetings(name="noble stranger"):
    if isinstance(name, str):  # ตรวจสอบว่าเป็นสตริงหรือไม่
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# ทดสอบการเรียกฟังก์ชัน
greetings('Pataradanai')
greetings('Thongngoen')
greetings()
greetings(17)
