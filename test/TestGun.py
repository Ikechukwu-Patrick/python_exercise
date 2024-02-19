import unittest

import self

from PrimaryPackages import Gun


class myGunTest(unittest.TestCase):
    def test_add_bullet(self):
        gun = Gun(10)
        gun.add_bullet(5)
        self.assertEqual(5, gun.add_bullet())
