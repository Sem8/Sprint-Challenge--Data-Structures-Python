Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
1 ans. I would say runtime complexity is O(3) because I'm just assigning a bunch of variables in if statements which takes O(1) time.
And since I've assigned 3 variables (3 times) it'll be O(1) + O(1) + O(1) = O(3). 

2. What is the space complexity of your ring buffer's `append` function?
2 ans. Space complexity may be O(c) because we need to assign space based on size of self.capacity here. Or more precisesly, O(c + 3) because
assigning variables also take O(1) space complexity and since I'm assigning 3 variables here. 

3. What is the runtime complexity of your ring buffer's `get` method?
3 ans. Runtime complexity would be O(n) because I have a for loop in the get method. 

4. What is the space complexity of your ring buffer's `get` method?
4 ans. Space complexity would be O(c) because again because we need to assign a certain amount of space, in this case length of self.capacity for this method, where the c is size of self.capacity.


5. What is the runtime complexity of the provided code in `names.py`?
5 ans. O(n^2) because there is a for loop within a for loop. 

6. What is the space complexity of the provided code in `names.py`?
6 ans. O(n) because to assign each duplicate name to the duplicates array we have to assign that many number of spaces. If all names in the two files were the same, in the worst case this would be O(n). Otherwise if all names are not the same, to be precise it would be O(n * (number of duplicates / total number of names)). 

7. What is the runtime complexity of your optimized code in `names.py`?
7 ans. O(2n) which reduces down to O(n) because two for loops are being used. 

8. What is the space complexity of your optimized code in `names.py`?
8 ans. O(2n + 2) which will reduce down to O(2n) or O(n). This is because I'm assigning extra space for the duplicates array which in the worst case where all names are duplicates will be assigned n number of spaces where n is the number of names which equates to O(n). Additionally I'm also assigning extra space for the names object or hash table which will hold all the names from names_1 array as keys. Since in worst case, n spaces are being assigned twice, once for array append and one for putting it into the names object it comes down to O(2n). And declaring a duplicates array and a names object takes up O(1) + O(1) space complexity thus, O(n) + O(n) + O(1) + O(1) = O(2n + 2)
