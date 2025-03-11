#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์มากกว่าหรือเท่ากับ 2 ตัว
if len(sys.argv) < 2:
    print("none")
else:
    # ใช้ reversed() หรือการสลับลำดับรายการ แล้วแสดงผล
    for param in reversed(sys.argv[1:]):
        print(param)
