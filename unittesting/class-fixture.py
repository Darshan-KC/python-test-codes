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
        

