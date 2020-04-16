


# Python program to add two numbers represented by linked list

# Node class 
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Add contents of two linked lists and return the head

    # node of resultant list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both list exists 
        while (first is not None or second is not None):

            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # update carry for next calculation 
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10 
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data 
            temp = Node(Sum)

            # if this is the first node then set it as head 
            # of resultant list 
            if self.head is None:
                self.head = temp
            elif prev is not None:
                prev.next = temp

                # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes 
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)
        return self.head
            # Utility function to print the linked LinkedList

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.data) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

# Driver program to test above function
def main():
    first = LinkedList()
    second = LinkedList()

# Create first list 
    first.push(8)
    first.push(1)



# Create second list 
    second.push(0)



# Add the two lists and see result 
    res = LinkedList()
    ret = res.addTwoLists(first.head, second.head)
    out = listNodeToString(ret)
    print(out)

if __name__ == '__main__':
    main()