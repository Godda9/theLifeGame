import asyncio      # to pause main thread
import os           # to clear console
import random as r  # to generate numbers


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
def main():
    os.system('cls')
    print("[!] Enter matrix width: ", end='')
    width = int(input())
    print("[!] Enter matrix height: ", end='')
    height = int(input())
     # matrix input
    arr = matrix_input(w=width, h=height)      # arr = list returned from matrix_input
    

if __name__ == '__main__':
    main()
