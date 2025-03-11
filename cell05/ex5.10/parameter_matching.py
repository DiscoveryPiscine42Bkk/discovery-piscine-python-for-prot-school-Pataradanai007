#!/usr/bin/env python3

import sys

# ตรวจสอบจำนวนพารามิเตอร์ที่ส่งมา
if len(sys.argv) != 2:
    print("none")
else:
    # รับพารามิเตอร์ที่ส่งมา
    param = sys.argv[1]
    
    # ขอให้ผู้ใช้กรอกคำ
    user_input = input("What was the parameter? ")

    # เปรียบเทียบคำที่ผู้ใช้กรอกกับพารามิเตอร์ที่ส่งมา
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
