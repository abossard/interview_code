from linked_list import LinkedList
from pprint import pprint

list = LinkedList()
list.append(3)
list.append('b')
list.append('v')
list.append(list)
list.append(0)
print(list.__unicode__())