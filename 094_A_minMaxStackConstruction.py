# --------------------------------------------
# Problem Statement:
# --------------------------------------------
# Implement a special type of stack called "MinMaxStack".
# Unlike a normal stack which only supports:
#   - push (add element to top)
#   - pop (remove element from top)
#   - peek (see the top element without removing it)
#
# MinMaxStack must also support:
#   - getMin() -> Returns the minimum value in the stack at any point.
#   - getMax() -> Returns the maximum value in the stack at any point.
#
# The challenge:
# Normally, to find min or max, we would scan the entire stack (O(n)).
# But here we want O(1) time (constant time) for min and max lookups.
#
# --------------------------------------------
# Code Execution Theory (How it works):
# --------------------------------------------
# To achieve O(1) min and max:
# - We maintain two stacks:
#   1. self.stack -> stores all values as in a normal stack.
#   2. self.minMaxStack -> stores a dictionary for each value pushed,
#      keeping track of the min and max so far at that point.
#
# Example:
# If we push: [5, 2, 7, 1]
# self.stack = [5, 2, 7, 1]
# self.minMaxStack =
#   [
#     {'min': 5, 'max': 5},        # after pushing 5
#     {'min': 2, 'max': 5},        # after pushing 2
#     {'min': 2, 'max': 7},        # after pushing 7
#     {'min': 1, 'max': 7}         # after pushing 1
#   ]
#
# Now at any time:
#   - Top element in stack is current element.
#   - Top element in minMaxStack gives min and max instantly.
#
# --------------------------------------------
# Corrected + Commented Code
# --------------------------------------------

class MinMaxStack:
    def __init__(self):
        # main stack that holds actual values
        self.stack = []
        # auxiliary stack that holds min and max at each level
        self.minMaxStack = []

    def peek(self):
        # return the top element of the stack without removing it
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # remove the top element from both stacks
        self.minMaxStack.pop()
        value = self.stack.pop()
        #  important debug print: show state after pop
        print(f"After pop({value}) -> stack: {self.stack}, minMaxStack: {self.minMaxStack}")
        return value

    def push(self, number):
        # create a new dictionary with min and max as the new number
        newMinMax = {"min": number, "max": number}

        # if stack already has elements, update min and max
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)

        # push updated min and max to minMaxStack
        self.minMaxStack.append(newMinMax)
        # push actual number to stack
        self.stack.append(number)

        # 🔑 important debug print: show state after push
        print(f"After push({number}) -> stack: {self.stack}, minMaxStack: {self.minMaxStack}")

    def getMin(self):
        # return the min value from top dictionary in minMaxStack
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        # return the max value from top dictionary in minMaxStack
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


# --------------------------------------------
# Dummy Data Example:
# --------------------------------------------
stack = MinMaxStack()
stack.push(5)   # stack = [5], minMaxStack = [{'min':5, 'max':5}]
stack.push(2)   # stack = [5,2], minMaxStack = [{'min':5,'max':5}, {'min':2,'max':5}]
stack.push(7)   # stack = [5,2,7], minMaxStack = [{'min':5,'max':5}, {'min':2,'max':5}, {'min':2,'max':7}]
stack.push(1)   # stack = [5,2,7,1], minMaxStack = [{'min':5,'max':5}, {'min':2,'max':5}, {'min':2,'max':7}, {'min':1,'max':7}]

print("Peek:", stack.peek())  # should return 1
print("Min:", stack.getMin()) # should return 1
print("Max:", stack.getMax()) # should return 7

stack.pop()  # removes 1
print("After pop -> Min:", stack.getMin()) # should return 2
print("After pop -> Max:", stack.getMax()) # should return 7



#  Practical applications of MinMaxStack: 
# 🏦 Example 1: Banking / Finance (Industry Equivalent Scenario)
#
# Real-time Application Scenario:
# Imagine you are building a mobile banking app that shows a customer:
# - Their last 10 transactions (like a stack: newest on top)
# - The minimum transaction amount (e.g., smallest debit) instantly
# - The maximum transaction amount (e.g., largest credit) instantly
#
# ➡ Without MinMaxStack, to find min/max you'd scan all 10 transactions each time
# ➡ With MinMaxStack, you just peek the minMaxStack top in O(1) time
#
# Problem Statement (Banking Version):
# Design a transaction stack for a banking app where the system can push new transactions, 
# pop old transactions, peek the most recent one, and instantly get the minimum and maximum 
# transaction values in real time
#
# Why this matters in industry?
# - Customer dashboard needs instant insights
# - Backend load should stay low (constant time instead of scanning)
# - Ensures scalability as millions of users do transactions simultaneously

# 🛒 Example 2: E-Commerce (Price Tracking)
#
# Scenario:
# You're tracking product price changes over time
# Each new price is pushed into a stack
# Customers want to instantly know:
# - The highest price (max) in last 30 days
# - The lowest price (min) in last 30 days
#
# ➡ MinMaxStack solves this instantly, instead of re-scanning 30 days of prices
#
# Problem Statement (E-Commerce Version):
# Design a price history tracker for an online store that supports instant queries of 
# min and max price within a rolling window of recent price updates