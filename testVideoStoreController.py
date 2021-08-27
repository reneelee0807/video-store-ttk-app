import unittest
from video import Video
from customer import Customer
from videoStoreController import VideoStoreController

class TestVideoStoreController(unittest.TestCase):      
    def testAVideoIsAdded(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')

        self.assertEqual(videoStore.allVideos[0].__dict__, Video('The Avengers', '2012', True).__dict__)

    def testACustomerIsAdded(self):
        videoStore = VideoStoreController()
        videoStore.addCustomerIntoCustomerList('Julie Smith', 'Christchurch', '0.00')

        self.assertEqual(videoStore.allCustomers[0].__dict__, Customer('Julie Smith', 'Christchurch', 0.00).__dict__)

    def testAVideoIsRentedSuccessfullyThatReturnTrue(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')
        videoStore.addCustomerIntoCustomerList('Julie Smith', 'Christchurch', '0.00')
        isSuccessful =videoStore.rentVideo('Julie Smith','The Avengers')

        self.assertTrue(isSuccessful)

    def testAVideoIsFailedToRentedThatReturnFalse(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'false')
        videoStore.addCustomerIntoCustomerList('Julie Smith', 'Christchurch', '0.00')
        isSuccessful =videoStore.rentVideo('Julie Smith','The Avengers')

        self.assertFalse(isSuccessful)

    def testAVideoIsReturnedSuccessfullyThatReturnTrue(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')
        videoStore.addCustomerIntoCustomerList('Julie Smith', 'Christchurch', '0.00')
        videoStore.rentVideo('Julie Smith','The Avengers')
        isSuccessful = videoStore.returnVideo('Julie Smith','The Avengers')

        self.assertTrue(isSuccessful)

    def testAVideoIsFailedToReturnedThatReturnFalse(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'false')
        videoStore.addCustomerIntoCustomerList('Julie Smith', 'Christchurch', '0.00')
        isSuccessful = videoStore.returnVideo('Julie Smith','The Avengers')

        self.assertFalse(isSuccessful)

    def testFindVideoThatReturnFoundVideo(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('Forrest Gump', '1994', 'true')
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')
        foundVideo = videoStore.findVideo('The Avengers')
        
        self.assertEqual(foundVideo.__dict__, Video('The Avengers', '2012', True).__dict__)

    def testFindVideoThatReturnNone(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('Forrest Gump', '1994', 'true')
        foundVideo = videoStore.findVideo('The Avengers')
        
        self.assertEqual(foundVideo, None)

    def testFindCustomerThatReturnFoundNone(self):
        videoStore = VideoStoreController()
        videoStore.addCustomerIntoCustomerList('Mary Smith', 'Christchurch', '0.00')
        foundCustomer = videoStore.findCustomer('Julie Smith')
        
        self.assertEqual(foundCustomer, None)

    def testGetVideoDetailWhenVideoIsInTheList(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')
        detail = videoStore.getVideoDetail('The Avengers')
        self.assertEquals(detail, 'The Avengers 2012 Available')

    def testGetCustomerDetailWhenCustomerIsNotInTheList(self):
        videoStore = VideoStoreController()
        videoStore.addVideoIntoVideoList('The Avengers', '2012', 'true')
        detail = videoStore.getVideoDetail('Forrest Gump')
        self.assertEquals(detail, None)




if __name__ == '__main__':
    unittest.main()