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
    ll=LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert_after(7,1)
    assert ll.head.next.value ==1

def test_kthFromEnd():
    ll = LinkedList()
    node1 = ll.insert("hind")
    ll.head == node1
    ll.insert("ahmad")
    ll.insert("hbashneh")
    expected = ll.kthFromEnd(2)
    assert expected.value == "hbashneh"

def test_k_less_than_zero():
    ll = LinkedList()
    node1 = ll.insert("hind")
    ll.head == node1
    ll.insert("ahmad")
    ll.insert("hbash")
    expected = ll.kthFromEnd(-1)
    assert expected == "Error - input value is less than 0"

def test_is_one():
    ll = LinkedList()
    node1 = ll.insert("hind")
    ll.head == node1
    expected = ll.kthFromEnd(1)
    assert expected.value == "hind"

def test_k_middll():
    ll = LinkedList()
    node1 = ll.insert("hind")
    ll.head == node1
    ll.insert("ahmad")
    ll.insert("hbash")
    expected = ll.kthFromEnd(1)
    assert expected.value == "ahmad"

def test_zip():
    newList = LinkedList()
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    list1 = LinkedList()
    list1.insert(2)
    list1.insert(4)
    list1.insert(6)
    list2 = LinkedList()
    list2.insert(1)
    list2.insert(3)
    list2.insert(5)
    expected = newList.zip_list(list2, list1)
    actual = '{1}->{2}->{3}->{4}->{5}->{6}->NULL'
    expected ==  actual

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
    assert str(ll.kthFromEnd("Python")) == 0


    return 

