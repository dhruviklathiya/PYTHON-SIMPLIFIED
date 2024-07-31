# Important concept: Destroying of object
    # In Python, objects are destroyed by the garbage collector when they are no longer needed, specifically when there are no more references to them.

# There is no need to use del keyword for deleting objects,
    # Objects are auto deleted when they go out of scope

# * Reference Counting
# Python primarily uses a technique called reference counting for memory management. Each object maintains a count of the number of references pointing to it. When this count drops to zero, it means there are no references to the object, and it can be safely destroyed.

# * Garbage Collection
# In addition to reference counting, Python also has a garbage collector that handles cyclic references (where two or more objects reference each other). The garbage collector periodically searches for and collects such cyclic references to free up memory.

# * Object Destruction
# When an object’s reference count drops to zero, its destructor method (__del__) is called (if it exists). This allows you to define any cleanup operations that should be performed before the object is destroyed.

# Previously covered topic: * Python integer caching
# In Python, integer caching is an optimization technique that pre-allocates and reuses a range of small integer objects. This mechanism helps improve performance and memory usage, especially for frequently used integers.

# * Python memory: In short python takes up more memory than it should as compare to C language because python is dynamic.