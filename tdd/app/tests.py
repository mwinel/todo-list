import unittest
from user import User


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.user1 = User('paul', 'paul1', 'paul@example.com', '123456', 25)
        self.user2 = User('mimi', 'mimi', 'mimi@example.com', '12345', 21)

    def test_user_class(self):
        self.assertIsInstance(self.user1, User)
        self.assertIsInstance(self.user2, User)

    def test_name(self):
        self.assertEqual(self.user1.name, 'paul')
        self.assertEqual(self.user2.name, 'mimi')

    def test_username(self):
        self.assertEqual(self.user1.username, 'paul1')
        self.assertEqual(self.user2.username, 'mimi')

    def test_email(self):
        self.assertEqual(self.user1.email, 'paul@example.com')
        self.assertEqual(self.user2.email, 'mimi@example.com')

    def test_password(self):
        self.assertEqual(self.user1.password, '123456')
        self.assertEqual(self.user2.password, '12345')

    def test_age(self):
        self.assertEqual(self.user1.age, 25)
        self.assertEqual(self.user2.age, 21)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
