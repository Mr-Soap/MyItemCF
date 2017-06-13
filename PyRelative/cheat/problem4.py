#!/usr/bin/python
class RaceTrack:
    name='';
    speeds=[];
    def __init__(self,name):
        self.name =name;
        self.speeds = [];
    @classmethod
    
    def Add(self,value):
        self.speeds.insert(len(self.speeds),value);

    @classmethod
    def Largest(self):
        if len(self.speeds) > 0:
            max=self.speeds[0]
            i=1
            while(i < len(self.speeds)):
                if self.speeds[i] > max:
                    max = self.speeds[i]
                i+=1
            return max;
        return None;

if __name__== "__main__":
    p = RaceTrack('xpjian');
    #p.Add(1.23);
    #p.Add(2.23);
    #p.Add(99.23);
    print p.Largest();