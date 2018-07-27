import unittest

def fun(x):
    return x + 1

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    test = Test.test()
    #test.test()
