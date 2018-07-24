import logging

from lib.execution_wrapper import ExecutionWrapper

logging.getLogger().setLevel(logging.INFO)


class TestFramework:

    def __init__(self):
        self.execution_wrapper = ExecutionWrapper()

    def install_pkg(self, pkg_name, input_option):
        logging.info("Installing {} pkg".format(pkg_name))

        args = ['apt-get', 'install', pkg_name]
        return self.execution_wrapper.execute_command_with_option(args, input_option)

    def upgrade_apt_get(self):
        logging.info("Upgrading apt-get")

        return self.execution_wrapper.execute_command(['apt-get', 'upgrade', '-y'])

    def update_apt_get(self):
        logging.info("Updating apt-get")

        return self.execution_wrapper.execute_command(['apt-get', 'update', '-y'])

    def remove_pkg(self, pkg_name):
        logging.info("Removing {} pkg".format(pkg_name))

        args = ['apt-get', 'remove', pkg_name, '-y']
        return self.execution_wrapper.execute_command(args)

    def get_installed_pkg_list(self):
        logging.info("Getting list of installed pkg's")

        return self.execution_wrapper.execute_command(['apt', 'list', '--installed'])

    def get_pkg_pwd(self, pkg_name):
        logging.info("Checking pwd and status for {} pkg".format(pkg_name))

        args = ["which", pkg_name]
        return self.execution_wrapper.execute_command(args)

    def check_pkg_version(self, pkg_name):
        logging.info("Checking version of {} pkg".format(pkg_name))

        try:
            version = self.execution_wrapper.execute_command_popen(
                "apt-cache policy {} | grep 'Installed' | awk '{{ print $2; }}'".format(pkg_name))
            return version.decode("utf-8").rstrip()
        except Exception as e:
            logging.error(e, exc_info=True)
            return False
