
# Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n.
# De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.

# Python program to generate binary numbers from
# 1 to n

# This function uses queue data structure to print binary numbers


def generatePrintBinary(n):
    # Create an empty queue
    from queue import Queue
    q = Queue()

    # Enqueue the first binary number
    q.put("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while (n > 0):
        n -= 1
        # Print the front of queue
        s1 = q.get()
        print(s1)

        s2 = s1  # Store s1 before changing it

        # Append "0" to s1 and enqueue it
        q.put(s1 + "0")

        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.put(s2 + "1")


# Driver program to test above function
n = 10
generatePrintBinary(n)
