from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import time


class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        response_body = 'The local time is %s' % (time.ctime())
        return response_body.encode('utf8')


factory = Site(ClockPage())
reactor.listenTCP(8080, factory)
print('Staring app on port 8080');

reactor.run()
