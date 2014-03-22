class Url():
    SCHEME_FILE = "file"

    def __init__(self, scheme, domain, resource, port=None):
        self.scheme = scheme
        self.domain = domain
        self.port = port
        self.resource = resource

    def get_scheme(self):
        return self.scheme

    def get_domain(self):
        return self.domain

    def get_resource(self):
        return self.resource

    def get_url(self):
        port_string = ""
        if self.port is not None:
            port_string = ":" + self.port
        return self.scheme + ":" + self.domain + port_string + "/" + self.resource

    def get_port(self):
        if self.port is None:
            return ""
        return self.port