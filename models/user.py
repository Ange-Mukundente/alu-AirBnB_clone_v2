from models import storage
from models.state import State
from models.city import City
from models.user import User  # Import the User model

def test_create_user_with_all_attributes():
    # Can create User with email, password, first_name, and last_name via the console
    new_user = User(email="a@a.com", password="pwd", first_name="fn", last_name="ln")
    storage.new(new_user)
    storage.save()
    print("Test create User with all attributes is present - Passed")

def test_create_user_with_email_and_password():
    # Can create User with email and password via the console
    new_user = User(email="a@a.com", password="pwd")
    storage.new(new_user)
    storage.save()
    print("Test create User with email and password is present - Passed")

def test_create_user_only_email():
    # Can't create User with only email via the console
    try:
        user_without_password = User(email="a@a.com")
        storage.new(user_without_password)
        storage.save()
        print("Test failed: User created with only email.")
    except Exception as e:
        print("Test passed: {}".format(e))

def test_create_user_only_password():
    # Can't create User with only password via the console
    try:
        user_without_email = User(password="pwd")
        storage.new(user_without_email)
        storage.save()
        print("Test failed: User created with only password.")
    except Exception as e:
        print("Test passed: {}".format(e))

def test_create_user_without_email_and_password():
    # Can't create User without email and password via the console
    try:
        user_without_credentials = User()
        storage.new(user_without_credentials)
        storage.save()
        print("Test failed: User created without email and password.")
    except Exception as e:
        print("Test passed: {}".format(e))

def test_list_all_users():
    # Can list all User in MySQL (created outside the program)
    # Implement the logic to fetch and print all users from your MySQL database
    all_users = storage.all(User)
    print("All Users in MySQL:")
    for user_id, user in all_users.items():
        print(user)

def main():
    test_create_state()
    test_create_city()
    test_create_city_space_translation()
    test_rollback()
    test_table_exists()

    # New User-related tests
    test_create_user_with_all_attributes()
    test_create_user_with_email_and_password()
    test_create_user_only_email()
    test_create_user_only_password()
    test_create_user_without_email_and_password()
    test_list_all_users()

if __name__ == "__main__":
    main()
