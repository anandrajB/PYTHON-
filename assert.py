batch = [ 40, 26, 39, 30, 25, 30] 
  

  
# using assert to check for temperature greater than cut 
for i in batch: 
    assert i >= 26, "Batch is Rejected"
    print (str(i) + " is O.K" ) 
'''
a = 4
b = 0
  
# using assert to check for 0 
print ("The value of a / b is : ") 
assert b != 0, "Divide by 0 error"
print (a / b) 
'''
