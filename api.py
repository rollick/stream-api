import cherrypy


class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True


if __name__ == '__main__':
    root = HelloWorld()
    cherrypy.quickstart(root)

