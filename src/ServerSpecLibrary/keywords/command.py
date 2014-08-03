from robot.utils import asserts


class CommandKeyword(object):

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
