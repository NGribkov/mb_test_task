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
		self.assertLessEqual(len(popular_products.popular_products(self.df1, self.df2)), len(self.df2['ProductId'].unique()))
		
	#check if max average order price in resulting dataframe is not greater then max order price
	def test_check_max_price(self):
		self.df1 = pd.read_csv('orders.csv')
		self.df2 = pd.read_csv('order_lines.csv')
		self.assertLessEqual(popular_products.popular_products(self.df1, self.df2)['AvgInvoice'].max(), self.df2.merge(self.df1, on='OrderId', how='left').groupby('OrderId').agg({'Price': 'sum'})['Price'].max())
    
	#check if input data has correct types
	def test_check_types(self):
		self.df1 = pd.read_csv('orders.csv')
		self.df2 = pd.read_csv('order_lines.csv')
		self.assertEqual(self.df1['OrderId'].dtype, 'int64')
		self.assertEqual(self.df1['CustomerId'].dtype, 'int64')
		self.assertEqual(self.df1['DateTime'].dtype, 'object')
		self.assertEqual(self.df2['ProductId'].dtype, 'int64')
		self.assertEqual(self.df2['OrderId'].dtype, 'int64')
		self.assertEqual(self.df2['Price'].dtype, 'int64')
if __name__ == '__main__':
	unittest.main()