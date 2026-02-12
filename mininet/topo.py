from mininet.topo import Topo

class MyTopo(Topo):
	def build(self):
		h1 = self.addHost('h1')	#Normal user
		h2 = self.addHost('h2')	#Normal user
		h3 = self.addHost('h3')	#attacker
		s1 = self.addSwitch('s1')

		self.addLink(h1, s1)
		self.addLink(h2, s1)
		self.addLink(h3, s1)

topos = {'mytopo' : (lambda: MyTopo())}


