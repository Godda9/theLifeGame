import os           # to clear console
import random as r  # to generate numbers
import asyncio      # to pause main thread


def matrix_input(w: int, h: int):
    pass


def get_sosedi(array: list, i: int, j: int, width: int, height: int):
    pass


def main():
    os.system('cls')
    print("[!] Enter matrix width: ", end='')
    width = int(input())
    if width <= 0:
        if width == 0:
            width += 5
        else:
            width = abs(width)

    print("[!] Enter matrix height: ", end='')
    height = int(input())
    if height <= 0:
        if height == 0:
            height += 5
        else:
            height = abs(height)
    print()

    # matrix input
    arr = matrix_input(w=width, h=height)      # arr = list returned from matrix_input

    while True:
        alive = 0
        for i in range(height):
            for j in range(width):
                temp = get_sosedi(arr, i, j, width, height)      # count all nearest cells

                if (temp < 2 or temp > 3) and arr[i][j] == 1:    # rule 1
                    arr[i][j] = 0

                if arr[i][j] == 1 and (temp == 2 or temp == 3):  # rule 2
                    continue

                if temp == 3 and arr[i][j] == 0:                 # rule 3
                    arr[i][j] = 1

            asyncio.run(asyncio.sleep(0.3))  # main thread sleep for 0.3 sec
            os.system('cls')   # clear console
            print(*arr, sep='\n')

        for i in range(0, height):       #
            for j in range(0, width):    # just to calculate count (alive)
                if arr[i][j] == 1:       #
                    alive += 1           #

        if alive == 0:
            break


if __name__ == '__main__':
    main()
