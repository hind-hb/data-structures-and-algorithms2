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
    ss = PseudoQueue()
    ss.enqueue("hind")
    ss.enqueue("ahmad")
    ss.dequeue()
    ss.enqueue("hbashneh")
    ss.dequeue()
    expected = ss.stack2.top.value
    assert expected == "hbashneh"