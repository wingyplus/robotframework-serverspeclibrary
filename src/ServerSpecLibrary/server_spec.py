import subprocess
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import asserts
from paramiko import client


class ServerSpecLibrary(object):
    def __init__(self):
        self.client = None
        self.builtin = BuiltIn()

    def connect_to_server(self, hostname, username, password):
        self.client = client.SSHClient()
        self.client.load_system_host_keys()
        self.client.connect(hostname=hostname, username=username, password=password)

    def close_connection(self):
        self.client.close()

    def command(self, cmd, name, *args):
        _, stdout, stderr = self.client.exec_command(cmd)
        if name == 'Should Return Stdout':
            self.builtin.run_keyword(name, stdout, *args)
        else:
            self.builtin.run_keyword(name, stderr, *args)

    def should_return_exit_status(self, stdout, expected_code):
        code = stdout.channel.recv_exit_status()
        asserts.assert_equals(int(expected_code), code)

    def should_return_stdout(self, stdout, expected_output):
        output = stdout.readline()
        asserts.assert_equals(expected_output, output)

    def should_return_stderr(self, stderr, expected_output):
        output = stderr.readline()
        asserts.assert_equals(expected_output, output)

    def package(self, name, keyword, *args):
        _, stdout, _ = self.client.exec_command("dpkg-query -f '${Status}' --show %s | grep -E '^install ok installed'" % name)
        found_package = stdout.readline() != ''
        self.builtin.run_keyword(keyword, name, found_package)

    def should_be_installed(self, name, found_package):
        asserts.fail_unless(found_package, 'Package %s not found.' % name)

    def should_not_be_installed(self, name, found_package):
        asserts.fail_if(found_package, 'Found package %s' % name)
