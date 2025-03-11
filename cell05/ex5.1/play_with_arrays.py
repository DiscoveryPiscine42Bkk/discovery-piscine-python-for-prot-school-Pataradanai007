#!/usr/bin/env python3

# กำหนดอาเรย์เดิม
original_array = [8, 45, 8, 10, 20, 22, -14, 7]

# สร้างอาเรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละค่าในอาเรย์เดิม
new_array = [x + 2 for x in original_array]

# แสดงผลทั้งสองอาเรย์
print("Original array:", original_array)
print("New array:", new_array)
