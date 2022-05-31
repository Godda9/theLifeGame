# allows to input matrix manually or auto...   (w - width   h - height)
def matrix_input(w: int, h: int):
    print("[>] Random - (1) / Manual - (2)")
    choise = int(input())
    if choise == 1:
        arr1 = [[r.randint(0, 1) for i in range(w)] for j in range(h)]  # matrix generator '0' or '1'
        return arr1
    else:
        arr1 = [[0 for _ in range(w)] for _ in range(h)]  # matrix generator '0' only

        print("\n[!] In order to stop filling in the matrix, type: -1\n")

        while True:
            os.system('cls')  # clear console
            print('   ', end='')
            for i in range(w):
                print(f"[{i}]", end='')  # [0] [1] [2] ... left
            print()

            for i in range(h):
                print(f"[{i}]", end=' ')  # [0] [1] [2] ... down
                for j in range(w):
                    print(arr1[i][j], end='  ')  # matrix[i][j]
                print()

            # user must enter valid values
            while True:
                print("\n[>] i j:", end=' ')
                inp = [int(k) for k in
                       input().split()]  # split() returns array of elements example: (input(): 1 2 - > [1, 2])
                if inp[0] == -1:
                    return arr1
                elif inp[0] not in range(0, h) or inp[1] not in range(0, w):
                    print("[x] Please enter valid values!")
                    continue
                else:
                    arr1[inp[0]][inp[1]] = 1
                    break

            # print(*arr1, sep='\n')


def get_sosedi(array: list, i: int, j: int, width: int, height: int):
    count = 0
    if j + 1 <= width - 1:
        if array[i][j + 1] == 1:
            count += 1
            # print(f"IF 1 right ")   # +++++++

    if j - 1 >= 0:
        if array[i][j - 1] == 1:
            count += 1
            # print(f"IF 2 left ")   # +++++++

    if i + 1 <= height - 1:
        if array[i + 1][j] == 1:
            count += 1
            # print(f"IF 3 down:")   # +++++++

    if i - 1 >= 0:
        if array[i - 1][j] == 1:
            count += 1
            # print(f"IF 4 up")   # +++++++

    return count


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
