import pytest
from linked_list.Linked import LinkedList, Node

# Test empty linked list
def test_is_empty_ll():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

# Test insert  values
def test_insert():
  ll = LinkedList()
  ll.insert(5)
  actual = ll.head.value
  assert actual == 5 

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(Node(5))
    ll.insert(Node(1.33))
    ll.insert(Node("Python"))
    ll.includes(Node(5))== True 
    ll.includes(Node(1.33))== True 
    ll.includes(Node(7))== False

    return 

