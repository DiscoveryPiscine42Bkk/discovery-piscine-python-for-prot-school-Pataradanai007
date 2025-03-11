#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) != 2:  # ถ้าจำนวนพารามิเตอร์ไม่เท่ากับ 1
    print("none")
else:
    # แสดงพารามิเตอร์ในรูปแบบตัวพิมพ์เล็ก
    print(sys.argv[1].lower())
