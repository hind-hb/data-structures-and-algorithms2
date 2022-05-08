from Fizz_buzz import Node, binary_tree, FizzBuzzTree



def test_fizzbuzz():
    bt = binary_tree()
    bt.root = Node(12)
    bt.root.left = Node(15)
    bt.root.right = Node(5)
    bt.root.left.right = Node(6)
    bt.root.left.left = Node(8)
    bt.root.right.right=Node(9)
    bt.root.right.right.left=Node(4)
    bt.root.left.left.right=Node(5)
    bt.root.left.right.left = Node(11)
    expected = ['Fizz','FizzBuzz','8','Buzz','Fizz','11','Buzz','Fizz','4']
    actual = FizzBuzzTree(bt)
    assert expected == actual