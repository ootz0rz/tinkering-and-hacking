using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace csharpleetcode.arrays {
  public class ReverseStringSolution344 {
    public void ReverseString(char[] s) {
      var left = 0;
      var right = s.Length - 1;

      while (left < right) {
        var t = s[left];
        s[left] = s[right];
        s[right] = t;

        left++;
        right--;
      }
    }

    public static void TestSuite() {
      _test("a");
      _test("ab");
      _test("abc");
      _test("hello");
      _test("hello!");
    }

    static void _test(string input) {
      var forwards = input.ToCharArray();
      var reversed = input.ToCharArray().Reverse().ToArray();

      Console.WriteLine($"Test: {new String(forwards)} -> {new String(reversed)}");

      var s = new ReverseStringSolution344();
      s.ReverseString(forwards);
      Debug.Assert(forwards.SequenceEqual(reversed), $"Expected '{new String(reversed)}' but got '{new String(forwards)}'");
    }

    const string _str1 = "hello";
  }
}
