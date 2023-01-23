#list operations

listValuesA = [1, 4, 9, 16, 25]
print(listValuesA)

#printing by index
print(listValuesA[1])

#concatenate
listValuesB = [2, 82, 87, 16, 25]
print(listValuesA + listValuesB)

listValuesC = [2, 82, 87, 16, 25]
#changing a value - lists are mutable
listValuesC[0] = 44
print(listValuesC)

#adding values to the end of a list
listValuesC.append(50)
print(listValuesC)
