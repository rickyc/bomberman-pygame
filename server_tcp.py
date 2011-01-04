print "[ Bomberman TCP Server ]" 
import os, sys
sys.path.append(os.path.split(sys.path[0])[0])
from Net import *

class ServerHandler(TCPServer):
	def __init__(self):
		TCPServer.__init__(self)
		self.data = []
		self.s_id = 0
		self.users = 0
		self.startGame = False

	def connect_func(self,sock,host,port):
		print "Server successfully connected to %s on port %s!" % (host,port)

	def client_connect_func(self,sock,host,port,address):
		print "A client, (ip: %s, code: %s) connected on port %s!" % (address[0],address[1],port)

	def client_disconnect_func(self,sock,host,port,address):
		print "A client, (ip: %s, code: %s) disconnected from port %s!" % (address[0],address[1],port)

	def add_message(self,message):
		print "data =>" + message
		self.data.append(message)
		if len(self.data) >= 60:
			print 'larger?'
			self.data = self.data[1:]

	def handle_data(self,data):
		action = data[1]
		
		if action == "add message":
			self.s_id += 1
			self.add_message(str(self.s_id)+"|"+data[2])
		elif action == "user joined":
			self.s_id += 1
			self.users += 1
			self.add_message(str(self.s_id)+"|JOIN|"+str(data[2]))
			# event id | action | data ^ in this case random PLAYER ID | array id
		elif action == "user quit":
			self.s_id += 1
			self.users -= 1
			self.add_message(str(self.s_id)+"|QUIT|"+str(data[2]))
		elif action == "movement":
			self.s_id += 1
			self.add_message(str(self.s_id)+"|MOVE|"+str(data[3]) + "|" + str(data[2]))
		elif action == "bomb":
			self.s_id += 1
			self.add_message(str(self.s_id)+"|BOMB|"+str(data[3]) + "|" + str(data[2]))
		elif action == "clear all":
			print "cleared all data"
			self.clearData()
		elif action == "start game":
			self.add_message("[SERVER]|START")
		elif action == "reset ids":
			self.s_id = 0
		
		self.send_data(self.data)

		print len(self.data)
		if len(self.data) > 35:
			self.data = self.data[10:]

	def clearData(self):
		self.data = []

def main():
	server = ServerHandler()
	server.connect("localhost",6317)
	#server.connect("67.23.28.146",6317)
	server.serve_forever()
	server.quit()

if __name__ == '__main__': main()
