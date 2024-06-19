#Indexing
''''text = "Hello world!"
#       012345678910
input()
print(text[6])

word = input("Word: ")
print(text[-9])
# -3 -2 -1 0 1 2 3 4 5 6 7 8 9 
print(word[len(word)-1])'''

#Slicing

'''text = "hello World"
print(text[-6:11])
print(text[0:2], text[6:8])

name = "diana"
print("{0} {1}".format(text[6:8], text[6:8]))
print(f"{text[0:2]} {text[6:8]}")'''

#String Methods

word = "helloWORLD"
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.replace("h", "x"))
print(word.find("h"))
print(word.isalpha())
print(word.isnumeric())
print(word.isalnum())
