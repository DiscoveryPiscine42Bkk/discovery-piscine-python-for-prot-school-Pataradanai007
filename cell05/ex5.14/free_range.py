#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัว
if len(sys.argv) != 3:
    print("none")
else:
    # แปลงพารามิเตอร์ให้เป็นตัวเลข
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # สร้างอาเรย์จากช่วงตัวเลขระหว่าง num1 และ num2 (รวม num2 ด้วย)
    result = list(range(num1, num2 + 1))

    # แสดงอาเรย์
    print(result)
