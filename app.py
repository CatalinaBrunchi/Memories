# app.py
import datetime 
from models import User, Memory, Album, Comment

# Main application entry point
def main():
    # Initialize lists to hold user and memory objects
    users = []
    memories = []
    # Variable to keep track of the logged-in user
    logged_in_user = None
    
    # Main application loop
    while True:
        # Print the main menu options
        print("\nMain Menu")
        print("1. Create a new user")
        print("2. Log In")
        print("3. Create a new memory")
        print("4. View all memories")
        print("5. Add users to a memory")
        print("6. View user memories")
        print("7. Add a comment to a memory")
        print("8. Exit")
        
        # Get the users's menu choice
        choice = input("Enter your choice: ")
        
        # Handle the user's choice
        if choice == "1":
            # Create a new user
            create_user(users)
        elif choice == "2":
            # Log in a user
            logged_in_user = login(users)
            if logged_in_user:
                print(f"You are now logged in as {logged_in_user.username}.")
            else:
                print("Login failed.")
        elif choice == "3":
            # Create a new memory, ensuring the user is logged in
            if logged_in_user:
                create_memory(logged_in_user, memories)
            else:
                print("Please log in to create a memory.")
        elif choice == "4":
            # View all memories
            view_memories(memories)
        elif choice == "5":
            # Add users to an existing memory
            add_users_to_memory(users, memories)
        elif choice == "6":
            # View memories created by a specific user
            view_user_memories(users)    
        elif choice == "7":
            # Add a comment to a specific memory
            add_comment_to_memory(users, memories)
        elif choice == "8":
            # Exit the application
            print("Thank you for using Memory!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Function to create a new user
def create_user(users):
    global logged_in_user
    # Ask for user details 
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    # Create a new User object and add it to the list of users
    user = User(username, password, email)
    users.append(user)
    # Confirm user creation
    print(f"User created: {user.username}")
    # Log out any currently logged-in user
    logged_in_user = None  # Log out the current user
    print("You have been logged out. Please log in again.")

# Function to handle user login    
def login(users):
    # Ask for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check if the username and password match a user in the list
    for user in users:
        if user.username == username and user.password == password:
            # Successful login
            print(f"Welcome, {username}!")
            return user
    # If login fails, return None
    print("Invalid username or password.")
    return None

# Function to create a new memory    
def create_memory(logged_in_user, memories):
    # Ensure a user is logged in
    if not logged_in_user:
        print("Please log in to create a memory.")
        return
    
    # Ask for memory details
    title = input("Enter memory title: ")
    description = input("Enter memory description: ")
    timestamp = input("Enter memory timestamp (e.g., MM/DD/YYYY): ")
    # Create a new Memory object and add it to the list of memories
    new_memory = Memory(title, description, timestamp, [logged_in_user])
    memories.append(new_memory)
    # Associtate the memory with the user who created it
    logged_in_user.add_memory(new_memory)  # Add the memory to the user's list
    print("Memory created successfully!")


# Function to display all memories associated comments
def view_memories(memories):
    # Check if there are any memories to display
    if not memories:
        print("No memories available.")
        return

    # Loop through the list of memories and print their details
    for memory in memories:
        print(f"Title: {memory.title}")
        print(f"Description: {memory.description}")
        print(f"Timestamp: {memory.timestamp}")
        # Create a comma-separated list of usernames who are associated with the memory
        user_names = ', '.join(user.username for user in memory.users)
        print(f"Users: {user_names}")
        # Check if the memory has any comments and display them
        if memory.comments:
            print("Comments:")
            for comment in memory.comments:
                # Print each comment with the username of the commenter and timestamp
                print(f"\t{comment.user.username} ({comment.timestamp}): {comment.content}")
        print("-" * 20)


def add_users_to_memory(users, memories):
    # Check if there are any memories to modify
    if not memories:
        print("No memories available. Please create a memory first.")
        return
    
    # Display all memories with a numerical choice
    print("Select a memory:")
    for i, memory in enumerate(memories):
        print(f"{i + 1}. {memory.title}")
        
    # User selects a memory to modify by number    
    memory_choice = int(input("Enter memory number: "))
    selected_memory = memories[memory_choice - 1]
    
    # Prompt user to select which users to add to the memory
    print("Select users to add (separate numbers with commas):")
    for i, user in enumerate(users):
        print(f"{i + 1}. {user.username}")
    user_choices = input("Enter user numbers: ").split(',')
    
    # Process user choices and add to the memory if not already present
    new_users = []
    for choice in user_choices:
        try:
            user_index = int(choice.strip()) - 1
            user = users[user_index]
            if user not in selected_memory.users:
                new_users.append(user)
            else:
                print(f"{user.username} is already a part of this memory.")
        except (ValueError, IndexError):
            print(f"Invalid user number: {choice}")
    
    # Add new users to the memory and confirm
    if new_users:
        selected_memory.add_users(new_users)
        print("Users added successfully to the memory!")
    else:
        print("No new valid users selected. Please try again.")
        
def view_user_memories(users):
    # Check if there are users to select from
    if not users:
        print("No users available.")
        return
    
    # Display all users for selection
    print("Select a user to view their memories:")
    for i, user in enumerate(users):
        print(f"{i + 1}. {user.username}")
    
    # User selects which user's memories to view by number
    user_choice = int(input("Enter user number: "))
    selected_user = users[user_choice - 1]
    
    # Display the selected user's memories if they have any
    if not selected_user.memories:
        print(f"{selected_user.username} has not created any memories.")
        return

    print(f"\nMemories created by {selected_user.username}:")
    for memory in selected_user.memories:
        print(f"Title: {memory.title}")
        print(f"Description: {memory.description}")
        print(f"Timestamp: {memory.timestamp}")
        print("-" * 20)
        

def add_comment_to_memory(users, memories):
    # Check if there are any memories to comment on
    if not memories:
        print("No memories available. Please create a memory first.")
        return
    
    # Display all memories for selection
    print("Select a memory to comment on:")
    for i, memory in enumerate(memories):
        print(f"{i + 1}. {memory.title}")
        
    # User selects a memory to comment on by number    
    memory_choice = int(input("Enter memory number: "))
    selected_memory = memories[memory_choice - 1]
    
    # Prompt the user to select who is commenting
    print("Select a user to comment as:")
    for i, user in enumerate(users):
        print(f"{i + 1}. {user.username}")
        
    # User selects which user they are commenting as by number    
    user_choice = int(input("Enter user number: "))
    selected_user = users[user_choice - 1]
    
    # User enters the content of their comment
    comment_content = input("Enter your comment: ")
    
    # Automatically generate the timestamp
    comment_timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    # Create a new comment object
    new_comment = Comment(comment_content, comment_timestamp, selected_user)
    
    # Add the comment to the selected memory
    selected_memory.add_comment(new_comment)
    
    # Confirm the comment has been added
    print("Comment added successfully!")

# Run the main function if this file is executed as a script
if __name__ == "__main__":
    main()
