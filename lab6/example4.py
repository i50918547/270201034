itemCount = int(input("How many element will you enter? "))
usersList = list()
uniqueList = list()
for i in range(itemCount):
	usersList.append(input(f"{i+1}. element: "))
for i in range(itemCount):
	if not usersList[i] in uniqueList:
		uniqueList.append(usersList[i])

sorted(uniqueList, reverse=True)



print(usersList,"\n",uniqueList, "\n", descendedList)

