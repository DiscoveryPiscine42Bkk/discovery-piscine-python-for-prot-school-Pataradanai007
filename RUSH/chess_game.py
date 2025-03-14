def checkmate(board):  
    rows = board.split() #แยกบรรทัดของกระดานเป็นลิสต์
    # print(rows)
    # หาตำแหน่งของราชาโดยใช้ while loop
    i = 0                 #ใช้ตัวแปร i ไล่ดูแต่ละแถว while loop
    j = 0
    king_position = None
    king_Big = 0
    while i < len(rows):
        j=0
        while j < len(rows[i]):
             #if 'K' in rows[i]: 
            #king_position = (i, rows[i].index('K'))
            # print(rows[i][j])
            if rows[i][j] == 'K': # ถ้าเจอ K ในแถวนั้น ให้บันทึกต่ำแหน่ง
       
                king_position = [i, j]
                king_Big += 1
            j+=1

        i += 1
    
    if king_Big > 1 :
        print("Error : King > 1")
        return

    if not king_position:
        print("Error: King not found.") #ถ้าไม่พบ K ให้ขึ้น King not found
        return

    x, y = king_position  # ตำแหน่งของราชา

    # ฟังก์ชันตรวจสอบการโจมตี ของ เรือ บิชอป ราชินี
    def check_direction(dx, dy, pieces): #ตรวจสอบไปตามแนว x,y
        i, j = x + dx, y + dy 
        while 0 <= i < len(rows) and 0 <= j < len(rows[0]):
            if rows[i][j] in pieces:
                return True
            if rows[i][j] != '.':
                break
            i, j = i + dx, j + dy
        return False

    # ตรวจสอบเบี้ย
    if x + 1 < len(rows) and ((y - 1 >= 0 and rows[x + 1][y - 1] == 'P') or (y + 1 < len(rows[0]) and rows[x + 1][y + 1] == 'P')):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากเรือ (R), ราชินี (Q) แนวตรงและแนวนอน
    if any(check_direction(dx, dy, {'R', 'Q'}) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากบิชอป (B), ราชินี (Q) แนวทแยง
    if any(check_direction(dx, dy, {'B', 'Q'}) for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]):
        print("Success")
        return  

    print("Fail")
