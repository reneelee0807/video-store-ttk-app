class Customer:
    # constructor
    def __init__(self, name, city, payment):
        self.__name = name
        self.__city = city
        self.__payment = payment
        self.__videoList = []

    # getter and setter for name
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    # getter and setter for city
    @property
    def City(self):
        return self.__city

    @City.setter
    def City(self, city):
        self.__city = city

    # getter and setter for payment
    @property
    def Payment(self):
        return self.__payment

    @Payment.setter
    def Payment(self, payment):
        self.__payment = payment

    # getter for video list
    @property
    def VideoList(self):
        return self.__videoList

    # add a video from the list
    def addRental(self, aVideo):
        self.__videoList.append(aVideo)

    # remove a video from the list
    def removeVideo(self, aVideo):
        self.__videoList.remove(aVideo)  

    # update payment
    def updatePayment(self):
        self.__payment += 10.00
        
    # customer detailed information
    def displayCustomerDetails(self):
        videoTitles = self.getAllVideoTitles()
        return f'Customer Name: {self.__name} \nCity: {self.__city} \n\n{videoTitles} \n\nTotal Payment: ${self.__payment}'

    def getAllVideoTitles(self):
        videoTitles = []
        for video in self.__videoList:
            videoTitles.append(video.Title)
        return '\n'.join(videoTitles)
       