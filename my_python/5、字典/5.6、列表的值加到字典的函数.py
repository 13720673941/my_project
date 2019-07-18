# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/14 20:02


# fruits = {"apple": 10,"banana": 20,"orange": 30}

def displayInventory(inventory):

    print("Inventory:")

    item_total = 0

    for k,v in inventory.items():

        print(str(v) + " " + k)

        item_total += v

    # print("Total number of items: " + str(item_total))

# displayInventory(fruits)

def addToInventory(inventory,addedItems):

    # 遍历列表

    for value in addedItems:

        # setdefault() 方法如果该值在字典中返回 该字段中的值，如果该值不再字典中返回 0

        inventory.setdefault(value,0)

        # 如果该值该字典中的值 + 1，如果不存在该值，就初始化为 0 ，加上 1

        inventory[value] = inventory[value] + 1

    return inventory



inv = {"apple":10,"banana":10}

dragonLoot = ["apple", "apple", "orange", "banana", "banana", "banana"]

inv1 = addToInventory(inv,dragonLoot)

displayInventory(inv1)

