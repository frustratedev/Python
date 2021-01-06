# Coding challenge part 6
# 1. Write Python code to open a file named demo.txt and write some random data into it.
# 2. Open the file, read the contents and display them as output.
# 3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.

#Write
file = open('demo.txt', 'w')
file.write("Captain Evan Natividad, Pilot in Command")

#Append
file = open('demo.txt', 'a')
file.write("\nAir New Zealand")

#Read
file = open('demo.txt', 'r')
content = file.read()
print(content)