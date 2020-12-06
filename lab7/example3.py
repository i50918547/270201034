books =  ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookDict = dict()

for i in range(len(books)):
	tup = ((len(books[i]), len(set(books[i])), (len(books[i]) + len(set(books)))/2 ))
	bookDict.update({books[i]: tup})

print(bookDict)