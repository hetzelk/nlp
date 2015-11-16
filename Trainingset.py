import os,sys
from random import *


class Trainingset:
    def __init__(self):
        pass
    
    
    def mash(self,input1_path,input2_path,output_path):
        
        path = os.path.dirname(os.path.abspath(__file__))         
        fullpath = (os.path.join(path, input1_path))
        inputfile1=""
        
        file1 = open(os.path.join(path, input1_path), 'r').read()
        file2 = open(os.path.join(path, input2_path), 'r').read()
        
        concatfile = (file1+"\r\n"+file2).split()
        
        randomfile= ""
        print (len(concatfile))
        while(len(concatfile) != 1):
            random = randrange(0,len(concatfile))
            line = concatfile[random]
            randomfile=randomfile + "\r\n" + line
            print(line)
            
            del concatfile[random]
    def annotate(self):
        pass
    
#simpletest 
set1= Trainingset()
set1.mash("links.txt","random.txt","output.txt")
