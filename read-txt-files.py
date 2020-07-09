# The file is opened, read and closed
handle= open("quotes.txt", "r")
file_read=handle.read()
print(file_read)
handle.close()

# The file is closed automatically by using with statement
with open("quotes.txt", "r") as handle:
    file_read=handle.read()
    print(file_read)
