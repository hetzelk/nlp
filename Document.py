
class Document:
    def __init__(self, info = {
          'url': None
        , 'topic': None
        , 'text': None
        , 'summary': None
        , 'times_calculated':None
        , 'word_counts': None
        }):
        self.info = info
        
    #functions to get data and put into dictionary for pymongo storage
    
    #with dict setup in init, we can pass in the json object when we instantiate the class in order to change it if necessary, ie update scores etc
    #Or, to then access it within this class context for display purposes