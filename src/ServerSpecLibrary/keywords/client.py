from paramiko import client


class ClientKeyword(object):

    def connect_to_server(self, hostname, username, password):
        self.client = client.SSHClient()
        self.client.load_system_host_keys()
        self.client.connect(hostname=hostname, username=username, password=password)

    def close_connection(self):
        self.client.close()
