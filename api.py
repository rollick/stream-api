import cherrypy

messages = {
    '1': {
        'text': 'Pull request #76: Smashing new stylez',
        'source': 'github'
    },

    '2': {
        'text': 'Pull request #77: New stuff',
        'source': 'github'
    },

    '3': {
        'text': 'Bart donated 50 bucks',
        'source': 'donations'
    }
}


class Message:

    def GET(self, id=None):

        if id == None:
            result = ('Here are all the messages we have: %s' % messages)
        elif id in messages:
            message = messages[id]
            result = ('Message with the ID %s is called %s, and the artist is %s' % (id, message['text'], message['source']))
        else:
            result = ('No message with the ID %s :-(' % id)

        return result
    
    def POST(self, message):

        id = str(max([int(_) for _ in messages.keys()]) + 1)
        messages[id] = message
        return ('Create a new message with the ID: %s' % id)

    exposed=True

if __name__ == '__main__':

    cherrypy.tree.mount(
        Message(), '/api',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
