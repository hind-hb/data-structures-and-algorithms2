from hashtab import __version__
import pytest
from hashtab.hash_tabel import HashTable

def test_version():
    assert __version__ == '0.1.0'
    
      
def test_add_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert len(hash_table.arr[hash_table.get_hash('hello')]) == 1
  
def test_get_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.get('hello') == 15

def test_contains_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.contains('hello')

def test_delete_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  hash_table.delete('hello')
  assert len(hash_table.arr[hash_table.get_hash('hello')]) == 0