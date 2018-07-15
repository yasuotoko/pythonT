# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 13:40:17 2018

@author: win
"""
from import_t import make_album

#8-1
def display_message():
    print('this is a message')
    
display_message()

#8-2
def favourite_book(title1):
    print('One of my favourite book is '+ title1.title())

favourite_book('Alice in Wonderland')


#8-3
def make_shirt(size,word):
    print('shirt size is :'+size+", word is :" + word)
    
make_shirt('s','disneland')

#8-4
def make_shirt2(size,word='I love Python'):
    print('shirt size is :'+size+", word is :" + word)
    
make_shirt2('S')

make_shirt2('S','I love too')

#8-5
def descirbe_city(c_name,c='Iceland'):
    print(c_name + ' is in ' + c)

descirbe_city('Reykjavik')
descirbe_city('dadaa')
descirbe_city('chongq','china')

#8-6
def city_country(city,country):
    return city.title()+','+country.title()

print(city_country('santiago','chile'))

#8-7
print(make_album('jay','ylxx','14'))

#8-9
magicList = ['zzz','ccc','fff','rrr']

def show_magicians(magicList):
    for magic in magicList:
        print(magic)

show_magicians(magicList)

#8-10
'''
def make_great(magicList):
    for magic in range(0,len(magicList)):
        magicList[magic] = 'the Great' + magicList[magic]

make_great(magicList)
show_magicians(magicList)
'''

#8-11
def make_great(magicList):
    for magic in range(0,len(magicList)):
        magicList[magic] = 'the Great ' + magicList[magic]
    show_magicians(magicList)

make_great(magicList[:])
show_magicians(magicList)

#8-12
def make_sandwich(*topping):
    print('sandwich:')
    for top in topping:
        print(top)
make_sandwich('sada','agg')
make_sandwich('agg')
make_sandwich('huotui','dadadadadadad','dadadad')
    

#8-14
def make_car(brand,ty,**infos):
    car = {}
    car['brand'] = brand
    car['type'] = ty
    for key,value in infos.items():
        car[key] = value
    return car

car = make_car('subaru','outback',color='blue',tow_package=True)

print(car)
















