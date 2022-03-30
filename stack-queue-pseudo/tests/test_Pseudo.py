from stack_queue_pseudo.stackQueuePesudo import Node , Stack , PseudoQueue


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


def test_enqueue_dequeue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(8)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 5