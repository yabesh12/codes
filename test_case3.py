import unittest

class TestFunc(unittest.TestCase):

    def func(kwargs):
        total = sum(input.values())
        return total
        input = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
        print(func(input))
        
if __name__ == "__main__":
    unittest.main()
