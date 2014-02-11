def add(a,b):
    print " %d + %d"%(a,b)
    return a + b

def subtract(a,b):
    print " %d - %d"%(a,b)
    return a-b

def multiply(a,b):
    print "%d * %d" % (a, b)
    return a * b

def divide(a,b):
    print " %d / %d"%(a,b)
    return a/b

print "Let's do some math wiith just functions!"

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "Age:%d,Height:%d,multiply:%d,iq:%d"%(age, height, weight, iq)

#A puzzle for the extra credit,type it in anyway
print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:",what,"Can you do it by hand ?"
