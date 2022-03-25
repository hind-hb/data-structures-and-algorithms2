from stackqueue.stack_and_queue import Node , Stack ,Queue
import pytest

def test_push_stack ():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.top.value
  expected = 6
  assert actual == expected 

def test_pop_stack ():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.pop()
  expected = 6
  assert actual == expected 

def test_peek_stack():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.peek()
  expected = 6
  assert actual == expected 

def test_isEmpty():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected


def test_enqueue():
  queue = Queue()
  queue.enqueue("hind")
  queue.enqueue("ahmad")
  queue.enqueue("hbashneh")

  actual = queue.rear.value
  expected = "hbashneh"
  assert actual == expected

def test_dequeue():
  queue = Queue()
  queue.enqueue("hind")
  queue.enqueue("ahmad")
  queue.enqueue("hbashneh")

  actual = queue.front.value
  expected = "hind"
  assert actual == expected

def test_peek_queue():
  queue = Queue()
  queue.enqueue("hind")
  queue.enqueue("ahmad")

  actual = queue.front.value
  expected = "hind"
  assert actual == expected

def test_isEmpty_queue():
  queue = Queue()
  actual = queue.isEmpty_queue()
  expected = True
  assert actual == expected
