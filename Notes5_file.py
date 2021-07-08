#open file
f=open("FILENAME")
# read file, the output is string
f.read()
# if we run f.read() again, it will return empty, so it is needed to use f.seek(0) before f.read()
f.seek(0)
f.read()
#Read string as single lines in a list
f.readlines()
# Close file
f.close()

#To avoid the use of close file, go for with,:
with open("file") as f:
    s=f.read()

#write to file (change mode, w,r,a,w+,r+)
with open("file",w) as f:
    f.write("ADD CONTENTS AND REMOVE EXISING")

