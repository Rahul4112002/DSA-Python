class Node:
    """Node structure for Linked List"""
    def __init__(self, data):
        self.data = data  # Data part of Node
        self.next = None  # Pointer to next Node

class LinkedList:
    """Linked List Implementation"""
    def __init__(self):
        self.head = None  # Initialize an empty Linked List

    def insert_at_end(self, data):
        """Inserts a new node at the end of the Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the Linked List"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """Deletes a node with a specific value"""
        temp = self.head

        # If head node holds the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """Displays the entire Linked List"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example: Browser Tabs Management
class BrowserTabs:
    """Real-life example of Linked List: Managing browser tabs"""
    def __init__(self):
        self.tabs = LinkedList()

    def open_tab(self, tab_name):
        """Opens a new browser tab (inserts at end)"""
        print(f"Opening tab: {tab_name}")
        self.tabs.insert_at_end(tab_name)

    def close_tab(self, tab_name):
        """Closes a tab (deletes a node)"""
        print(f"Closing tab: {tab_name}")
        self.tabs.delete_node(tab_name)

    def show_tabs(self):
        """Displays currently open browser tabs"""
        print("Current Tabs: ", end="")
        self.tabs.display()

# Driver Code
if __name__ == "__main__":
    print("Creating Linked List...")
    ll = LinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.insert_at_end(15)
    ll.insert_at_beginning(1)
    print("Linked List after insertion:")
    ll.display()

    print("\nDeleting node 10...")
    ll.delete_node(10)
    print("Linked List after deletion:")
    ll.display()

    print("\nBrowser Tabs Simulation:")
    browser = BrowserTabs()
    browser.open_tab("Google")
    browser.open_tab("YouTube")
    browser.open_tab("GitHub")
    browser.show_tabs()

    print("\nClosing 'YouTube' tab...")
    browser.close_tab("YouTube")
    browser.show_tabs()
