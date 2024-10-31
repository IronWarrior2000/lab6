# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data for the node
        self.next = None  # Initialize the next pointer to None (no next node yet)

# Create individual nodes with data values
node1 = Node(10)  # First node with data 10
node2 = Node(20)  # Second node with data 20
node3 = Node(30)  # Third node with data 30

# Link the nodes together to form a chain (a simple linked list)
# Link node1 to node2
node1.next = node2
# Link node2 to node3
node2.next = node3

# Function to traverse the list and print each node's data
def print_linked_list(head):
# Start with the head node
# Continue until reach the end of the list (None)
# Print the data and follow with "->"
# Move to the next node in the list
# Indicate the end of the list
    
    current = head
    while current:
        print(current.data, "->")
        current = current.next
    print(None)

#Added this print statement to separate and label each section
print("Example ----------")
print_linked_list(node1)
# Test the print function by printing the linked list from node1
print("\nExercise 1------------")
# Exercise 1: Update node2's data and print the list again
# Change data in the second node
node2.data = 70
print_linked_list(node1)


# Exercise 2: Add a new node (node4) with a new value and link it to the list
# Create a new fourth node with data 40
# Link node3 to the new node4
node4 = Node(40)
node3.next = node4
#Added this print statement to separate and label each section
print("\nExercise 2------------")
print_linked_list(node1)


# Exercise 3: Modify the print function to count nodes and print the count
def print_linked_list_with_count(head):
    # Start with the head node
    # Initialize a counter for the nodes
    # Traverse until the end of the list
    # Print the data for each node
    # Move to the next node
    # Increment the count for each node visited
    # Indicate the end of the list
    # Print the total node count
    current = head
    count = 0
    while current:
        print(current.data, "->")
        current = current.next
        count += 1
    print(None)
    print(f"\nTotal Amount of Counts: {count}")

# Test the new function to print the list and count nodes
# Added this print statement to separate and label each section
print("\nExercise 3-------------------")
print_linked_list_with_count(node1)


