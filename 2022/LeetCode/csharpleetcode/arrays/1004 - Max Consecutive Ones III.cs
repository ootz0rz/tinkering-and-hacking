using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// https://leetcode.com/problems/max-consecutive-ones-iii/description/
namespace csharpleetcode.arrays {
  class _1004___Max_Consecutive_Ones_III {
    public int LongestOnes(int[] nums, int k) {

      var left = 0;
      var right = 0;
      var max = 0;
      var zeroes = 0;

      while (right < nums.Length) {
        if (nums[right] == 0) {
          zeroes++;
        }

        while (left <= right && zeroes > k) {
          if (nums[left] == 0) {
            zeroes--;
          }

          left++;
        }

        max = Math.Max(max, right - left + 1);

        right++;
      }

      return max;
    }
  }
}
