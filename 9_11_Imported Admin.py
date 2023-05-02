
from privileges import Admin
rico = Admin('Rico', 'Robinosn','11/14/1996', '345678')
rico.describe_user()


rico_privileges = ["can add post", "can delete post", "can ban user"]
rico.privileges.privileges = rico_privileges
print(f"\nThe Admin {rico.first_name} has these privileges: ")
rico.privileges.show_privileges()