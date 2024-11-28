// class in dart
class Student {
  String? name;
  int? age;

  // constructor

  Student(String name, int age) {
    this.name = name;
    this.age = age;
  }

  void display() {
    print("Name of student: $name");
    print("Age of student: $age");
  }
}
// Another class//

class Rectangle {
  double? height;
  double? width;

  Rectangle(this.height, this.width);

  double Area() {
    return (height! * width!);
  }
}

void main() {
  Student st = Student('Ali', 23);

  // st.display();

  Rectangle r = Rectangle(4.5, 2.32);
  var area = r.Area();
  print('Area of Rectangle: $area');

  r.height = 3.4;
  r.width = 2.4;

  print('Area of Rectangle 2: ${r.Area()}');
}
