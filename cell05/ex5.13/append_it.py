#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) == 1:
    print("none")
else:
    # วนลูปผ่านพารามิเตอร์ที่ส่งเข้ามา
    for param in sys.argv[1:]:
        # ถ้าพารามิเตอร์ไม่ลงท้ายด้วย 'ism' ให้เพิ่ม 'ism' ต่อท้ายและแสดง
        if not param.endswith("ism"):
            print(param + "ism")
