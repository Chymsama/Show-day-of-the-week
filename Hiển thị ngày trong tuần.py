#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = int(input("Nhập một số từ 1 đến 7: "))

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("error, out of range")

