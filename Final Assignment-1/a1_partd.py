#    Main Author(s): Avreet Kaur
#    Main Reviewer(s):

from a1_partc import Queue

def get_overflow_list(grid):
    def is_overflow(row, col, cell, r, c):
        if (row ==0 and col==0 )or (row ==0 and col==c-1) or (row ==r-1 and col==0) or (row ==r-1 and col==c-1):
            return abs(cell) >1
        elif row==0 or col==0 or row==r-1 or col==c-1:
            return abs(cell) >2
        else:
            return abs(cell)>3

    overflow_list = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if is_overflow(r, c, grid[r][c], len(grid), len(grid[0])):
                overflow_list.append((r, c))

    # print(overflow_list)
    return overflow_list if len(overflow_list)!=0 else None

def overflow(grid, a_queue):
    def spread_overflow(row, col, isNegative):
        neighbors = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        ]

        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] < 0:
                    grid[r][c] -= 1
                else:
                    grid[r][c] +=1
        for r, c in neighbors:
            if isNegative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] >0:
                grid[r][c]*=-1
            if not isNegative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] <0:
                grid[r][c]*=-1

    steps = 0
    while True:
        overflow_list = get_overflow_list(grid)
        if not overflow_list:
            break

        for r, c in overflow_list:
            isNegative = (grid[r][c]<0)
            if (r, c-1) not in overflow_list and (r-1,c) not in overflow_list:
                grid[r][c] = 0
            if (r, c-1) in overflow_list:
                if (r-1,c)  in overflow_list:
                    grid[r][c] = 2
                grid[r][c] = 1

            spread_overflow(r, c, isNegative)

        a_queue.enqueue([row[:] for row in grid])
        steps += 1

    return steps
    

