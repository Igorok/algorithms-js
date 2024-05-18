move = 0
def inc_move():
    global move
    move += 1

def hanoi_towers(n, fromPeg, toPeg):
    if (n == 1):
        inc_move()
        print(f'Move disc {n} from {fromPeg} to {toPeg}')
        return

    '''
    calculate an unused peg, to avoid third variable
    firstPeg - 1
    secondPeg - 2
    thirdPeg - 3
    so we can always can calculate one peg from two others
    '''
    unusedPeg = 6 - fromPeg - toPeg
    hanoi_towers(n - 1, fromPeg, unusedPeg)
    print(f'Move disc {n} from {fromPeg} to {toPeg}')
    inc_move()
    hanoi_towers(n - 1, unusedPeg, toPeg)



def main():
    hanoi_towers(6, 1, 3)
    print('move', move)


if __name__ == "__main__":
    main()