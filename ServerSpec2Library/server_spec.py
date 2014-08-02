import subprocess
from robot.libraries.BuiltIn import BuiltIn
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
        if code != int(expected_code):
            raise AssertionError('expect code %s but was %s' % (expected_code, code))

    def should_return_stdout(self, stdout, expected_output):
        output = stdout.readline()
        if output != expected_output:
            raise AssertionError('expect output %s but was %s' % (expected_output, output))

    def should_return_stderr(self, stderr, expected_output):
        output = stderr.readline()
        if output != expected_output:
            raise AssertionError('expect output %s but was %s' % (expected_output, output))
