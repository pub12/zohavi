import unittest, datetime

import sys
sys.path.insert(0, '../')

from flask import Flask, Blueprint
from zohavi.zcommon import Utils


class TestCommon(unittest.TestCase):
	#############################################################
	def test_is_dir_valid(self):	
		self.assertEqual( Utils.is_dir_valid('.'), True)

	#############################################################
	def test_is_file_valid(self):	
		self.assertEqual( Utils.is_file_or_dir(__file__), True)


	#############################################################
	def test_is_date(self):
		self.assertEqual( Utils.date_str_to_date_obj( '2022-01-20'), datetime.datetime(2022, 1, 20, 0, 0) )
		self.assertEqual( Utils.date_str_to_date_obj( '2022-9920'), None )
	
	#############################################################
	def test_is_all_from_listA_in_listB(self):
		self.assertEqual( Utils.is_all_from_listA_in_listB( ['a', 'b'], ['x', 'y', 'a', 'f', 'b'] ), True)
		self.assertEqual( Utils.is_all_from_listA_in_listB( ['a', 'b'], ['x', 'y', 'a', 'f', 'c'] ), False)
	
	#############################################################
	def test_has_all_dict_values(self):
		self.assertEqual( Utils.has_all_dict_values(  ['a', 'b'], {'a':'aa', 'b':'cc'}), True  )

	#############################################################
	def test_concat_dirs(self):
		self.assertEqual( Utils.concat_dirs(  'abc', 'def' ), 'abc/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc/', 'def' ), 'abc/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc', 'def/' ), 'abc/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc/def', 'def' ), 'abc/def/def/'  )
		self.assertEqual( Utils.concat_dirs(  '/abc', 'def' ), '/abc/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc/def/', 'def' ), 'abc/def/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc', '/def' ), 'abc/def/'  )
		self.assertEqual( Utils.concat_dirs(  'abc', 'def/' ), 'abc/def/'  )


