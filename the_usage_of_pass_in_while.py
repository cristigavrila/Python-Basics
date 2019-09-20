#"pass" is used when you do not have nothing the make after a condition

x = 0
while x < 8:
    x +=1
    if x == 4:
        pass
    #insted of a block use pass to get over
    print(x)
