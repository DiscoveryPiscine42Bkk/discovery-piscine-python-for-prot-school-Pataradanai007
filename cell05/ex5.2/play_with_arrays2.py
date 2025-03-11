#!/usr/bin/env python3

# กำหนดอาเรย์เดิม
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาเรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละค่าในอาเรย์เดิมที่มากกว่า 5
new_array = [x + 2 for x in original_array if x > 5]

# แสดงผลทั้งสองอาเรย์
print(original_array)
print(new_array)
