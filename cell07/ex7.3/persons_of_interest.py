def famous_births(historical_figures):
    # เรียงลำดับพจนานุกรมโดยใช้ค่าในคีย์ 'date_of_birth'
    sorted_figures = sorted(historical_figures.items(), key=lambda x: x[1]['date_of_birth'])
    
    # แสดงผลแต่ละรายการในรายการที่เรียงลำดับแล้ว
    for _, figure in sorted_figures:
        print(f"{figure['name']} เป็นนักวิทยาศาสตร์ที่ยิ่งใหญ่ที่เกิดในปี {figure['date_of_birth']}.")

# ตัวอย่างพจนานุกรมของนักวิทยาศาสตร์หญิง
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# เรียกใช้ฟังก์ชัน famous_births กับพจนานุกรม women_scientists
famous_births(women_scientists)
