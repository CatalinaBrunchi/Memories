class User:
    
    """
    Represents a user of the social media application.

    Attributes:
        username (str): The user's username, used for identification and login.
        password (str): The user's password, used for authentication (Note: in a real application, passwords should be hashed).
        email (str): The user's email address.
        memories (list): A list of memories (posts) created by the user.

    Methods:
        add_memory(memory): Adds a new memory to the user's list of memories.
    """
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.memories = []

    def add_memory(self, memory):
        self.memories.append(memory)    


class Memory:
    """
    Represents a memory (post) shared by users on the social media application.

    Attributes:
        title (str): The title of the memory.
        description (str): A detailed description of the memory.
        timestamp (str): The date and time when the memory was created.
        users (list): A list of users who are associated with the memory.
        images (list): A list of images attached to the memory.
        comments (list): A list of comments made on the memory.
        likes (int): The count of likes the memory has received.

    Methods:
        add_users(new_users): Adds one or more users to the memory's user list.
        add_image(image): Adds an image to the memory's image list.
        add_comment(comment): Adds a comment to the memory.
        add_like(): Increments the memory's like count.
    """
    def __init__(self, title, description, timestamp, users, images=None):
        self.title = title
        self.description = description
        self.timestamp = timestamp
        self.users = users  # Now a list of users
        self.images = images if images is not None else []
        self.comments = []
        self.likes = 0
        
    def add_users(self, new_users):
        self.users.extend(new_users)    

    def add_image(self, image):
        self.images.append(image)

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, like):
        self.likes.append(like)
    
    def add_like(self):
        self.likes += 1    


class Image:
    """
    Represents an image uploaded to the social media application.

    Attributes:
        file (str): The file path or URL to the image.
        caption (str, optional): A caption describing the image.
        timestamp (str, optional): The date and time when the image was uploaded.
    """
    def __init__(self, file, caption=None, timestamp=None):
        self.file = file
        self.caption = caption
        self.timestamp = timestamp


class Comment:
    """
    Represents a comment made on a memory.

    Attributes:
        content (str): The text content of the comment.
        timestamp (str): The date and time when the comment was made.
        user (User): The user who made the comment.
    """
    def __init__(self, content, timestamp, user):
        self.content = content
        self.timestamp = timestamp
        self.user = user


class Album:
    """
    Represents a collection of memories grouped into an album.

    Attributes:
        name (str): The name of the album.
        description (str): A description of the album's content.
        creator (User): The user who created the album.
        memories (list): A list of memories included in the album.

    Methods:
        add_memory(memory): Adds a memory to the album.
    """
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator
        self.memories = []

    def add_memory(self, memory):
        self.memories.append(memory)


class Event:
    """
    Represents a social event that can be associated with memories.

    Attributes:
        name (str): The name of the event.
        description (str): A description of the event.
        date (str): The date of the event.
        time (str): The time when the event takes place.
        location (str): The location of the event.
        related_memories (list): A list of memories related to the event.

    Methods:
        add_related_memory(memory): Associates a memory with the event.
    """
    def __init__(self, name, description, date, time, location):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.location = location
        self.related_memories = []

    def add_related_memory(self, memory):
        self.related_memories.append(memory)


class Notification:
    def __init__(self, notification_type, content, timestamp, recipient):
        self.notification_type = notification_type
        self.content = content
        self.timestamp = timestamp
        self.recipient = recipient


class ConnectionRequest:
    def __init__(self, sender, recipient, status):
        self.sender = sender
        self.recipient = recipient
        self.status = status


class Profile:
    def __init__(self, user, profile_picture=None, bio=None):
        self.user = user
        self.profile_picture = profile_picture
        self.bio = bio
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


class Like:
    def __init__(self, user, memory_or_comment):
        self.user = user
        self.memory_or_comment = memory_or_comment


class Tag:
    def __init__(self, user, memory):
        self.user = user
        self.memory = memory


class Search:
    @staticmethod
    def search_users(keyword):
        pass  # Implement user search logic

    @staticmethod
    def search_memories(keyword):
        pass  # Implement memory search logic

    @staticmethod
    def search_albums(keyword):
        pass  # Implement album search logic


class Timeline:
    def __init__(self, user):
        self.user = user
        self.memories = []

    def add_memory(self, memory):
        self.memories.append(memory)
