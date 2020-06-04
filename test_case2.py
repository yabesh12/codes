import unittest

class TestInput(unittest.TestCase):

    def test_case(self):
        input = [1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]

        d = {input[num]:input.count(input[num]) for num in input}

        for k,v in d.items():# k has key and v has value 
            if v>1:
                print(k,"-",v)
if __name__ == "__main__":
    unittest.main()