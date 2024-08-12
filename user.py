# A class is a blueprint of objects. A plan of a house and each house has its specifications.
class User:
    # This is a constructor in the function below
    def __init__(self, user_email, user_name, user_password, user_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = user_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"The user's email is {self.email} and the username is {self.name} "
              f"and his current job title is {self.current_job_title}.")
