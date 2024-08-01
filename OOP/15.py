# Encapsulation:
    # In simple words, grouping together of variables, and functions that are related
    # Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class.

# Abstraction:
    # In simple words, using functions and methods without worrying about what is running underneath
    # Abstraction is a core concept in object-oriented programming (OOP) that deals with hiding the complex implementation details and showing only the essential features of an object. It enables developers to work with high-level concepts without needing to understand the intricacies of how those concepts are implemented.

# Example of abstraction:
_list = [12,3,4,53,6]
_list.sort()
    # There are alot of sorting algorithms:
                                        # Quick sort
                                        # Merge sort
                                        # Heap sort
                                        # Bubble sort
                                        # Insertion sort
    # Pyhton is running sort method but we have no idea which sort is being run
        # For knowledge: Python uses Timsort algorithm for sorting list
print(_list)

# We must encapsulate functions and variable together for using abstraction
# By default access modifier of python is public so we do not have to make our methods public manually