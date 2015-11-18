import os,sys
from random import *
from Wikipedia_API import *
from DAO import *

class Trainingset:
    def __init__(self):
        self.DAO = DAO()
        self.api = Wikipedia_API()
        self.links = self.read_file("links.txt") ## 285 Topics Successfully Parsed
        ## self.random = self.api.get_random(285)
        
    def annotate(self, input):
        print("Beginning annotation of {} titles.".format(len(input)))
        inserted = 0
        for title in input:
            try:
                page_info = self.api.get_article_info(title)
                ## print("Title: {}".format(title))
                ## page_info['topic_score'] = input("Enter a topic score for {} (How topical is this article?) > ".format(title))
                ## page_info['code_score'] = input("Enter a Software Engineering score {} (How related to code is this article?) > ".format(title))
                inserted_id = self.DAO.insert_one(page_info)
                print("Inserted: {}".format(inserted_id))
                inserted += 1
            except Exception as e:
                print(e)
        print("Inserted: {} article objects.".format(inserted))
            
    def test(self, input):
        successfully_parsed = 0
        errored_out = []
        for title in input:
            try:
                page_info = self.api.get_article_info(title)
                if page_info['links'] is not None:
                    successfully_parsed += 1
                    print("Parsed {}".format(title))
            except Exception as e:
                print(e)
                errored_out.append(title)
                
        return successfully_parsed, errored_out
            
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
set.annotate(set.links)