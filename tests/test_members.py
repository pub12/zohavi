import unittest, json

import sys
sys.path.insert(0, '../')

from flask import Flask, render_template, jsonify
from zohavi.zbase.routes import BaseView
from zohavi.zwebui.routes import WebUIView
from zohavi.zmembers.routes import MembersView


class TestProc(unittest.TestCase):
	# print('sssss')
	def create_app(self):
		app = Flask(__name__)
		app.register_blueprint( BaseView.bp, url_prefix='/base' )
		app.register_blueprint( WebUIView.bp, url_prefix='/webui' )
		app.register_blueprint( MembersView.bp, url_prefix='/members' )
		app.debug = False

		return app

	# from zohavi_procs import 
	def test_members_blueprint_registration(self):
		app = self.create_app()
		self.assertNotEqual( app, None)

	def test_run_app(self):
		app = self.create_app()
		
		@app.route("/routes", methods=["GET"])
		def getRoutes():
			routes = {}
			for r in app.url_map._rules:
				routes[r.rule] = {}
				routes[r.rule]["functionName"] = r.endpoint
				routes[r.rule]["methods"] = list(r.methods)
			routes.pop("/static/<path:filename>")
			return jsonify(routes)
			
		@app.route("/")
		def hello_world():
			# raise
			return render_template('test_zmembers_001.html')

		app.run(host="0.0.0.0", port=8602)

if __name__ == '__main__':
    unittest.main()