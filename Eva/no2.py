def ejectNos(list):
    pos = 2-1 # takes function to the next position
    idN = 0
    lenList = (len(list))
    while lenList > 0:
	    idN = (pos+idN)%lenList
	    print(list.pop(idN))
	    lenList -= 1
numbers = ['12','13','14','15','16','17','18']
ejectNos(numbers)