my_file = open("vasobuilder.config", "r")
content_list = my_file. readlines()
my_file.close()
True
x = 0
allowcmd = 1
while True:
    x = x + 1
    file = open(content_list[x], "r")

    for line in file:
        for character in line:
            previous = character
            m = 1
            while m = 1:
               if != 9:
                    try:
                        parser = character + previous
                    previous = character
                    if allowcmd == 1:
                        if parser == "print":
                            allowcmd = 9
               else:
                    for character in line:
                        if character != ";":
                            paser = character + previous
                            previous = character

    
