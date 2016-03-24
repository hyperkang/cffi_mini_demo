# A mini demo for [cffi](http://cffi.readthedocs.org/) - API level, out-of-line

# Demo environment
  - Ubuntu 14.04.4 LTS
  - GCC 4.8.2
  - CPython 2.7.6(with cffi 1.5.2), pypy 5.0.1 (with built-in cffi)


# Demo steps:

## 1. Create a C static lib
   - Implement a simple function as: `int mysum(int a, int b)` in `./clib/mysum.c`
   - Complie mysum.c into static lib `libmysum.a`
     ```
     cd clib
     gcc -c mysum.c
     ar -crv libmysum.a mysum.o
     ```
     
   - Write a testing program in C to link with `libmysum.a`
      - Build testing executable from `clib/test_mysum.c`
      
        ```
        gcc ./test_mysum.c -lmysum -L./
        ```
      - Run it (You should see `1+2=3` printed)
      
        ```
        ./a.out
        ```

## 2. Run cffi build script to generate python extension
   - With pypy
     ```
     cd ..
     [path]/pypy ./mysum_build.py
     ```
     File `_mysum.pypy-41.so` should be generated at current directory which can be imported by python code;
     
   - With CPython
     ```
     cd ..
     [path]/python ./mysum_build.py
     ```
     File `_mysum.so` should be generated at current directory which can be imported by python code;
     

## 3. Test generated extension
   - With pypy
   
     ```
     [path]/pypy ./test_mysum.py
     ```
   - With CPython
   
     ```
     [path]/python ./test_mysum.py
     ```
  
   You should get `1+2=3` printed.
