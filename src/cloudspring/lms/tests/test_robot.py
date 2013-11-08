from  cloudspring.lms.testing import CLOUDSPRING_LMS_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=CLOUDSPRING_LMS_FUNCTIONAL_TESTING)
    ])
    return suite