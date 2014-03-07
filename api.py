import cherrypy
import mongo


class Messages:

    def GET(self, source=None):
	
	messages = mongo.get_messages_collection()
	result = messages.find_one({"source": source})
	
	#import ipdb; ipdb.set_trace()
	
	if source == None:
	    result = "Here you have all the messages: \n"
	    for message in messages.find():
	    	result += mongo.to_string(message)
		result += "\n ====== \n"
	
	elif result:
	    result = mongo.to_string(message)
	
	else:
	    result = "No messages with the specified ID %s" %source

	return result

    def POST(self, text, tags, source):
        
	#a typical POST request:
	new_message['text'] = text
	new_message['tags'] = tags
	new_message['source'] = source
    	return mongo.put_message(new_message)
    
    exposed=True

if __name__ == '__main__':

    cherrypy.tree.mount(
        Messages(), '/api/messages/',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

