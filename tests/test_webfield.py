import unittest, json

import sys
sys.path.insert(0, '../')

from flask import Flask, render_template, jsonify
from zohavi.zbase.routes import BaseView
from zohavi.zwebui.routes import WebUIView
from zohavi.zwebui.web_field import WebField, Validate, Transform


class TestValidation(unittest.TestCase):
	# print('sssss')
	
	def test_validation_required(self):
		self.assertEqual( Validate.required( '', False), True)      #if not required return should be true
		self.assertEqual( Validate.required( 'abc', False), True)   #if not required return should be true

		self.assertEqual( Validate.required( 'abc', True), True)    #if  required return should be true if present
		self.assertEqual( Validate.required( '', True), False)      #if  required return should be false if not present

	def test_validation_text_min_len(self):
		self.assertEqual( Validate.text_min_len( 'abc', 2), True )
		self.assertEqual( Validate.text_min_len( 'abc', 3), True )
		self.assertEqual( Validate.text_min_len( 'abc', 4), False )
		self.assertEqual( Validate.text_min_len( '', 2), False )


	def test_validation_text_max_len(self):
		self.assertEqual( Validate.text_max_len( 'abc', 2), False )
		self.assertEqual( Validate.text_max_len( 'abc', 3), True )
		self.assertEqual( Validate.text_max_len( 'abc', 4), True )
		self.assertEqual( Validate.text_max_len( '', 2), True )

	def test_validation_num_gte(self):
		self.assertEqual( Validate.num_gte( 2, 10), False )
		self.assertEqual( Validate.num_gte( 20, 10), True )
		self.assertEqual( Validate.num_gte( 10, 10), True )
		self.assertEqual( Validate.num_gte( '2', 10), False )
		self.assertEqual( Validate.num_gte( '20', 10), True )
		self.assertEqual( Validate.num_gte( '10', 10), True )
		self.assertEqual( Validate.num_gte( '2', '10'), False )
		self.assertEqual( Validate.num_gte( '20', '10'), True )
		self.assertEqual( Validate.num_gte( '10', '10'), True )
	
	def test_validation_num_lte(self):
		self.assertEqual( Validate.num_lte( 2, 10), True )
		self.assertEqual( Validate.num_lte( 20, 10), False )
		self.assertEqual( Validate.num_lte( 10, 10), True )
		self.assertEqual( Validate.num_lte( '2', 10), True )
		self.assertEqual( Validate.num_lte( '20', 10), False )
		self.assertEqual( Validate.num_lte( '10', 10), True )
		self.assertEqual( Validate.num_lte( '2', '10'), True )
		self.assertEqual( Validate.num_lte( '20', '10'), False )
		self.assertEqual( Validate.num_lte( '10', '10'), True )
	
	def test_validation_is_url(self):
		self.assertEqual( Validate.is_url( ''), False )
		self.assertEqual( Validate.is_url( 'www.google.com'), True )
		self.assertEqual( Validate.is_url( 'http://wwww.google.com'), True )
		self.assertEqual( Validate.is_url( 'https://www.google.com'), True )
		self.assertEqual( Validate.is_url( 'www.google.com/'), True )
		self.assertEqual( Validate.is_url( 'http://wwww.google.com/'), True )
		self.assertEqual( Validate.is_url( 'https://www.google.com/'), True )
		self.assertEqual( Validate.is_url( 'www.google.com/index.html'), True )
		self.assertEqual( Validate.is_url( 'http://wwww.google.com/index.html'), True )
		self.assertEqual( Validate.is_url( 'https://www.google.com/index.html'), True )
		self.assertEqual( Validate.is_url( 'www.google.com/analaytics'), True )
		self.assertEqual( Validate.is_url( 'http://wwww.google.com/analaytics'), True )
		self.assertEqual( Validate.is_url( 'https://www.google.com/analaytics'), True )
		self.assertEqual( Validate.is_url( 'www.google.com/analaytics/'), True )
		self.assertEqual( Validate.is_url( 'http://wwww.google.com/analaytics/'), True )
		self.assertEqual( Validate.is_url( 'https://www.google.com/analaytics/'), True )
		
	def test_validation_is_ip(self):
		self.assertEqual( Validate.is_ip( ''), False )
		self.assertEqual( Validate.is_ip( '0.0.0.0'), True ) 
		self.assertEqual( Validate.is_ip( '255.255.255.255'), True ) 
		self.assertEqual( Validate.is_ip( '256.256.256.256'), False ) 
		
		 
	def test_validation_is_unix_path(self):
		self.assertEqual( Validate.is_unix_path( 'abc'), True )
		self.assertEqual( Validate.is_unix_path( '/abc'), True )
		self.assertEqual( Validate.is_unix_path( '/abc/'), True )
		self.assertEqual( Validate.is_unix_path( '/abc/xyz'), True )
		self.assertEqual( Validate.is_unix_path( '/abc/xyz/'), True )
		
 