from customer import Customer
from video import Video

class VideoStoreController:
    def __init__(self):
        self.allVideos = []
        self.allCustomers = []

    # add new video into the video list
    def addVideoIntoVideoList(self,title, year, status):
        aVideo = Video(title, year, status)
        self.allVideos.append(aVideo)

    # add new customer into the customer list
    def addCustomerIntoCustomerList(self, name, city, payment):
        aCustomer = Customer(name, city, float(payment))
        self.allCustomers.append(aCustomer)


    #rent a video, returns a boolean status
    def rentVideo(self, aCustName, aVideoTitle):
        foundCustomer = self.findCustomer(aCustName)
        foundVideo = self.findVideo(aVideoTitle)
        if foundVideo.Status:
            foundVideo.Status = False
            foundCustomer.addRental(foundVideo)
            return True
        else:
            return False
    
    #return a video
    def returnVideo(self, aCustName, aVideoTitle):
        foundCustomer = self.findCustomer(aCustName)
        
        for video in foundCustomer.VideoList:
            if video.Title == aVideoTitle:
                foundVideo = self.findVideo(aVideoTitle)
                foundVideo.Status = True
                foundCustomer.removeVideo(foundVideo)
                foundCustomer.updatePayment()
                return True
        return False
            
    
    #find a video based on a title, returns video object or None
    def findVideo(self, aTitle) -> Video:
        for video in self.allVideos:
            if video.Title == aTitle:
                return video
        return None

    #find a customer based on name, returns a customer object or None
    def findCustomer(self, aName) -> Customer:
        for customer in self.allCustomers:
            if customer.Name == aName:
                return customer
        return None

    def getCustomerDetail(self, aName):
        foundCustomer = self.findCustomer(aName)
        return foundCustomer.displayCustomerDetails()

    def getVideoDetail(self, aVideoTitle):
        foundVideo = self.findVideo(aVideoTitle)
        return foundVideo.displayVideoDetails()





    # # display all movies' details
    # def displayAllMoviesDetails(self) -> str:
    #     pass

    # # search movie by name
    # def searchMovie(self, mName) -> Movie:
    #     pass

    # # use 'searchMovie' function to find a movie then display a movie details
    # def displayAMovieDetails(self, mName) -> str:
    #     pass

    # # use 'searchMovie' function to find a movie then set movie is rented by setting isRented to true
    # def setMovieIsRented(self, mName):
    #     pass

    # # use 'searchMovie' function to find a movie then set movie is return by setting isRented to false
    # def setMovieIsReturned(self, mName):
    #     pass



    # """
    #     functions to create and maintain the Customer objects
    # """

    # # display all customers' details
    # def displayAllCustomerDetails(self) -> str:
    #     pass

    # # search customer by customer email as customer email is unique
    # def searchCustomer(self, cEmail) -> Customer:
    #     pass

    # # use 'searchCustomer' function to find customer then display a customer details
    # def displayACustomerDetails(self, cEmail) -> str:
    #     pass



    # # use 'searchCustomer' function to find customer then add a movie to the rental list to store the movie that customer is rented
    # def addRental(self, cEmail, aMovie):
    #     pass

    # # use 'searchCustomer' function to find customer then delete movie from the rental List when movie is return
    # def deleteRental(self, cEmail, aMovie):
    #     pass

    # # generate a payment object by movies that customer is going to pay for
    # def generatePayment(self, movies) ->Payment:
    #     pass

    # # use 'searchCustomer' function to find customer then add the payment into the customer rental payment record list
    # def addRentalPaymentRecordForACustomer(self, cEmail, aPayment):
    #     pass