
### Problem1.py ###

####################
# Project Euler
#
# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
####################

def appendUniqueMultiples(multiList, multiple, upperLimit):
  i = 1
  
  while i * multiple < upperLimit:
    if multiList.count(i * multiple) == 0:
      multiList.append(i * multiple)
    i += 1
  return multiList

def addMultiples(curList):
  i = 0
  n = 0
  
  for i in range(len(curList)):
    n += curList[i]
   
  return n

multiples = []
appendUniqueMultiples(multiples, 3, 1000)
appendUniqueMultiples(multiples, 5, 1000)
  
print addMultiples(multiples)