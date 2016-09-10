from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from calendar import calendar
from time import sleep


class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        response_body = '<html><body><pre>%s</pre></body></html>' % (calendar(self.year))
        return response_body.encode('utf8')


class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            if int(name) >= 2000:
                sleep(2)
            return YearPage(int(name))
        else:
            return NoResource()

    def render_GET(self, request):
        response_body = '<html><body>Welcome to the calendar server!</body></html>'
        return response_body.encode('utf8')


factory = Site(CalendarHome())
reactor.listenTCP(8080, factory)
print('Starting app on port 8080')

reactor.run()
