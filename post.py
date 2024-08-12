class Post:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_post_info(self):
        print(f"The book title: {self.title}, it was written by {self.author}")
