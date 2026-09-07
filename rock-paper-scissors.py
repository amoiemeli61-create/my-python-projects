print("welcome to the game")
p1_name = input("Enter player 1 name:")
p2_name = input("Enter player 2 name:")
p3_name = input("Enter player 3 name:")
rounds = int(input("How many rounds?"))
score1 = 0
score2 = 0
score3 = 0
for i in range(1, rounds + 1):
    print("\nRound", i)
    p1 = int(input(p1_name + "(1:(paper),2:(stone),3:(scissores):"))
    p2 = int(input(p2_name + "(1:(paper),2:(stone),3:(scissores):"))
    p3 = int(input(p3_name + "(1:(paper),2:(stone),3:(scissores):"))
    if (
        (p1 == 1 and p2 == 2 and p3 == 2)
        or (p1 == 3 and p2 == 1 and p3 == 1)
        or (p1 == 2 and p2 == 3 and p3 == 3)
    ):
        score1 += 1
        print(p1_name, "wins")
    elif (
        (p2 == 3 and p1 == 1 and p3 == 1)
        or (p2 == 1 and p1 == 2 and p3 == 2)
        or (p2 == 2 and p1 == 3 and p3 == 3)
    ):
        score2 += 1
        print(p2_name, "wins")
    elif (
        (p3 == 1 and p1 == 2 and p2 == 2)
        or (p3 == 3 and p1 == 1 and p2 == 1)
        or (p3 == 2 and p1 == 3 and p2 == 3)
    ):
        score3 += 1
        print(p3_name, "wins")
    else:
        print("Draw or complex win!")
print("\n Final score")
print(p1_name, ":", score1)
print(p2_name, ":", score2)
print(p3_name, ":", score3)
