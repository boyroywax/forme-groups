import unittest
import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.base import Base


class TestBase(unittest.TestCase):

    def test_base(self):
        base = Base()
        self.assertEqual(base.__str__(), 'Base')
        self.assertEqual(base.__repr__(), 'Base')

    def test_base_log_error(self):
        base = Base()
        base.log.error('Test Error Logging')

    def test_base_log_info(self):
        base = Base()
        base.log.info('Test Info Logging')

    def test_base_log_debug(self):
        base = Base()
        base.log.debug('Test Debug Logging')

    def test_base_log_warning(self):
        base = Base()
        base.log.warning('Test Warning Logging')

    def test_base_log_critical(self):
        base = Base()
        base.log.critical('Test Critical Logging')

    def test_base_log_exception(self):
        base = Base()
        base.log.exception('Test Exception Logging')
