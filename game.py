import random

def main():
    n = input("level: ")
    n = int(n)
    if n <= 100:
        i = check(n)
        j = ""
        i = int(i)
        while j != i:
            j = input("Guess: ")
            j = int(j)
            if j < i:
                print("Too Small!")
            elif j > i:
                print("Too Big")
            elif j == i:
                print("Correct")
                break

def check(n):
    n = int(n)
    if n > 0:
        n = int(n)
        i = random.randint(1, n)
        i = int(i)
        return i

if __name__ == "__main__":
    main()
