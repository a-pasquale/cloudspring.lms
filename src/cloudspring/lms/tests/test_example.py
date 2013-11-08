import unittest2 as unittest


from cloudspring.lms.testing import \
    CLOUDSPRING_LMS_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = CLOUDSPRING_LMS_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        pass

    def test_success(self):
        sum = 1 + 3
        self.assertEqual(sum, 4)

