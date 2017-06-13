#write a function that is given a list of integer values and an integer value, 
#returns the integer number of items that are greater than the given value.
#Use the following function definition
#def CountItems(items, value):
def CountItems(item, letter):
    count = 0
    i = 0
    while(i < len(item)):
        if item[i] > letter:
            count += 1
        i += 1
    return count
if __name__ == '__main__':
    item = [2, 3, 8, 5, 6]
    letter = 3
    result = CountItems(item, letter)
    print(result)