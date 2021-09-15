#!/usr/bin/env python
# coding: utf-8

# ### Converting km/hr to m/hr and Vice versa

# In[1]:


def kmh_to_mph(x):
    return round(x * 0.621371, 2) # return to the nearest 2 decimal places

def mph_to_kmh(x):
    return round(1/ 0.621371 * x, 2) # return to the nearest 2 decimal places


# In[2]:


speed_km = float(input("What is the speed in km/hr?:"))
g = kmh_to_mph(speed_km)
print("The speed in miles/hr is {}".format(g))


# In[3]:


speed_m = float(input("What is the speed in miles/hr?:"))
g = mph_to_kmh(speed_m)
print("The speed in km/hr is {}".format(g))


# ### Converting km/hr to metres/sec and Vice versa

# In[4]:


def kmh_to_ms(x):
    return round(1/ 3.6 * x, 2) # return to the nearest 2 decimal places

def ms_to_kmh(x):
    return round(3.6 * x, 2) # return to the nearest 2 decimal places


# In[5]:


speed_ms = float(input("What is the speed in metres/s?:"))
g = ms_to_kmh(speed_ms)
print("The speed in km/hr is {}".format(g))


# In[6]:


speed_kmh = float(input("What is the speed in km/hr?:"))
g = kmh_to_ms(speed_kmh)
print("The speed in metres/sec is {}".format(g))

