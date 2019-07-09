import popular_products
import numpy as np
import pandas as pd
import unittest

class PpTest(unittest.TestCase):
	
	#check if orders dataframe contains only unique OrderId's
	def test_unique_orders(self):
		self.df1 = pd.read_csv('orders.csv')
		self.assertEqual(len(self.df1['OrderId']), len(self.df1['OrderId'].unique()))
        
    #check if resulting dataframe is not greater then unique ProductId's
	def test_check_lenght(self):
		self.df1 = pd.read_csv('orders.csv')
		self.df2 = pd.read_csv('order_lines.csv')
		self.assertLessEqual(len(popular_products(self.df1, self.df2)), len(self.df2['ProductId'].unique()))
        
if __name__ == '__main__':
	unittest.main()