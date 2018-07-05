import HoneyProduction
import unittest


class TestHoneyProduction(unittest.TestCase):
    def test_init(self):
        honey1 = HoneyProduction.HoneyProduction("A", 1, 2, 3, 4, 0.5, 6, 2000)
        self.assertEqual(honey1.state, "A")
        self.assertEqual(honey1.number_of_colonies, 1)
        self.assertEqual(honey1.yield_per_colony, 2)
        self.assertEqual(honey1.total_production, 3)
        self.assertEqual(honey1.stocks, 4)
        self.assertEqual(honey1.price_per_lb, 0.5)
        self.assertEqual(honey1.production_value, 6)
        self.assertEqual(honey1.year, 2000)

        with self.assertRaises(TypeError):
            honey2 = HoneyProduction.HoneyProduction()

    def test_get_total_production(self):
        honey1 = HoneyProduction.HoneyProduction("A", 1, 2, 3, 4, 0.5, 6, 2000)
        self.assertEqual(honey1.get_total_production(2000), 3)
        self.assertEqual(honey1.get_total_production(1999), False)

    def test_get_production_value(self):
        honey1 = HoneyProduction.HoneyProduction("A", 1, 2, 3, 4, 0.5, 6, 2000)
        self.assertEqual(honey1.get_production_value(2000), 6)
        self.assertEqual(honey1.get_production_value(1999), False)

    def test_get_state(self):
        honey1 = HoneyProduction.HoneyProduction("A", 1, 2, 3, 4, 0.5, 6, 2000)
        self.assertEqual(honey1.get_state(2000), "A")
        self.assertEqual(honey1.get_state(1999), False)


if __name__ == '__main__':
    unittest.main()
