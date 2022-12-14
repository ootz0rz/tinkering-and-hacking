using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// https://leetcode.com/problems/maximum-average-subarray-i/description/
namespace csharpleetcode.arrays {
  class MaxAvgSubarrayI643 {
    public double FindMaxAverage(int[] nums, int k) {
      var curr = 0;

      // do first k vals
      for (var i = 0; i < k; i++) {
        curr += nums[i];
      }

      // slide the window along
      var max = curr;
      for (var i = k; i < nums.Length; i++) {
        // add right-most thing in our window, and subtract the previous left-most item
        curr += nums[i] - nums[i - k];

        // then just save value of largest
        max = Math.Max(max, curr);
      }

      Console.WriteLine($"{(double)max} / {(double)k}");
      return (double)max / (double)k;
    }

    public static void TestSuite() {
      _test(new[] { 5 }, 1, 5);
      _test(new[] { 1, 12, -5, -6, 50, 3 }, 4, 12.75);
    }

    static void _test(int[] nums, int k, double expected) {
      var s = new MaxAvgSubarrayI643();

      var ans = s.FindMaxAverage(nums, k);


      Debug.Assert(Math.Abs(ans - expected) <= 0.0001, $"Expected '{expected}' but got '{ans}'");
    }
  }

}
