from numpy import number


def callnumberforuser():
    numbertest = input("enter a number: ")
    return numbertest


def testfortest():
    while True:
        mynumber = callnumberforuser()
        mynumber = int(mynumber)
        if mynumber < 10:
            print("lower")
        else:
            print("exit code")
            break


testfortest()
