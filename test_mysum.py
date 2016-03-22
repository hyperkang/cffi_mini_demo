from _mysum import ffi, lib

a = 1
b = 2
print '%d+%d=%d' % (a, b, lib.mysum(1,2))


