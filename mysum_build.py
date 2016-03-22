import cffi
ffi = cffi.FFI()

lib = ffi.set_source("_mysum",
    """
        #include "mysum.h"
    """,
    libraries=["mysum"],
    library_dirs=["./clib"],
    include_dirs=["./clib"]
)

ffi.cdef("""
    int mysum(int a, int b);
"""
)


if __name__ == "__main__":
    ffi.compile()

