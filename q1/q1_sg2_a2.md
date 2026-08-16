Annex C
Code Quality Assessment Worksheet

Section: 9-Samat   Score:

C24 / Name: Jasmine Kaylee M. Falla  Date: 8/16/2026
Groupmates: Kayle Doculan, Miel Evangelista


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

PseudoCode 2

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm



Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- PseudoCode 1 is faster and more efficient because it uses only one loop, while PseudoCode 2 uses two nested loops.

2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- PseudoCode 1 is easier to understand because it uses meaningful variable names, simpler logic, and fewer lines of code.

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- PseudoCode 1 would be easier to update because its structure is more sraightforward and adding new steps is less likely to cause errors or break the code.

4. Testability
Which algorithm is easier to test with different inputs? Why?
- PseudoCode 1 is easier to test with different inputs because it works with small lists easily, has fewer conditions to check, and produces a predictable and clear output.

5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- The algorithm should check if the list is empty, reject invalid inputs, and avoid crashing when inputs are unusual to avid errors or misuse.

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
- The better algorithm is PseudoCode 1 because its more shorter, faster, and easier to understand, maintain, and test.
