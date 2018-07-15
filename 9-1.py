# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:36:11 2018

@author: win
"""

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('restaurant is :' + self.restaurant_name + "\ncuisine_type is :" 
              + self.cuisine_type)
        
    def open_restaurant(self):
        print('now is open')

#9-2        
my_restaurant = Restaurant('afufand','jxcc')
my_restaurant.describe_restaurant()
my_restaurant2 = Restaurant('afufand','shcc')
my_restaurant2.describe_restaurant()
my_restaurant3 = Restaurant('afufand','bjcc')
my_restaurant3.describe_restaurant()


#9-3
class User():
    def __init__(self,first_name,last_name,**infos):
        self.first_name = first_name
        self.last_name = last_name
        self.infos = infos
        self.login_attempts = 0
    
    def describe_user(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        print('login_attempts: ' + str(self.login_attempts))
        for key,value in self.infos.items():
            print(key + " : " +value)
    
    def grert_user(self):
        print('Hello ' + self.first_name + self.last_name)
        
    def increment_number_served(self):
        self.login_attempts += 1
    
    def rest_login_attempts(self):
        self.login_attempts = 0
        
z = User('z','bf',age='14')


z.describe_user()
#z.grert_user()
z.increment_number_served()
z.increment_number_served()
z.describe_user()








