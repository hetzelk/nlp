import os,sys
from random import *
from Wikipedia_API import *
from DAO import * 

class Trainingset:
    def __init__(self):
        self.DAO = DAO()
        self.api = Wikipedia_API()
        self.links = self.read_file("links.txt")
        self.training_set = []
        self.training_dict = {'set': None}
        
    def annotate(self, input, collection):
        for title in input:
            page_info = self.api.get_article_info(title)
            ## page_info['topic_score'] = input("Enter a topic score (How topical is this article?) > ")
            ## page_info['code_score'] = input("Enter a code score (How related to code is this article?) > ")
            inserted_id = self.DAO.insert_one(page_info)
            if inserted_id is not None:
                return True
            
    def read_file(self, file):
        file = open('links.txt', 'r+')
        lines = file.readlines()
        file.close()
        return [line[:-1] for line in lines]

    def mash(self,input1_path,input2_path,output_path):
        path = os.path.dirname(os.path.abspath(__file__))
        fullpath = (os.path.join(path, input1_path))
        inputfile1 = ""
        
        file1 = open(os.path.join(path, input1_path), 'r').read()
        file2 = open(os.path.join(path, input2_path), 'r').read()
        
        concatfile = (file1+"\r\n"+file2).split()
        
        randomfile = ""
        print(len(concatfile))
        while(len(concatfile) != 1):
            random = randrange(0,len(concatfile))
            line = concatfile[random]
            randomfile = randomfile + "\r\n" + line
            print(line)
            
            del concatfile[random]
        return randomfile
            
set = Trainingset()
set.annotate("TEST", set.links)