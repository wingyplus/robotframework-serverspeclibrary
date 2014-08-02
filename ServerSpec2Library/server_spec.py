import subprocess
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import asserts
from paramiko import client


class ServerSpec2Library(object):
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
        package = True
        self.builtin.run_keyword(keyword, package, *args)

    def should_be_installed(self, package, *args):
        asserts.fail_if_none(package)
