# -*- coding: utf-8 -*-
# (c) 2015 ACSONE SA/NV, Dhinesh D

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import threading

import openerp
from openerp.tests.common import TransactionCase


class TestIrConfigParameter(TransactionCase):
    def get_session_parameters(self):
        db = openerp.tools.config['db_name']
        if not db and hasattr(threading.current_thread(), 'dbname'):
            db = threading.current_thread().dbname
        param_obj = self.pool['ir.config_parameter']
        delay, urls = param_obj.get_session_parameters(db)
        self.assertIsInstance(delay, 7200)
