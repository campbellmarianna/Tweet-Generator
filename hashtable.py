#!python

from linkedlist import LinkedList

# jumping to the right LinkedList using the hash code is the key feature of a Hash Table
class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self): # magic method # method
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(b + n) for b buckets in the LinkedList because we have to iterate over all b buckets, iterate over all the n nodes and append the key for each"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(b + n) for b buckets in the LinkedList because we have to iterate over all b buckets, iterate over all the n nodes and append the value for each"""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Best and worst case running time: O(n) for n buckets in the array
        because we always need to loop through all n buckets to get there items."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) for n LinkedList in the array because we have to iterate over all n LinkedList and get the length for each"""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets: # b iterations
            count += bucket.length() # 0(l)
        return count
        # Overall: 0(b * l) --> 0(n)


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n + i) for n nodes in the LinkedList because we have to iterate over all n nodes, iterate over all the i items and check to see whose data matches the given key """
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)

        # Check out the entry that was returned - is it None?
        if entry is None:
            return False
        else: # entry is not None
            return True
        # Shorter version:
        # return (entry is not None)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n + i) for n nodes in the LinkedList because we have to iterate over all n nodes, iterate over all the i items and check to see whose data matches the given key"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)] # 0(1) to calculate index
        # the lambda is a closure because it is cpaturing around a function in the outer scope ()
        entry = bucket.find(lambda key_value: key_value[0] == key) # 0(1) to index an array
        # Check if key-value entry exists in bucket
        if entry is not None: # Found entry
            # If found, return value associated with given key
            return entry[1] # entry = (key, value)
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n + i) for n nodes in the LinkedList because we have to iterate over all n nodes, iterate over all the i items and check to see whose data matches the given key In class: Best case O(1) item is located near head of list. Otherwise O(l) (find) + O(l) (delete) = O(2*1) simplifies to O(l) if item is near tail of list"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        bucket_entry = bucket.find(lambda key_value: key_value[0] == key)
        new_entry = (key, value)
        # Check if key-value entry exists in bucket
        if bucket_entry is not None: # Found entry
            bucket.delete(bucket_entry) # O(l) in worst case
        bucket.append(new_entry)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n + i) for n nodes in the LinkedList because we have to iterate over all n nodes, iterate over all the i items and check to see whose data matches the given key"""
        # Find bucket where given key belongs
        index = self._bucket_index(key) # 0(1) #very fast mutiple the index by # array method 0(1)
        bucket = self.buckets[index] #0(1)
        bucket_entry = bucket.find(lambda key_value: key_value[0] == key) # 0(l)
        # Check if key-value entry exists in bucket
        if bucket_entry is not None:
            bucket.delete(bucket_entry) # 0(l) # If found, delete entry associated with given key # delete method is scoped to LinkedList object
        else: # Otherwise, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key)) # Hint:
        # Overall 0(3 + 2l) --> 0(l)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
