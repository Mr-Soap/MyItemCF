#Write a class MyClass to store email address information. 
#Store the email addresses in a dictionary named data with a user as the key and host as the value.  
#For example, david.knox@colorado.edu can be parsed into user david.knox and host colorado.edu   
#Provide method Load takes in a filename as a parameter to read the list of email addresses from a file 
#and place them in the dictionary. 
#The method returns the number of lines read or -1 if the file cannot be opened.  
#Each line of the file contains a single email address with user and host separated by an at sign('@') character. 
#Provide a Find method which is given a host string and returns a list of dictionary keys 
#that have the matching host value.
#Hint: use try-except for exception handling. Also, make sure the key and values have been stripped of whitespace.
class MyClass:
    data = {}
    
    def Load(self, filename):
        try:
            file = open(filename, "r")
        except IOError:
            return -1
        numOfLines = 0
        for line in file:
            key = line.strip().split("@")[0]
            value = line.strip().split("@")[1]
            MyClass.data[key] = value
            numOfLines += 1
        return numOfLines
    
    def Find(self, host):
        result = []
        for key, value in MyClass.data.items():
            if value == host:
                result.insert(len(result), key)
        return result

if __name__ == '__main__':
    numOfLines = MyClass.Load(MyClass, 'input.txt')
    result = MyClass.Find(MyClass, '163.com')
    print(numOfLines)
    print(result)