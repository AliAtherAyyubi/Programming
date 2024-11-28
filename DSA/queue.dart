// import 'dart:convert';

class Queue {
  int front = -1;
  int rear = -1;

  List<int> queue = [];
  bool isFull() {
    if (front > rear) {
      return true;
    }
    return false;
  }

  bool isEmpty() {
    if (front == -1)
      return true;
    else
      return false;
  }

  void enqueue(int data) {
    if (isFull()) {
      print('Queue is full');
    } else {
      if (front == -1) {
        front = 0;
      }
      rear++;
      // print("rear: $rear");
      queue.add(data);
      print('added');
    }
  }

  void dequeue() {
    if (isEmpty()) {
      print('Queue is empty!');
    } else {
      queue.removeAt(0);
      if (front >= rear) {
        front = -1;
        rear = -1;
      } else
        front++;
    }
  }

  void displayQueue() {
    print('Your Queue:');
    for (var i in queue) {
      print(i);
    }
  }
}

void main() {
  Queue q = new Queue();

  q.enqueue(3);
  q.enqueue(32);
  q.enqueue(36);

  q.displayQueue();

  q.dequeue();
  q.dequeue();
  q.dequeue();
  q.displayQueue();
  // print("front value: ${q.front}");
  // print(q.queue.length);
}
