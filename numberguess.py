while True:
    print("Enter '0' for exit.")
    val = int(input("Guess a number: "))
    if val == 0:
            break
    elif(val>10 and val<100):
            print("Nice job!!\n")
    else:
            print("Nice Try\n")
