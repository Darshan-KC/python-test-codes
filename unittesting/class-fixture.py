import unittest

class TestFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('called once before any tests in class')
        
    @classmethod
    def tearDownClass(cls):
        print('\ncalled once after all tests in class')
        
    def setUp(self):
        self.a=10
        self.b=20
        name=self.shortDescription()
        print('\n',name)
        
    def tearDown(self):
        print('\nend of test',self.shortDescription())
        
    def test1(self):
        """One"""
        result = self.a + self.b 
        self.assertTrue(True)
        
    def test2(self):
        """Two"""
        result = self.a - self.b
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
        

