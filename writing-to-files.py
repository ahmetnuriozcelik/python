# Creates a file or if the file does not exist it overwrites the file
with open("quotes_new.txt","w") as handle:
    handle.write("This is the first line \n")

# Adds a line to an existing file
with open("quotes_new.txt","a") as handle:
    handle.write("This is the second line \n")

# Reads a file and writes it on another file
with open("quotes.txt","r") as handle1:
    with open("quotes_copy.txt","w") as handle2:
        for line in handle1:
            handle2.write(line)
# Prints the new file that is copied from quotes.txt  
with open("quotes_copy.txt") as handle1:
    file_read=handle1.read()
    print(file_read)
