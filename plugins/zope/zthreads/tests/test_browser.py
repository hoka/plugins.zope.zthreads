from Testing.ZopeTestCase import base
from Products.Five import zcml
import Products.Five
import plugins.zope.zthreads

zcml.load_config('meta.zcml' , Products.Five)
zcml.load_config('configure.zcml' , Products.Five)
zcml.load_config('configure.zcml' , plugins.zope.zthreads)

class TestBrowser(base.TestCase):

    def test_browser(self):
        """ """
        if not self.app.unrestrictedTraverse('@@zthreads')().endswith('End of dump'):
            raise 'zthreads browser not ready'
