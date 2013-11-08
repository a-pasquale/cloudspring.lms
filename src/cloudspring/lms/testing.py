from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CloudspringlmsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cloudspring.lms
        xmlconfig.file(
            'configure.zcml',
            cloudspring.lms,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


CLOUDSPRING_LMS_FIXTURE = CloudspringlmsLayer()
CLOUDSPRING_LMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CLOUDSPRING_LMS_FIXTURE,),
    name="CloudspringlmsLayer:Integration"
)
CLOUDSPRING_LMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CLOUDSPRING_LMS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CloudspringlmsLayer:Functional"
)
