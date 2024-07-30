import sys

# Function to get the size of an object in bytes
def get_memory_size(obj):
    return sys.getsizeof(obj)

# Test objects
integer_obj = 42
string_obj = "Hello, World!"
list_obj = [1, 2, 3, 4, 5]
dict_obj = {"name": "Alice", "age": 30}
custom_obj = get_memory_size  # Example of a function object

# Get memory sizes
integer_size = get_memory_size(integer_obj)
string_size = get_memory_size(string_obj)
list_size = get_memory_size(list_obj)
dict_size = get_memory_size(dict_obj)
custom_size = get_memory_size(custom_obj)

# Print results
print(f"Memory size of integer object: {integer_size} bytes")
print(f"Memory size of string object: {string_size} bytes")
print(f"Memory size of list object: {list_size} bytes")
print(f"Memory size of dictionary object: {dict_size} bytes")
print(f"Memory size of custom function object: {custom_size} bytes")


# Python generally occupies more memory space than C for several reasons:

# 1. Abstraction Levels:
# Python: It is a high-level language that abstracts many details of the system. This abstraction layer adds overhead. Python objects are more complex, containing additional metadata, such as type information, reference counts, and other interpreter-related data.
# C: It is a low-level language with direct access to memory and hardware. C programs typically manage memory manually, allowing for fine-tuned control and optimizations.
# 2. Garbage Collection:
# Python: Uses automatic garbage collection, which requires additional data structures and overhead to keep track of object lifetimes.
# C: Does not have built-in garbage collection; memory management is manual, leading to less overhead but more responsibility on the programmer to avoid memory leaks and other issues.
# 3. Dynamic Typing vs. Static Typing:
# Python: Dynamically typed, meaning variables can hold any type of object, and type checking is done at runtime. This flexibility requires additional memory to store type information and perform type checks.
# C: Statically typed, with types determined at compile-time. This results in more efficient use of memory as the compiler optimizes storage based on fixed types.
# 4. Interpreter Overhead:
# Python: Executed by an interpreter, which introduces overhead. The interpreter itself requires memory to store and execute the bytecode, manage the execution environment, and handle runtime tasks.
# C: Compiled directly to machine code, which can be executed directly by the hardware, resulting in minimal overhead.
# 5. Memory Management:
# Python: Uses a heap to store objects and employs memory management techniques like reference counting and garbage collection, which add to memory usage.
# C: Gives direct control over memory allocation and deallocation, allowing for potentially more efficient memory use, but also making it easier to make mistakes such as buffer overflows and memory leaks.