class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # ذخیره اعداد هر ستون
        rows = collections.defaultdict(set) # ذخیره اعداد هر سطر
        squares = collections.defaultdict(set) # key = (r/3, c/3) # ذخیره اعداد هر مربع ۳×۳

        for r in range(9):
            for c in range(9):
                #تمام خانه‌های تخته ۹×۹ را بررسی می‌کند.
                if board[r][c] == ".":
                    #نادیده گرفتن خانه‌های خالی
                    continue
                if (board[r][c] in rows[r] or # آیا در همین سطر قبلاً دیده‌ایم؟
                    board[r][c] in cols[c] or # آیا در همین ستون قبلاً دیده‌ایم؟
                    board[r][c] in squares[( r // 3) , c //3]): # آیا در همین مربع ۳×۳ قبلاً دیده‌ایم؟
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c//3)].add(board[r][c]) #اضافه کردن به مجموعه‌ها
        return True