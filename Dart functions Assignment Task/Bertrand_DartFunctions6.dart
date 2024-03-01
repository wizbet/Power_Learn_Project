//Dart Functions Assignment

//Task 6

T? getFirstElement<T>(List<T> inputList) {
  return inputList.isNotEmpty ? inputList.first : null;
}

void main() {
  List<int> myList = [10, 20, 30, 40];
  int? firstElement = getFirstElement(myList);
  print("The first element of the list is: $firstElement");
}
