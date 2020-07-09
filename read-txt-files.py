# The file is opened, read and closed
handle= open("quotes.txt", "r")
file_read=handle.read()
print('This is  the open/close method \n',file_read)
handle.close()

# The file is closed automatically by using with statement
with open("quotes.txt", "r") as handle:
    file_read=handle.read()
    print('This is the with option \n',file_read)

# For loop is used to read the file
with open("quotes.txt", "r") as handle:
    print("File is read using a for loop line by line")
    for line in handle:
        print (line.strip())
