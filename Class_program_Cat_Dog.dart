// Define the Animal class (base class)
class Animal {
  String name;
  Animal(this.name);
}

// Define the Pet interface
abstract class Pet {
  void makeSound();
}

// Define the Cat class (inherits from Animal and implements Pet)
class Cat extends Animal implements Pet {
  Cat(String name) : super(name);

  @override
  void makeSound() {
    print('$name says "Meow!"');
  }
}

// Define the Dog class (inherits from Animal and implements Pet)
class Dog extends Animal implements Pet {
  Dog(String name) : super(name);

  @override
  void makeSound() {
    print('$name says "Woof!"');
  }
}

void main() {
  // Read pet names from a file (for demonstration, we'll use hardcoded names)
  final petNames = ['Whiskers', 'Buddy', 'Fluffy'];

  // Create instances of Cat and Dog
  final cat = Cat(petNames[0]);
  final dog = Dog(petNames[1]);

  // Demonstrate method overriding
  cat.makeSound();
  dog.makeSound();

  // Demonstrate a loop
  print('\nAll pet names:');
  for (var name in petNames) {
    print(name);
  }
}