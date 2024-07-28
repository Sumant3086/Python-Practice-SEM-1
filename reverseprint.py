def reversePrint(num):
    if num>5:
        return
        reversePrint(num+1)
        print(num)
reversePrint(1)