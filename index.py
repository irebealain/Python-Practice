from user import User
from post import Post
app_user_one = User("irebalain@gmail.com", "Alain", "password1", "AI engineer")
app_user_one.get_user_info()
app_user_two = User("kezaarlene2@gmail.com", "Kenza", "passw", "journalist")
app_user_two.get_user_info()
# Objects created from the class called Post
app_book_one = Post("Look at me & tell me what you see", app_user_two.name)
app_book_one.get_post_info()