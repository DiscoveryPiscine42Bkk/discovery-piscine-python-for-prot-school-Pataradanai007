#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) != 2:
    print("none")
else:
    # รับสตริงที่ส่งมาเป็นพารามิเตอร์
    input_string = sys.argv[1]
    
    # แปลงข้อความทั้งหมดเป็นตัวพิมพ์เล็ก (เพื่อให้รองรับทั้ง 'z' และ 'Z')
    input_string = input_string.lower()
    
    # ค้นหาตัวอักษร 'z' ในสตริง
    if 'z' in input_string:
        # แสดง 'z' สำหรับแต่ละการเกิดขึ้นของ 'z'
        print('z' * input_string.count('z'))
    else:
        print("none")
