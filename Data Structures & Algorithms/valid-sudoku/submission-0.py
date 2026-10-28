class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # One set per row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                digit = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)

                # Check all three constraints at once
                if (digit in rows[r] or
                    digit in cols[c] or
                    digit in boxes[box_idx]):
                    return False

                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_idx].add(digit)

        return True