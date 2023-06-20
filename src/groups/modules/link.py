class Link():
    """
    A class to represent a link to a decentralized object.
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.blockchain = None
        self.blockchain_id = None
        self.blockchain_address = None
        self.blockchain_network = None
        self.blockchain_status = None
        self.blockchain_transaction = None
        self.smart_contract = None

