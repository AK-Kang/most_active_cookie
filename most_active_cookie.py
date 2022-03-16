#!/usr/bin/env python
# coding: utf-8

# In[21]:


import sys
import csv
import collections
import unittest


# In[22]:


def most_active_cookie(file, day):
    with open(file, 'r') as file:
        most_active = []
        activeness = -1
        dict_cookie = {}
        for i in file:
            cookie, time = i.split(",")
            date, _= time.split("T")
            if date == day:
                dict_cookie[cookie] += 1
                if len(most_active) == 0:
                    most_active = [cookie]
                    activeness = dict_cookie[cookie]
                else:
                    if dict_cookie[cookie] > activeness:
                        most_active = [cookie]
                        activeness = dict_cookie[cookie]
                    elif dict_cookie[cookie] == activeness:
                        most_active.append(cookie)
        for c in most_active:
            print(c)      
                    


# In[23]:


rows = [['AtY0laUfhglK3lC7', '2018-12-09T14:19:00+00:00'],
        ['SAZuXPGUrfbcn5UA', '2018-12-09T10:13:00+00:00'],
        ['5UAVanZf6UtGyKVS', '2018-12-09T07:25:00+00:00'],
        ['AtY0laUfhglK3lC7', '2018-12-09T06:19:00+00:00'],
        ['SAZuXPGUrfbcn5UA', '2018-12-08T22:03:00+00:00'],
        ['4sMM2LxV07bPJzwf', '2018-12-08T21:30:00+00:00'],
        ['fbcn5UAVanZf6UtG', '2018-12-08T09:30:00+00:00'],
        ['4sMM2LxV07bPJzwf', '2018-12-07T23:30:00+00:00']
       ]


# In[24]:


f = open('test_cookies.csv', 'w', newline='')
writer = csv.writer(f)
header = ["cookie", "timestamp"]
writer.writerow(header)
writer.writerows(rows)
f.close()


# In[25]:


class TestActiveCookie(unittest.TestCase):
    def test_single_active():
        retr = most_active_cookie('test_cookies.csv', '2018-12-09')
        assertEqual(retr[0], "AtY0laUfhglK3lC7")
        
    def test_multiple_actives():
        retr = most_active_cookie('test_cookies.csv', '2018-12-08')
        assertEqual(len(retr), 3)


# In[26]:


def main():
    command = sys.argv
    if len(command) == 4:
        most_active_cookie(command[1], command[3])
    else:
        print("Command Not Found.")


# In[ ]:




