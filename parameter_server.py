from twisted.internet import protocol, reactor, endpoints

import time


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class Echo_udp(protocol.DatagramProtocol):
    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        self.transport.write(data, addr)
        time.sleep(3)
        self.transport.write(b'2nd' + data, addr)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.listenUDP(1234, Echo_udp())
reactor.run()
