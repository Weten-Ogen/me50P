import unittest
from que import MyQueue



class Tests(unittest.TestCase):
    
    l = MyQueue()
    k = l.is_empty()

    def test_1(self):
        self.assertTrue(self.k)
    
    def test_2(self):
        self.l.enqueue("marcus")
        m = self.l.dequeue()
        self.assertTrue(m , "marcus")

    
if __name__ == "__main__":
    unittest.main()
