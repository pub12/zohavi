import unittest

import sys
sys.path.insert(0, '../')

# from flask import Flask, render_template, jsonify
from zohavi.zemailer import Emailer
# from zohavi.zwebui.routes import WebUIView


class TestProc(unittest.TestCase):
	# print('sssss')

	def setup_email(self):
		return Emailer( config ={"HOST":"mail.trendcelebs.com", "PORT":465, "SENDER":"admin@trendcelebs.com", "PASSWORD":"p9sLk00OpKpP"} )
	def test_email_send_plain_text(self):
		emailer = self.setup_email()
		email_ret = emailer.send_email( "hello", "admin@trendcelebs.com", ["pubs@pythonhowtoprogram.com"], "hello world","")

		self.assertEqual( {}, email_ret )

	def test_email_send_html(self):
		emailer = self.setup_email()
		email_ret = emailer.send_email( "hello there", "admin@trendcelebs.com", ["pubs@pythonhowtoprogram.com"], "hello world","<h1>hello world</h1>")

		self.assertEqual( {}, email_ret )

	