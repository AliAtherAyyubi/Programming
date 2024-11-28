// Encapsulation in Dart//

class Employee {
  int? _id;
  String? _name;

  int getId() {
    return _id!;
  }

  void setId(int id) {
    this._id = id;
  }

  String getName() {
    return _name!;
  }

  void setName(String n) {
    this._name = n;
  }
}

void main() {
  Employee e = Employee();

  e.setId(56);

  print('${e._id}');
}
