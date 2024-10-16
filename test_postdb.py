import unittest
import sqlite3
import os
from connection import PostDB  # Import the PostDB class from your existing file

class TestPostDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a temporary database for testing."""
        cls.test_db_name = 'test_database.db'
        cls.db = PostDB(cls.test_db_name)

    @classmethod
    def tearDownClass(cls):
        """Remove the test database after tests."""
        cls.db.conn.close()
        os.remove(cls.test_db_name)

    def test_add_post(self):
        """Test adding a post."""
        self.db.add_post("Test Title", "Test Content", 100, 10)
        posts = self.db.fetch_all()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Test Title")
        self.assertEqual(posts[0]['content'], "Test Content")
        self.assertEqual(posts[0]['price'], 100)
        self.assertEqual(posts[0]['amount'], 10)

    def test_update_post(self):
        """Test updating an existing post."""
        self.db.add_post("Old Title", "Old Content", 50, 5)
        post_id = self.db.fetch_all()[0]['id']
        self.db.update_post(post_id, "New Title", "New Content", 150, 15)
        
        post = self.db.fetch_all()[0]
        self.assertEqual(post['title'], "New Title")
        self.assertEqual(post['content'], "New Content")
        self.assertEqual(post['price'], 150)
        self.assertEqual(post['amount'], 15)

    def test_delete_post(self):
        """Test deleting a post."""
        self.db.add_post("Delete Me", "Content", 20, 2)
        post_id = self.db.fetch_all()[0]['id']
        self.db.delete_post(post_id)
        
        posts = self.db.fetch_all()
        self.assertEqual(len(posts), 0)

    def test_fetch_all(self):
        """Test fetching all posts."""
        self.db.add_post("Post 1", "Content 1", 30, 3)
        self.db.add_post("Post 2", "Content 2", 40, 4)
        
        posts = self.db.fetch_all()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Post 1")
        self.assertEqual(posts[1]['title'], "Post 2")

if __name__ == '__main__':
    unittest.main()
