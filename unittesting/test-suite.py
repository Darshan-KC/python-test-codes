import unittest

class suiteTest(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 10
        self.b = 20
        
    def testadd(self):
        """Add"""
        result = self.a + self.b 
        self.assertTrue(result == 100)

    def testsub(self):
        """sub"""
        result = self.a - self.b 
        
def suite():
    suite = unittest.TestSuite()
    # suite.addTest (simpleTest3("testadd"))
    ## suite.addTest (simpleTest3("testsub"))
    suite.addTest(unittest.makeSuite(simpleTest3))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)