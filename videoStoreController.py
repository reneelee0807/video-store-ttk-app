from customer import Customer
from video import Video

class VideoStoreController:
    def __init__(self):
        self.allVideos = []
        self.allCustomers = []

    # add new video into the video list
    def addVideoIntoVideoList(self,title, year, status):
        formatedStatus = True if status.strip() == 'true' else False
        aVideo = Video(title.strip(), year.strip(), formatedStatus)
        self.allVideos.append(aVideo)

    # add new customer into the customer list
    def addCustomerIntoCustomerList(self, name, city, payment):
        aCustomer = Customer(name.strip(), city.strip(), float(payment))
        self.allCustomers.append(aCustomer)


    #rent a video, returns a boolean status
    def rentVideo(self, aCustName, aVideoTitle):
        foundCustomer = self.findCustomer(aCustName)
        foundVideo = self.findVideo(aVideoTitle)
        print(foundVideo.Status)
        if foundVideo.Status:
            foundVideo.Status = False
            foundCustomer.addRental(foundVideo)
            foundCustomer.updatePayment()
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
        if foundCustomer:
            return foundCustomer.displayCustomerDetails()
        return None

    def getVideoDetail(self, aVideoTitle):
        foundVideo = self.findVideo(aVideoTitle)
        if foundVideo:
            return foundVideo.displayVideoDetails()
        return None
