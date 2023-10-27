from random import randint

count_heads = 0
count_tails = 0

while True:
    answer = input("Flip coin? (y/n) ")
    if answer == "n":
        break
    elif answer == "y":
        heads_tails = randint(0,1)
        if heads_tails == 0:
            print("Heads")
            count_heads += 1
        elif heads_tails == 1:
            print("Tails")
            count_tails += 1
        print(f"Head: {count_heads}     Tails: {count_tails}")
        continue
    else:
        print("Invalid answer.")
        continue