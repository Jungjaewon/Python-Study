

def list_change(a):

    b = [4,5,6]
    #print a, id(a), id(b), 'in function before assign'
    a = b
    print a, id(a), id(b),'in function'

def list_change1(a):

    print a , id(a), 'in function before assign'
    a[0] = 4
    a[1] = 5
    a[2] = 6
    print a ,'in function'

def list_change2(a):

    b = [4,5,6]

    print a , id(a), id(b), 'in function before assign'
    a.append(1)
    a = b
    print a , id(a),'in function'

if '__main__' == __name__:

    a = [1,2,3]
    print a, id(a), 'in main'
    list_change(a)
    print ''
    print a, id(a), 'in main'
    #print a,'in main'
    print ''
    #list_change1(a)
    print a, id(a), 'in main'
    #list_change2(a)
    #print a, 'in main'