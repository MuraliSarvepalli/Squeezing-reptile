#unittest sample

import unittest

class SampleTest(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('MURALI'.isupper())
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_strip(self):
        s='geeksforgeeks'
        self.assertEqual(s.strip('geek'),'sforgeeks')

if __name__=='__main__':
    unittest.main()
