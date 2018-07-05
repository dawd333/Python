import Drawer
import unittest


class TestDrawer(unittest.TestCase):
    def test_init(self):
        drawer1 = Drawer.Drawer("total production", ["STATE"], [100])
        self.assertEqual(drawer1.state_array, ["STATE"])
        self.assertEqual(drawer1.total_production_array, [100])
        self.assertEqual(drawer1.production_value_array, [])
        self.assertEqual(drawer1.mode, "total production")
        drawer2 = Drawer.Drawer("production value", ["STATE"], [100])
        self.assertEqual(drawer2.state_array, ["STATE"])
        self.assertEqual(drawer2.total_production_array, [])
        self.assertEqual(drawer2.production_value_array, [100])
        self.assertEqual(drawer2.mode, "production value")

        with self.assertRaises(SystemExit) as cm:
            drawer3 = Drawer.Drawer("zly mode", ["STATE"], [100])
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
