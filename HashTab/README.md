# Code Challenge 30 Hash Table

## Hash Table
  * It is a data structure that implements an associative array abstract data type, a structure that can map keys to values(This means every Node or Bucket has both a key, and a value). A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
  
## Challenge Summary
  * Implement a Hashtable with the following methods:
    * add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    * get: takes in the key and returns the value from the table.
    * contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
    * hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
  * Time: O(1)
  * Space: O(1)
  * Worst case: O(n)

## API
  * Add(): When adding a new key/value pair to a hashtable.
  * Find():takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.
  * Contains() : The Contains method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the GetHash and check the hashtable if the key exists in the table given the index returned.
  * GetHash(): The GetHash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.
  
## PR : [LINK](https://github.com/hind-hb/data-structures-and-algorithms2/pull/23/commits/1384d0762a6368722119b839f34b58dd6664eb7a)
