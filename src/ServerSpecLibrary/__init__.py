from ServerSpecLibrary.keywords import ClientKeyword
from robot.libraries.BuiltIn import BuiltIn
from ServerSpecLibrary.keywords import CommandKeyword
from ServerSpecLibrary.keywords import PackageKeyword


class ServerSpecLibrary(ClientKeyword, CommandKeyword, PackageKeyword):

    def __init__(self):
        self.client = None
        self.builtin = BuiltIn()
