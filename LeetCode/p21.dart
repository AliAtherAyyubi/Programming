class ListNode {
  int? val;
  ListNode? next;
  //
  ListNode([this.val, this.next]);
}

ListNode? mergeTwoLists(ListNode? list1, ListNode? list2) {
  ListNode dummy = ListNode(0);
  ListNode tail = dummy;

  while (list1 != null && list2 != null) {
    if (list1.val! < list2.val!) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next!;
  }

  if (list1 != null) {
    tail.next = list1;
  } else {
    tail.next = list2;
  }

  return dummy.next;
}

void main() {
  ListNode? head;
  ListNode? second;
  ListNode? third;

  head = ListNode(1);
  second = ListNode(2);
  third = ListNode(3);

  head.next = second;
  second.next = third;
// print(second.val);

  // while (head != null) {
  //   print(head.val);
  //   head = head.next;
  // }
  ListNode? list1 = ListNode(1, ListNode(3, ListNode(5)));
  ListNode? list2 = ListNode(2, ListNode(4, ListNode(6)));

  ListNode? mergedHead = mergeTwoLists(list1, list2);

  while (mergedHead != null) {
    print(mergedHead.val);
    mergedHead = mergedHead.next;
  }
}
