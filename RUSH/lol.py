from chess_game import checkmate  # นำเข้าฟังก์ชัน checkmate จาก checkmate.py

def is_square_board(board):
    rows = board.splitlines()
    row_length = len(rows[0])
    return all(len(row) == row_length for row in rows)

def main():
    board2 = """\
R...
.K..
.PP.
....
"""

    print("\nTesting Board 2:")
    if is_square_board(board2):
        checkmate(board2)  # ตรวจสอบกระดาน 2 (เช็คสี่เหลี่ยมจัตุรัสก่อน)
    else:
        print("Fail: Board is not square.")

if __name__ == "__main__":
    main()
