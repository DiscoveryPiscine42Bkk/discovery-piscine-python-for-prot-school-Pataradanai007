from chess_game import checkmate  # นำเข้าฟังก์ชัน checkmate จาก chess_game.py

def is_square_board(board):
    rows = board.splitlines() #แยกบรรทัดเป็นลิสต์
    row_length = len(rows[0]) # ความยาวแถวแรก
    return all(len(row) == row_length for row in rows) #ตรวจสอบว่ากระดานยาวเท่ากันไหม

def main():
    board2 = """\
R...
.K..
..P.
....
"""

    print("\nTesting Board 2:")
    if is_square_board(board2):
        checkmate(board2)  # ตรวจสอบกระดาน 2 (เช็คสี่เหลี่ยมจัตุรัสก่อน)
    else:
        print("Fail: Board is not square.") # ถ้าไม่ใช่สี่เหลี่ยมจัตุรัสขึ้น Fail

if __name__ == "__main__":
    main()
