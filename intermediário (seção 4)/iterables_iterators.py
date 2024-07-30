iterable = ['eu','tenho','_iter_']

#iterator = iterable.__iter__()
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))

