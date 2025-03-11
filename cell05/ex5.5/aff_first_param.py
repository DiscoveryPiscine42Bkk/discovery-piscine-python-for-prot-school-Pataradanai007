#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) < 2:  # ถ้ามีพารามิเตอร์น้อยกว่า 2 (แปลว่าไม่มีพารามิเตอร์)
    print("none")
else:
    # แสดงพารามิเตอร์แรก
    print(sys.argv[])
