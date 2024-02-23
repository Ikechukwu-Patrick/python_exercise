import unittest

import self

from PrimaryPackages import Gun


class myGunTest(unittest.TestCase):
    def test_add_bullet(self):
        gun = Gun.Gun()
        gun.add_bullet(5)
        self.assertEqual(5, Gun.add_bullet())
