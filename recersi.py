def retroc(e):
    print("{},".format(e), end = "")
    if e==0:
        return
    rectroc(e-1)
    
retroc(10)

