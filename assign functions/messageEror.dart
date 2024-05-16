void main() {
  String message = "Hello";
  try {
    print("The character at position 5 is ${message[5]}.");
  } catch (e) {
    print("An exception occurred: $e");
  }
  print("Bye!");
}
