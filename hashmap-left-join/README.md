# Code Challenge 33 : Hashmap Left Join
  
  
## Challenge Summary
  * Write a function called left join.
  
  * Arguments: two hash maps.
    - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
  
  * Return: The returned data structure that holds the results like that -> 
    - Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
    -  LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
    - If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
  
## Whiteboard Process
![code-challange-33](https://user-images.githubusercontent.com/75991604/170965234-a002bf5c-33a0-4c69-86c8-9e04d84cb379.png)


## Approach & Efficiency
  * Time: O(n)
  * Space: O(n)
  
## PR :[LINK](https://github.com/hind-hb/data-structures-and-algorithms2/pull/27/commits/8d2b282d913d7400c4d9a7145cf264624e205f04)
