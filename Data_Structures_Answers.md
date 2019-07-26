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


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
