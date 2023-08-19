import unittest
import calc

class TestCalc(unittest.TestCase):
        
        def test_add(self):
                self.assertEqual(calc.add(10, 15), 25)
                self.assertEqual(calc.add(-1, 1), 0)
                self.assertEqual(calc.add(-1, -1), -2)
        
        def test_sub(self):
                result = calc.sub(15, 10)
                self.assertEqual(result,5)
        def test_mul(self):
                print(self.value)
                self.assertEqual(calc.mul(10, 5), 50)
                self.assertEqual(calc.mul(-1, 1), -1)
                self.assertEqual(calc.mul(-1, -1), 1)
                
        def test_div(self):
                self.assertEqual(calc.div(100, 10), 10)
                self.assertEqual(calc.div(-1, 1), -1)
                self.assertEqual(calc.div(-1, -1), 1)
                with self.assertRaises(ValueError):
                        calc.div(0,10)

if __name__ == '__main__':
        unittest.main()