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
    
    # verify len(nums) == N
    if len(nums) != N:
        raise ValueError("Value for N, and length of nums, does not match")
    
    # need numbers
    if N <= 0:
        return 0
    
    count = 0
    
    # create a second list where the values are increased by K
    nums2 = list(nums)
    for i, n in enumerate(nums2):
        nums2[i] = n + K
    
    # make each list a set, find intersection, and count result
    count = len(list(set(nums) & set(nums2)))
    
    return count

class SampleCases(unittest.TestCase):
    def testSample00(self):
        l1 = '5 2'
        l2 = '1 5 3 4 2'
        res = 3
        
        N, K, nums = parse_input(l1, l2)
        final = count_pairs(N, K, nums)
        
        self.assertEqual(
            res, 
            final, 
            "Sample Input #00. Got %d expected %d." % (final, res))
        
    def testSample01(self):
        l1 = '10 1'
        l2 = '363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793'
        res = 0
        
        N, K, nums = parse_input(l1, l2)
        final = count_pairs(N, K, nums)
        
        self.assertEqual(
            res, 
            final, 
            "Sample Input #01. Got %d expected %d." % (final, res))
        
class OtherCases(unittest.TestCase):
    def testInvalidN(self):
        l1 = '2 1'
        l2 = '1 2 3'
        res = '0'
        
        N, K, nums = parse_input(l1, l2)
        self.assertRaises(ValueError, count_pairs, N, K, nums)
    
if __name__ == '__main__':
    # expect two lines from stdin
#    l1 = stdin.readline().strip()
#    l2 = stdin.readline().strip()
#    
#    N, K, nums = parse_input(l1, l2)
#    print 'INPUT:', 'N', N, 'K', K, 'nums', nums
#    print 'OUTPUT:', count_pairs(N, K, nums)

#    print count_pairs(N, K, nums)
    
    # run ze tests
    unittest.main()
            