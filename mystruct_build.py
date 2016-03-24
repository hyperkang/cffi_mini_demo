import cffi
ffi = cffi.FFI()

lib = ffi.set_source("_mystruct",
    """
        #include "mystruct.h"
    """,
    libraries=["mystruct"],
    library_dirs=["./clib"],
    include_dirs=["./clib"]
)

ffi.cdef("""
struct MyStruct {
   int a;
   double b;
};


void ChangeStruct(struct MyStruct* p, int a);
"""
)


if __name__ == "__main__":
    ffi.compile()

