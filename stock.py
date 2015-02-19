from openerp.osv import osv,fields
from datetime import date
import string

class stock_move(osv.osv):
	_name = "stock.move"
	_inherit = "stock.move"


	def _get_default_location(self, cr, uid, context=None):
        	user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
		location_id = user.pos_config.stock_location_id.id
	        return location_id



	_defaults = {
		'location_id': _get_default_location,
		}

stock_move()
