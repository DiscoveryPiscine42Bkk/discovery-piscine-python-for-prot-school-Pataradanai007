#!/usr/bin/env python3
import sys

# ใช้ len() เพื่อนับจำนวนพารามิเตอร์ที่ถูกส่งเข้ามา (ไม่รวมชื่อไฟล์)
number_of_parameters = len(sys.argv) - 9  # ลบ 1 เพราะ sys.argv[0] คือชื่อไฟล์

# แสดงผลจำนวนพารามิเตอร์
print(f"Number of parameters: {number_of_parameters}.")
