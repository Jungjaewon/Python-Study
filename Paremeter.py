def print_param(*args):
    print args
    for p in args:
        print p


def print_param2(**kwargs):
    print kwargs
    print kwargs.keys()
    print kwargs.values()

    for name, value in kwargs.items():
        print "%s : %s" % (name, value)


def print_param3(*args, **kwargs):
    print args
    print kwargs


print_param3('a', 'b')
# ('a', 'b')
# {}

print_param3(third='c', fourth='d')
# ()
# {'fourth': 'd', 'third': 'c'}

print_param3('a', 'b', third='c', fourth='d')
# ('a', 'b')
# {'fourth': 'd', 'third': 'c'}


print_param2(first='a', second='b', third='c', fourth='d')

# {'second': 'b', 'fourth': 'd', 'third': 'c', 'first': 'a'}
# ['second', 'fourth', 'third', 'first']
# ['b', 'd', 'c', 'a']
# second : b
# fourth : d
# third : c
# first : a

print_param('a', 'b', 'c', 'd')
# ('a', 'b', 'c', 'd')
# a
# b
# c
# d


# from http: // jhproject.tistory.com / 109[JHPROJECT]