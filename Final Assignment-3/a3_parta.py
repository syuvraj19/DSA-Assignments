# Main Author: Yuvraj Singh
# Main Reviewer: Avreet Kaur & Ravneet Kaur

def evaluate_board(board, player):
    winningPoint = 100
    losingPoint = -100
    drawPoint = 0
    value = 0
    total = 0
    gem = 0
    for row in board:
        for cell in row:
            if cell != 0:
                if cell < 0:
                    value = -cell                 
                else:
                    value = cell
                total += value
                if player == 1 and cell > 0:
                    gem += value
                if player == -1 and cell < 0:
                    gem += value
    if gem == total:
        return winningPoint
    if gem == 0:
        return losingPoint
    if total == 0:
        return drawPoint
    score = (gem * 100) // total
    return score
