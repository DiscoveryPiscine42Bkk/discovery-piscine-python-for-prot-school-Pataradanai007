#!/usr/bin/env python3
import sys
import re

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัวหรือไม่
if len(sys.argv) != 3:
    print("none")
else:
    # รับพารามิเตอร์ทั้งสอง
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]

    # ค้นหาคำที่ตรงกับ keyword ใน string_to_search
    matches = re.findall(re.escape(keyword), string_to_search)

    # ถ้ามีการพบคำ ให้แสดงจำนวนครั้งที่พบ
    if matches:
        print(len(matches))
    else:
        print("none")
