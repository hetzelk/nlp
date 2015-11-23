import urllib.request

class Exponentialsearch():
    def __init__(self):
        self.html = 0
        self.baseurl = 0
        self.listofall = 0
        self.goodlist = 0
        self.endlist = []

    def start(self):
        urllink = self.baseurl
        with urllib.request.urlopen(urllink) as url:
            html = url.read()
            self.html = html

    def allfinder(self):
        html = self.html
        html = html.decode().split(" ")
        allptags = []
        listofall = []

        for eachpfind in html:
            allptags.append(eachpfind)

        self.listofall = allptags

    def filter(self):
        badfilter = []
        for each in self.listofall:
            if "\n" in each:
                badfilter.append(each)
            if "=" in each:
                badfilter.append(each)
            if "<" in each:
                badfilter.append(each)
            if ">" in each:
                badfilter.append(each)
            if "//" in each:
                badfilter.append(each)
            if "\\\\" in each:
                badfilter.append(each)

        self.goodlist = list(set(self.listofall) - set(badfilter))

    def encoder(self): #take this out if you don't want it to be encoded
        for each in self.goodlist:
            self.endlist.append(each.encode('utf-8'))

    def main(self):
        self.baseurl = input("Hit enter to start")
        self.start()
        self.allfinder()
        self.filter()
        self.encoder()
        print(self.endlist)
        print(len(self.endlist))

   
expo = Exponentialsearch()
expo.main()

