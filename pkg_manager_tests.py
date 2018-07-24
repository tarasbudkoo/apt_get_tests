import logging
import unittest

from lib.apt_get_wrapper import TestFramework

logging.getLogger().setLevel(logging.INFO)


class PKGManagerTests(unittest.TestCase):
    def setUp(self):
        self.test_framework = TestFramework()
        self.test_framework.update_apt_get()
        self.test_framework.upgrade_apt_get()

    def tearDown(self):
        pass

    def test_simple_install(self):
        pkg_name = 'tircd'

        self.test_framework.install_pkg(pkg_name, 'y')

        pkg_status = self.test_framework.get_pkg_pwd(pkg_name)
        pkg_version = self.test_framework.check_pkg_version(pkg_name)

        self.assertEqual(0, pkg_status[0])
        self.assertTrue(pkg_version)

    def test_install_and_remove_with_version(self):
        pkg_name = "nmap"
        pkg_version = "6.47-3+deb8u2"

        self.test_framework.install_pkg(pkg_name + "=" + pkg_version, 'y')

        pkg_status = self.test_framework.get_pkg_pwd(pkg_name)
        pkg_version = self.test_framework.check_pkg_version(pkg_name)

        self.assertEqual(0, pkg_status[0])
        self.assertEqual(pkg_version, "6.47-3+deb8u2")

        self.test_framework.remove_pkg(pkg_name)

        new_pkg_status = self.test_framework.get_pkg_pwd(pkg_name)
        new_pkg_version = self.test_framework.check_pkg_version(pkg_name)

        self.assertEqual(1, new_pkg_status[0])
        self.assertEqual("(none)", new_pkg_version)

    def test_installation_interrupt(self):
        pkg_name = "tinyproxy"

        self.test_framework.install_pkg(pkg_name, 'n')

        pkg_status = self.test_framework.get_pkg_pwd(pkg_name)
        pkg_version = self.test_framework.check_pkg_version(pkg_name)

        self.assertEqual(1, pkg_status[0])
        self.assertEqual("(none)", pkg_version)

    def test_install_with_update(self):
        pkg_name = "subversion-tools"

        pkg_version_1 = "1.8.10-6+deb8u5"
        pkg_version_2 = "1.8.10-6+deb8u6"

        pkg_status = self.test_framework.get_pkg_pwd(pkg_name)
        self.assertEqual(1, pkg_status[0])

        self.test_framework.install_pkg(pkg_name + "=" + pkg_version_1, 'y')
        self.assertEqual(pkg_version_1, self.test_framework.check_pkg_version(pkg_name))

        self.test_framework.install_pkg(pkg_name + "=" + pkg_version_2, 'y')
        self.assertEqual(pkg_version_2, self.test_framework.check_pkg_version(pkg_name))

        self.test_framework.remove_pkg(pkg_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
