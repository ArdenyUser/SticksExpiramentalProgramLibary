file1 = open('compiler.config', 'r')
Lines = file1.readlines()
 
count = 0
for line in Lines:
    count += 1
    if count == 1:
      name = line
    if count == 2:
      powershellcompile = line
file1.close()


my_file = open("PScompiler.config", "r")
content_list = my_file. readlines()
my_file.close()
    

file1 = open("cpile.ps1", "a")  # append mode
file1.write("jar -cf " + name + " *.java\n")
file1.write("wget STICKSCLIENT\n")
if powershellcompile == "TruePS1":
  for x in content_list:
      temp = "ps2exe " + x + ".ps1"
      file1.write(temp + "/n")
file1.close()
