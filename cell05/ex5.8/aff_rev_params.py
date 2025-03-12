import sys

# ตรวจสอบว่ามีพารามิเตอร์มากกว่าหรือเท่ากับ 2 ตัว
if len(sys.argv) < 2:
    print("none")
else:
    i = len(sys.argv) - 1  # เริ่มจากตัวสุดท้าย
    while i > 0:  # หยุดเมื่อถึง sys.argv[0] (ชื่อไฟล์)
        print(sys.argv[i])
        i -= 1  # ลดค่า i เพื่อเลื่อนย้อนกลับ
