import unittest
from video import Video

class TestVideo(unittest.TestCase):
    def testVideoTitleIsSet(self):
        aVideo = Video('The Avengers', '2012', True)
        self.assertEquals(aVideo.Title, 'The Avengers')

    def testVideoYearIsSet(self):
        aVideo = Video('The Avengers', '2012', True)
        self.assertEquals(aVideo.Year, '2012')

    def testVideoStatusIsSet(self):
        aVideo = Video('The Avengers', '2012', True)
        self.assertEquals(aVideo.Status, True)

    def testDisplayVideoDetailWhenVideoIsAvailable(self):
        aVideo = Video('The Avengers', '2012', True)
        detail = aVideo.displayVideoDetails()
        self.assertEquals(detail, 'The Avengers 2012 Available')

    def testDisplayVideoDetailWhenVideoIsNotAvailable(self):
        aVideo = Video('The Avengers', '2012', False)
        detail = aVideo.displayVideoDetails()
        self.assertEquals(detail, 'The Avengers 2012 Not Available')

if __name__ == '__main__':
    unittest.main()