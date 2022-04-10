import json
from pathlib import Path
  
from flask_classful import  FlaskView,  route 
from . import bp

from flask_login import current_user #,   login_required
from flask_classful import FlaskView, route
from flask import   send_file, current_app, render_template,  current_app , abort

class BaseView(FlaskView):
	route_base = '/'
	# bpname = 'base'
	bp = bp

	##############################################################################################################
	def __init__(self):
		print('***init now**')
		breakpoint()
		self.module_name = __name__

	##############################################################################################################
	#	Return any static resources
	##############################################################################################################
	@route('/st/<string:subdir_type>/<string:module>/<path:resourceFile>')
	def get_page(self, subdir_type, module, resourceFile):		
		# path = current_app.config['APP_BASE_DIR']
		path = current_app.config['ENV_BASE_DIR']
		if subdir_type in [ "_def", "app"]: 
			path += subdir_type + "/" 
		else:
			logger.error( f"incorrect type sent of:{subdir_type}")
			abort(500)

		send_file_path = path + module + "/" + resourceFile

 
		if Path(send_file_path).is_file():
			logger.debug("file found:" + str(send_file_path)   )
			return send_file(send_file_path)

		logger.error("file missing:" + str(send_file_path)   )
		abort(404)

