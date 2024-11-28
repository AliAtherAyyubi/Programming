class Student {
  String? name;
  int? age;

  void display() {
    print("Name of student: $name");
    print("Age of student: $age");
  }
}

void main() {
  Student st = Student();

  st.name = 'Ali Ather';
  st.age = 22;
  st.display();
}
