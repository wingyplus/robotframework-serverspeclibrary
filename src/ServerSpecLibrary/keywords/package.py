from robot.utils import asserts


class PackageKeyword(object):

    def package(self, name, keyword, *args):
        _, stdout, _ = self.client.exec_command("dpkg-query -f '${Status}' --show %s | grep -E '^install ok installed'" % name)
        found_package = stdout.readline() != ''
        self.builtin.run_keyword(keyword, name, found_package)

    def should_be_installed(self, name, found_package):
        asserts.assert_true(found_package, 'Package %s not found.' % name)

    def should_not_be_installed(self, name, found_package):
        asserts.assert_false(found_package, 'Found package %s' % name)
