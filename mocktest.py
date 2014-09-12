__author__ = 'Administrator'

from roman import RemovalService, UploadService
import os.path
import tempfile
import unittest
import mock
"""
class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(),"tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath,'wb') as f:
            f.write("delete me!")

    def test_rm(self):
        print "in RmTestCase"
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath),"fail")
"""
class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('roman.os.path')
    @mock.patch('roman.os')
    def test_rm(self,mock_os,mock_path):
        print "in RmMockTestCase"
        reference = RemovalService()
        mock_path.isfile.return_value = False
        reference.rm("any path")
        self.assertFalse(mock_os.remove.called,"fail")
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")

class UploadServiceTestCase(unittest.TestCase):
    @mock.patch.object(RemovalService,'rm')
    def test_upload_complete(self,mock_rm):
        removal_service = RemovalService()
        reference = UploadService(removal_service)
        reference.upload_complete('my upload file')
        mock_rm.assert_called_with('my upload file')
        removal_service.rm.assert_called_with('my upload file')

class UploadServiceTestCase1(unittest.TestCase):
    def test_upload_complete(self):
        mock_removal_service = mock.create_autospec(RemovalService)
        print mock_removal_service
        reference = UploadService(mock_removal_service)
        reference.upload_complete('my upload file')
        mock_removal_service.rm.assert_called_with('my upload file')

class Target(object):
    def apply(self,value,are_you_sure):
        print "in apply"
        if are_you_sure:
            return value
        else:
            return value

def method(target, value):
    return target.apply(value,1)

class MethodTestCase(unittest.TestCase):
    def test_method(self):
        target = mock.Mock()
        method(target, "value")
        target.apply.assert_called_with("value",1)

class MethodTestCase1(unittest.TestCase):
    def test_method1(self):
        mock_target = mock.create_autospec(Target)
        method(mock_target, "value")
        mock_target.apply.assert_called_with('value',1)

if __name__ == "__main__":
    unittest.main()