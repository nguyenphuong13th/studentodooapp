import json

import odoo
import logging
_logger = logging.getLogger(__name__)

class MyStudentAPI(odoo.http.Controller): # class MystudentAPI kế thừa odoo controller là http.Controller
    @odoo.http.route('/foo', auth='public') #Routing đường dẫn đến method mà sẽ đón nhận xử lý: route @ /foo -> foo_handler()
    def foo_handler(self):
        return "Welcome to 'foo' API!"

    # @odoo.http.route('/bar', auth='public')  # Routing đường dẫn đến method mà sẽ đón nhận xử lý: route @ /foo -> foo_handler()
    # def bar_handler(self):
    #     return json.dumps({
    #         "content": "Welcome to 'bar' API!"
    #     })