"""

API Auto Test Python №1:

Створення профілю нового користувача завдяки API + Тестування

"""

import coreapi
import pytest_check as check


class TestRegistration:
    def test_registration(self):
        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://testsite.light-it.io/docs/")

        username = "alextest247"
        email = "alextest257@mail.com"
        password = "123456qwerty123!"

        # Interact with the API endpoint
        action = ["profiles", "create"]
        params = {
            "username": username,
            "email": email,
            "password1": password,
            "password2": password,
        }

        try:
            # Perform the API request
            result = client.action(schema, action, params=params)

            # JSON response output
            result = dict(result)
            result['user'] = dict(result['user'])
            print(f"Profile creation! JSON response:\n{result}")
            check.equal(result['user']['username'], params["username"])
        except Exception as e:
            print(f"Profile creation Error! Error message: {str(e)}")
            check.equal({str(e)}, "Error!")
            #check.is_in("A user is already registered with this e-mail address.", {str(e)})
