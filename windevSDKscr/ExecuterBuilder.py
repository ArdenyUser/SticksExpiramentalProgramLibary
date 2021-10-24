my_file = open("Exelinker.config", "r")
content_list = my_file. readlines()
my_file.close()

my_file = open("EXECUTE.ps1", "w")
for x in content_list:
    file1.write(content_list)
my_file.close()

    
