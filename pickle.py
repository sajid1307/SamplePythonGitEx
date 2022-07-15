import pickle

mylist = ['a', 'b', 'c', 'd']

with open('abc.txt', 'wb') as fh:
    pickle.dump(mylist, fh)