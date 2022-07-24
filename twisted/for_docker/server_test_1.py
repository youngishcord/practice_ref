from twisted.internet import reactor, protocol
from twisted.internet.protocol import Protocol, connectionDone
from twisted.internet.protocol import ServerFactory as ServFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(Protocol):
    def __init__(self, users):
        self.name = ""
        self.users = users

    def connectionMade(self):
        print('New connection')
        self.transport.write('Hellow from server'.encode())
        

    def add_user(self, name):
        if name not in self.users:
            self.users[self] = name
            self.name = name
        else:
            self.transport.write("wrong user name".encode())
        
    def dataReceived(self, data):
        data = data.decode()

        if not self.name:
            self.add_user(data)

        for protocol in self.users.keys():
            if protocol != self:
                protocol.transport.write(f"{self.name}: {data}".encode())

    def connectionLost(self, reason = connectionDone):
        del self.users[self]


class ServerFactory(ServFactory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return Server(self.users)



if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()