# Challenge Summary
## Hashmap Repeated Word 
Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Whiteboard Process

![code-challange-31](https://user-images.githubusercontent.com/75991604/169700847-11e46755-2e16-4594-bfd7-40667d636957.png)

## Approach & Efficiency
Space : O(n)
Time : O(1)

## Solution

``` def first_repeated_word(str):
  if str == "":
    return 'Empty String'
  strs = re.sub(r'[^\w\s]','',str).lower().split(' ')
  hash_table = HashTable()
  for i in strs:
    if hash_table.contains(i):
      return i
    else:
      hash_table.add(i,1)
  return 'Nothing Repeated ..!'
  ```

## PR LInk :  [LINK](https://github.com/hind-hb/data-structures-and-algorithms2/pull/24/commits/c111aae269d46d8e8a49129a659c60869a935cb0)

