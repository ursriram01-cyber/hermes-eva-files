'''
Problem Description:
Description

Write a program to print from HIGH to LOW ignoring NUM

Input:
HIGH (Integer)
LOW (Integer)
NUM (Number to be ignored

For example:

5
1
3

5 4 2 1 
6
3
4
6 5 3 
10
8
7

10 9 8 
6
2
6

5 4 3 2 
Output
	INPUT	EXPECTED	GOT	
	
5
1
3
	
5 4 2 1
	
5 4 2 1
	
	
6
3
4
	
6 5 3
	
6 5 3
	
	
10
8
7
	
10 9 8
	
10 9 8
	
	
6
2
6
	
5 4 3 2
	
5 4 3 2
	

Passed all tests!  

Code
c
cpp
java
python3
perl
php
ruby
javascript
c#
golang
Blocks
Skip Quiz navigation
1
2
3
4
5
Finish attempt ...
1
2
3
4
5
6
7
8
high = int(input())
low = int(input())
num = int(input())
for i in range(high, low - 1, -1):
    if i != num:
        print(i, end=" ")
print()
Copy Code
Run Code
'''

high = int(input())
low = int(input())
num = int(input())

for i in range(high, low - 1, -1):
    if i != num:
        print(i, end=" ")
print()