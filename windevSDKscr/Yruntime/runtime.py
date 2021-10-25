count = 0
while count < 5:
    f = open("com.y","r")
    lines = f.readlines()
    if lines == ".quit":
        count = 100
f.close()
