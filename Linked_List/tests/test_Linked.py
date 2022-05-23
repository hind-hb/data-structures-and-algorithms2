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


def test_insert_before():
    ll = LinkedList()
    A = Node("java")
    ll.append(A)
    ll.insert_before("java", 'Python')
    assert ll.head.value == 'Python'



def test_insert_After():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    li.insert_after(7,1)
    assert li.head.next.value==1

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(Node(5))
    ll.insert(Node(1.33))
    ll.append(Node("Python"))
    ll.includes(Node(5))== True 
    ll.includes(Node(1.33))== True 
    ll.includes(Node(7))== False
    ll.insert_after(Node(1.33,"a"))
    ll.insert_before(Node(5,"e"))


    return 

