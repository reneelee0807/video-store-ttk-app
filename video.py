class Video:

    # constructor
    def __init__(self, title, year, status):    
        self.__title = title
        self.__year = year
        self.__status = status 

    #getter and setter for videoTitle
    @property
    def Title(self):
        return self.__title

    @Title.setter
    def Title(self, title):
        self.__title = title

    #getter and setter for videoYear
    @property
    def Year(self):
        return self.__year

    @Year.setter
    def Year(self, year):
        self.__year = year

    #getter and setter for videoStatus
    @property
    def Status(self):
        return self.__status

    @Status.setter
    def Status(self, status):
        self.__status = status
    
    # display video details
    def displayVideoDetails(self):
        convertedStatus = 'Available' if self.__status else 'Not Available'
        return f'{self.__title} {self.__year} {convertedStatus}'

