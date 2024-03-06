import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
  


  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
     
    """-----Test for normal Case--------"""
    self.assertEqual(getRatio(10, 5), 2.0)

  def test_price_b_is_zero(self):

    """"----Test for zero division error"""
    self.assertIsNone(getRatio(0, 0))
  

  def test_both_prices_are_zero(self):
    """"----Test both prices are zero-----"""
    self.assertIsNone(getRatio(0, 0))

  def test_price_a_is_zero(self):
    """-----Test a is zero------"""
    self.assertEqual(getRatio(0, 5), 0.0)
  

  def test_negative_prices(self):
    """------Test for negative-------"""
    self.assertEqual(getRatio(-10, 5), 2.0)

  
  def test_both_negative_prices(self):
    """Test for both negative prices """

    self.assertEqual(getRatio(-10, -5), 2.0)

  def test_exception_handling(self):
    """Test if price_b is a non-numeric value"""

    self.assertIsNone(getRatio(10, 'invalid'))
  
  
  def test_both_for_non_numeric_value(self):
    """---Tes if both orices are non-numeric"""
    self.assertIsNone(getRatio('invalid', 'invalid'))

     




  
  """ ------------ Add more unit tests ------------ """




if __name__ == '__main__':
    unittest.main()



