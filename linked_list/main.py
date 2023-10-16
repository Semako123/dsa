from linked_list import LinkedList

ll = LinkedList()

ll.push_back(2)
ll.push_back(4)
ll.push_back(6)
ll.push_back(8)
ll.push_back(10)

print(ll)

ll.pop_front()

print(ll)

ll.pop_front()
ll.pop_front()

print(ll)

print(ll.front())
print(ll.back())

ll.insert(1, 50)

print(ll)

ll.insert(2, 100)

print(ll)
