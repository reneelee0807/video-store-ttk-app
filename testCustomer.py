import unittest
from customer import Customer
from video import Video

class TestCustomer(unittest.TestCase):
    def testCustomerNameIsSet(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        self.assertEquals(aCusomter.Name, 'Julie Smith')

    def testCustomerCityIsSet(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        self.assertEquals(aCusomter.City, 'Christchurch')

    def testCustomerPaymentIsSet(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        self.assertEquals(aCusomter.Payment, 0.00)

    def testCustomerVideoListIsEmptyByDefault(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        self.assertEquals(aCusomter.VideoList, [])

    def testARentalIsAdd(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        aVideo = Video('The Avengers', 2012, True)
        aCusomter.addRental(aVideo)
        self.assertEquals(aCusomter.VideoList, [aVideo])

    def testASecondRentalIsAdd(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        
        # Add the first rental
        firstVideo = Video('The Avengers', 2012, True)
        aCusomter.addRental(firstVideo)
        
        # Add the second rental
        secondVideo = Video('Forrest Gump', 1994, True)
        aCusomter.addRental(secondVideo)
        self.assertEquals(aCusomter.VideoList, [firstVideo, secondVideo])

    def testTheRentalIsRemove(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        # Add the first rental
        firstVideo = Video('The Avengers', 2012, True)
        aCusomter.addRental(firstVideo)

        # Add the second rental
        secondVideo = Video('Forrest Gump', 1994, True)
        aCusomter.addRental(secondVideo)

        # remove the first rental
        aCusomter.removeVideo(firstVideo)
        self.assertEquals(aCusomter.VideoList, [secondVideo])

    def testPaymentIsUpdated(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        aCusomter.updatePayment()
        self.assertEquals(aCusomter.Payment, 10.00)

    def testDisplayCustomerDetailWhenNoRentals(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        detail = aCusomter.displayCustomerDetails()
        self.assertEquals(detail, 'Customer Name: Julie Smith \nCity: Christchurch \n\n \n\nTotal Payment: $0.0')

    def testDisplayCustomerDetailWithRentals(self):
        aCusomter = Customer('Julie Smith', 'Christchurch', 0.00)
        # Add rentals and update payment
        firstVideo = Video('The Avengers', 2012, True)
        aCusomter.addRental(firstVideo)  
        aCusomter.updatePayment()     
        secondVideo = Video('Forrest Gump', 1994, True)
        aCusomter.addRental(secondVideo)
        aCusomter.updatePayment()

        detail = aCusomter.displayCustomerDetails()
        self.assertEquals(detail, 'Customer Name: Julie Smith \nCity: Christchurch \n\nThe Avengers\nForrest Gump \n\nTotal Payment: $20.0')

if __name__ == '__main__':
    unittest.main()