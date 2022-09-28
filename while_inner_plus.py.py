#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1

#find deepest list
def deepest_lists(while_list):
    lst_ind = [item for item in while_list if isinstance(item, list)]
    if len(lst_ind) == 0:
        return lst_ind[0]
    if all(isinstance(item, int) for while_list in lst_ind for item in while_list):
        return lst_ind[0]
    return deepest_lists([item for while_list in lst_ind for item in while_list])

while_list = [1,2,3,4,[5,6,7,[8,9]]]

deepest_lists(while_list)

#add 1 to the integers in the deepest list
newlist_1=[]
thislist = deepest_lists(while_list)
i = 0
while i < len(thislist):
    a=thislist[i]+1
    newlist_1.append(a)
    i = i + 1

print(newlist_1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




