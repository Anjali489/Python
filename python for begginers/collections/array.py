from array import array
scores = array('d')
num=int(input("add a number in array:"))
scores.append(num)
scores.append(num+1)

print(scores)