from _mystruct import ffi, lib

p1 = ffi.new('struct MyStruct*');

p1.a = 1;

print p1.a;
lib.ChangeStruct(p1, 10);
print p1.a;


