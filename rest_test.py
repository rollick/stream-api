import cherrypy

songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}

class Songs:

    def GET(self, id=None):

        if id == None:
            result = ('Here are all the songs we have: %s' % songs)
        elif id in songs:
            song = songs[id]
            result = ('Song with the ID %s is called %s, and the artist is %s' % (id, song['title'], song['artist']))
        else:
            result = ('No song with the ID %s :-(' % id)

        return result
    
    def POST(self, title, artist):
	
	# a typical put request
	# curl -d title='Lateralus' -d artist='Tool' -X POST '127.0.0.1:8080/api/songs/'
        
	id = str(max([int(_) for _ in songs.keys()]) + 1)

        songs[id] = {
            'title': title,
            'artist': artist
        }

        return ('Create a new song with the ID: %s' % id)

    exposed=True

if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
