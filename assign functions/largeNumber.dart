import 'dart:io';

void main() {
  var numbers = <int>[]; // Initialize an empty list to store numbers
  print("Enter a list of numbers (separated by spaces): ");
  var input = stdin.readLineSync();
  var numberStrings = input?.split(' ') ?? [];

  for (var numberString in numberStrings) {
    var number = int.tryParse(numberString);
    if (number != null) {
      numbers.add(number);
    }
  }

  if (numbers.isEmpty) {
    print("No valid numbers entered.");
  } else {
    var largestNumber = numbers.reduce((current, next) => current > next ? current : next);
    print("Largest value in the list: $largestNumber");
  }
}
