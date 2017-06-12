# Create a class named Student that has public data members course (string) and scores (list of integer values). 
# Provide a constructor that takes a parameter for initializing the course and initializes the list to an empty list.  
# Provide a public method Add(value) to add new items to the end of the list.  
# Also provide a public method Total() that returns total of values in list 
# or if there are no values in the list, return None.
class Student:
    course = ''
    scores = []
    
    def __init__(self, course):
        self.course = course
        self.scores = []
    
    def Add(self, value):
        self.scores.insert(len(self.scores), value)
    
    def Total(self):
        sum = 0
        i = 0
        if(len(self.scores) == 0):
            return None
        while(i < len(self.scores)):
            sum += self.scores[i]
            i += 1
        return sum
        
if __name__ == '__main__':
    Student.__init__(Student, 'aaa')
    Student.Add(Student, 100)
    Student.Add(Student, 200)
    print(Student.course)
    print(Student.scores)
    print(Student.Total(Student))