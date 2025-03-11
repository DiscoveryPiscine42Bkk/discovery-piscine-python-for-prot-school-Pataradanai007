#!/usr/bin/env python3

# กำหนดอาเรย์เดิม
original_array = [2, 10, 9, 26, 8, 9, -52, 10]

# สร้างอาเรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละค่าในอาเรย์เดิมที่มากกว่า 5
new_array = {x + 2 for x in original_array if x > 5}  # ใช้ set comprehension เพื่อกำจัดค่าซ้ำ

# แสดงผลทั้งสองอาเรย์
print(original_array)
print(new_array)
