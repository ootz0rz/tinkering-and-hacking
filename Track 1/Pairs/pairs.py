import unittest
from sys import stdin

def parse_input(l1, l2):        
    N, K = l1.split(' ')
    nums = l2.split(' ')
    
    N = int(N)
    K = int(K)
    
    for index, n in enumerate(nums):
        nums[index] = int(nums[index])
    
    return (N, K, nums)

def count_pairs(N, K, nums):
    return 0

class SampleCases(unittest.TestCase):
    def sample00(self):
        l1 = '5 2'
        l2 = '1 5 3 4 2'
        res = '3'
        
        N, K, nums = parse_input(l1, l2)
        
        self.assertEqual(
            res, 
            count_pairs(N, K, nums), 
            "Sample Input #00")
        
    def sample01(self):
        l1 = '10 1'
        l2 = '363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793'
        res = '0'
        
        N, K, nums = parse_input(l1, l2)
        
        self.assertEqual(
            res, 
            count_pairs(N, K, nums), 
            "Sample Input #01")
    
if __name__ == '__main__':
    # expect two lines from stdin
    l1 = stdin.readline().strip()
    l2 = stdin.readline().strip()
    
    N, K, nums = parse_input(l1, l2)
    print N, K, nums
    
    # run ze tests
    unittest.main()
            