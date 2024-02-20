#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *
import unittest
import MySQLdb

class TestMySQL(unittest.TestCase):
    def setUp(self):
        # Connect to the MySQL database
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='test_db')
        self.cursor = self.conn.cursor()

        # Create a table for testing
        self.cursor.execute('CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')

    def tearDown(self):
        # Clean up after the test
        self.cursor.execute('DROP TABLE IF EXISTS states')
        self.conn.close()

    def test_add_state(self):
        # Get the number of records before adding a new state
        self.cursor.execute('SELECT COUNT(*) FROM states')
        count_before = self.cursor.fetchone()[0]

        # Execute the command to add a new state
        self.cursor.execute('INSERT INTO states (name) VALUES ("California")')
        self.conn.commit()

        # Get the number of records after adding the new state
        self.cursor.execute('SELECT COUNT(*) FROM states')
        count_after = self.cursor.fetchone()[0]

        # Check if the number of records increased by 1
        self.assertEqual(count_after, count_before + 1)

if __name__ == '__main__':
    unittest.main()

