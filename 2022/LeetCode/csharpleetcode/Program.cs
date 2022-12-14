// See https://aka.ms/new-console-template for more information
using csharpleetcode.arrays;


Console.WriteLine("Starting tests...");

var testObjs = new List<Action>() {
  //ReverseStringSolution344.TestSuite,
  MaxAvgSubarrayI643.TestSuite,
};

foreach (var t in testObjs) {
  var name = t.Method.Name;
  var cname = t.Method.DeclaringType.Name;
  Console.WriteLine("-------------------- Testing: {0} :: {1}", cname, name);

  t();
}

Console.WriteLine("Test complete!");
//Console.ReadLine();
