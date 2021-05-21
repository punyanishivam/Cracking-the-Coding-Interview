import Linked Lists
def removeDuplicates(self):
  current = self.head
  while temp is not None:
    runner = current
    while runner.next is not None:
      if runner.next.data = current.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    current = current.next
