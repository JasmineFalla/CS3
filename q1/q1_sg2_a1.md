
Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9-Samat             Score:____________

C24 / Name: Jasmine Kaylee M. Falla         Date: 8/16/2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The PSHS school canteen is small and often gets crowded during lunch break.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Some students take too long to decide what to order.

2. The cashier has to manually calculate totals and give change.

3. There is no system to track which food items are running out.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

1. Some students take too long to decide what to order.

- CT Skill: Algorithm
- Example Solution: Create a digital menu that displays the available food items and their prices. Students can browse the menu and choose what they want before going to the canteen, which reduces the time they spend deciding what to order. 
- Algorithm makes ordering faster by giving students a way to choose what to order beforehand.

2. The cashier has to manually calculate totals and give change.

- CT Skill: Algorithm
- Example Solution: Create a digital system that allows the cashier to select the items purchased and automatically calculate the total cost. After entering the amount paid, the system calculates and displays the correct change. 
- Algorithm makes transactions faster by giving the system instructions on how to automatically calculate and display the total and change.

3. There is no system to track which food items are running out.

- CT Skill: Algorithm 
- Example Solution: Create a digital system that records the quantity of each item. Whenever an item is sold, its quantity reduces automatically. The system can also notify the cashier when an item needs to be restocked. 
- Algorithm prevents stock problems by giving the system instructions on how to automatically update an item's quantity and notify the cashier when an item needs to be restocked.

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
Sub-Problem: The cashier has to manually calculate totals and give change.
CT Skill: Algorithm


Pseudocode:
START

Display the available food items and their prices.

Set Total Cost = 0.

REPEAT
    Cashier selects a food item.
    Cashier enters the quantity purchased.
    Calculate Item Cost = Price × Quantity.
    Add Item Cost to Total Cost.

    Ask cashier if another item needs to be added.
UNTIL the answer is NO.

Display Total Cost.

Cashier enters the amount of money received from the customer.

IF Amount Received >= Total Cost THEN
    Change = Amount Received - Total Cost.
    Display Change.
    Display "Transaction complete."
ELSE
    Display "Insufficient payment."
    Cashier enters the amount received again.
END IF

END
