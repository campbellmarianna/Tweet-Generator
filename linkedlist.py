#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        Running time: 0(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) for n nodes in the list because we have to iterate over all n nodes and count 1 for each"""
        return self.size
        count = 0 # create count set it to 0
        node = self.head # set node to self.node
        # Loop through all nodes and count one for each
        while node is not None: # loop through nodes
            count += 1 # increment cout by one
            node = node.next

        return count # return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) we only change the tail node."""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        # if self.tail is not None: #if the last node has data
        #     self.tail.next = new_node # set new node after the last node
        # else: # if the tail doesn't have data
        #     self.head = new_node #self.head = new_node # set the head node to the new node
        # self.tail = new_node # in any case the new node will be the last node
        if self.head is None: # check if head is None
            self.head = new_node # set head to new node
            self.tail = new_node # set tail to new node
        else: # otherwise
            self.tail.next = new_node # set tail next to new_node
            self.tail = new_node # set tail to tail next
        # try:
        #     self.tail
        # except NameError:
        #     print("Well, it was not defined after all!")
        # else:
        #     print("Sure, it was defined.")

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because we ony change the first node and never loop through all nodes."""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head is None: # check if head is None
            self.head = new_node # set head to new node
            self.tail = new_node # set tail to new node
        else: # otherwise
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # def quality(self, item):
    #     if item < 1:
    #         return True
    #     else:
    #         return False1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(n)and worst case running time: O(n) if the item is near the tail of the list or not present and we need to loop through all n nodes in the list."""
        # Loop through all nodes to find item where quality(item) is True
        node = self.head # 0(1)
        while node is not None: # O(n)
            if quality(node.data): # Check if node's data satisfies given quality function # O(1)
                return node.data # O(1)
            else: # O(1)
                node = node.next # O(1)
        return None # O(1)
        # Overall: 0(n)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Running time: O(1) because we ony check if the first node isn't none then do further checks to see whose data matches the given item. """
        # Update previous node to skip around node with matching data
        current_node = self.head             # Inspired by Jackson Ho
        previous_node = None
        found = False
        # Loop through all nodes to find one whose data matches given item
        while current_node:
            if self.head.data == item:
                if self.head.next is not None: # if there is an item after the head
                    self.head = self.head.next
                    found = True
                    break
                else:
                    self.head = None
                    self.tail = None
                    found = True
                    break

            elif current_node.data == item:
                if current_node == self.tail:
                    previous_node.next = None
                    self.tail = previous_node
                    found = True
                    break
                else:
                    previous_node.next = current_node.next
                    found = True
                    break
            else:
                previous_node = current_node
                current_node = current_node.next
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if not found:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
