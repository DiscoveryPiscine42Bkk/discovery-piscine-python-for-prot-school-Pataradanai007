def a(input_string):
    if len(input_string) < 1:  # ถ้าสตริงว่างหรือมีความยาวน้อยกว่า 1
        return "none"  # คืนค่า "none"
    
    return "hello"  # ถ้ามีสตริงที่มีความยาวมากกว่าหรือเท่ากับ 1 ให้แสดง "hello"

# การทดสอบฟังก์ชัน
print(a("Hello"))  # ควรแสดงผลเป็น "hello"
  # ควรแสดงผลเป็น "none"
