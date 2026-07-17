/*
Problem Description:
Description

Create an arraylist aL1 and perform the following operations.

Add elements 65, 32, 56 ,78, 96, 124
Remove the element at the index 4.
Add 45 at the index 2.
Check whether 78 is present in aL1. If yes, Print “True” Otherwise “False”
Print the ArrayList aL1.

Output
	TEST	EXPECTED	GOT	
	
/*TC 1*/
	
True
[65, 32, 45, 56, 78, 124]
	
True
[65, 32, 45, 56, 78, 124]
	

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
6
7
8
Finish attempt ...
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
import java.util.ArrayList;
import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> aL1 = new ArrayList<>();
        aL1.add(65);
        aL1.add(32);
        aL1.add(56);
        aL1.add(78);
        aL1.add(96);
        aL1.add(124);
        aL1.remove(4);
        aL1.add(2, 45);
        if (aL1.contains(78)) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
 
Run Code
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> aL1 = new ArrayList<>();

        aL1.add(65);
        aL1.add(32);
        aL1.add(56);
        aL1.add(78);
        aL1.add(96);
        aL1.add(124);

        aL1.remove(4);

        aL1.add(2, 45);

        if (aL1.contains(78)) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

        System.out.println(aL1);

        scanner.close();
    }
}