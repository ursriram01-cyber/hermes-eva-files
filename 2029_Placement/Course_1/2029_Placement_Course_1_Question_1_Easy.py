'''
Problem Description:
Description

Write a program to display each digit separately in a given number

For example:

341

3
4
1

56420
5
6
4
2
0

Output
	INPUT	EXPECTED	GOT	
	
341
	
3
4
1
	
3
4
1
	
	
56420
	
5
6
4
2
0
	
5
6
4
2
0
	

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
number = input()
for digit in number:
    print(digit)
Run Code
'''

number = input()
for digit in number:
    print(digit)