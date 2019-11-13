#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')

info('*** Adding docker containers\n')
node1 = net.addDocker('node1', ip='10.0.0.247', dimage="infoslack/dvwa")
node2 = net.addDocker('node2', ip='10.0.0.248', dimage="szsecurity/mutillidae")
HP3 = net.addDocker('HP3', ip='10.0.0.249', dimage="peakkk/metasploitable")
node4 = net.addDocker('node3', ip='10.0.0.250', dimage="fedora")
node5 = net.addDocker('node4', ip='10.0.0.251', dimage="kalilinux/kali-linux-docker")
node6 = net.addDocker('node5', ip='10.0.0.252', dimage="jvhoof/badstore-docker")
node7 = net.addDocker('node6', ip='10.0.0.253', dimage="ubuntu")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')

info('*** Creating links\n')
net.addLink(node1, node2)
net.addLink(node2, HP3)
net.addLink(node2, s1)
net.addLink(s1, node4)
net.addLink(s1, node6)
net.addLink(node4, node5)
net.addLink(node6, node7)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([node1, node2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()

