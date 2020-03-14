class person:
    totalObjects=0
    def __init__(self):
        person.totalObjects=person.totalObjects+1

    #@classmethod
    def showcount(self):
        print("Total objects: ",self.totalObjects)




class greeting:
    @staticmethod
    def greet():
        print("Hello!")
greeting.greet()
