# from zohavi_procs import __version__
import unittest

import sys
sys.path.insert(0, '../')

from flask import Flask, render_template
from zohavi.zbase.routes import BaseView


class TestProc(unittest.TestCase):
	# print('sssss')

	# from zohavi_procs import 
	def test_blueprint_registration(self):
		app = Flask(__name__)
		app.register_blueprint( BaseView.bp )

		self.assertNotEqual( app, None)

	def x_test_run_app(self):
		app = Flask(__name__)
		app.register_blueprint( BaseView.bp )

		@app.route("/")
		def hello_world():
			return render_template('test_zbase_001.html')


		app.run(host="0.0.0.0", port=6601)