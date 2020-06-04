import unittest

class TestCase(unittest.TestCase):
    def test_one(self):

        l = [1,2,0,0,4,1,6,2,1,3]

        b1=[]
        b2=[]
        b3=[]
        b3=b1

        for ball in range(len(l)):
            if (ball %5 != 0):
                if (l[ball]%2==0) or l[ball]==1:
                    b3=b2
                else:
                    b3=b1
            else:
                if (ball!=0):
                    if (l[ball-1]%2!=0):
                        b3=b1
                    else:
                        b3=b2
            b3.append(l[ball])



        print("Total Score : ", sum(l))
        print("Batsman 1 Score: ", sum(b1),"(",*b1,")")
        print("Batsman 2 Score: ", sum(b2),"(",*b2,")")

if __name__ == "__main__":
    unittest.main()            





