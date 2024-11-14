while (True):
    try:
        n = int(input())
    except:
        break
    test = 1
    count = 1
    while True:
        if test%n == 0:
            print(count)
            break
        test = test*10 + 1
        count += 1