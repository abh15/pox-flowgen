#A script to create custom POX flows
#http://github.com/abh15/pox-flowgen

#import random
#fname="poxscript_"+str(random.randint(1000,9999))+".py"
#uncomment above lines if each script with a new name is required
fname="controllerScript.py"
file=open(fname,'w')
file.close()		
#----create a new empty file----

target=open(fname,'w')
target.write("\"\"\"\nScript created by POX custom flow generator (PCFG)\n\"\"\"\n")
target.write("from pox.core import core \nfrom pox.lib.addresses import IPAddr \nfrom pox.lib.addresses import EthAddr \nimport pox.openflow.libopenflow_01 as of")
target.write("\nlog = core.getLogger()\n")
#----print importing


def check(): #call match again or exit depending on if i/p is A or M
	f=raw_input("Enter A to move to action\nM to stay in match menu\n>") 
	if f=="M":
    	
		print t
		q=raw_input(">")
		match(int(q))
	else:
		pass
#---check if want to stay in match menu i.e to create multiple matches-----
def check2(str1,str2): #call actions again or exit depending on if i/p is A or N
	global msg
	msg.append(str1+str2)  				#create/concat array of all used actions
	f=raw_input("Enter A to stay in action\nF to create Flow\n>")
	if f=="A":
    	
		print t2
		q=raw_input(">")
		actions(int(q))
	else:
		pass 
#---check if want to stay in action menu i.e to create multiple actions----


def checkflows():
	
	global fooflows
	
	fooflows=fooflows-1
	
	if fooflows>0:
		fl()
	else:
		
		checkswitch()	
#-------keeps in flow menu alive until all flows are specified---------

def checkswitch():
	
	global foox
	
	foox=foox-1
	if foox>0:
		switch()
		fl()
	else:
		pass
#-------keeps in switch/flow menu until all switches/flows are specified---------		

def match(k):
	global name
	name=bar[int(fl_no)] #flow name of current instance
	

	def inport():
		f=raw_input("Enter inport>")
		target.write(name+"msg.match.in_port="+str(f)+"\n")
		check()					#check if more matching actions are going to be added
		
	def dltype():
		f=raw_input("Enter dltype>")
		target.write(name+"msg.match.dl_type="+str(f)+"\n")
		check()

	def nwtos():
		f=raw_input("Enter nwtos>")
		target.write(name+"msg.match.nw_tos="+str(f)+"\n")
		check()

	def nwproto():
		f=raw_input("Enter nwproto>")
		target.write(name+"msg.match.nw_proto="+str(f)+"\n")
		check()

	def nwsrc():
		f=raw_input("Enter nwsrc>")
		target.write(name+"msg.match.nw_src=IPAddr(\""+f+"\")\n")
		check()

	def nwdst():
		f=raw_input("Enter nwdst>")
		target.write(name+"msg.match.nw_dst=IPAddr(\""+f+"\")\n")
		check()

	def dlvlan():
		f=raw_input("Enter dlvlan>")
		target.write(name+"msg.match.dl_vlan="+str(f))
		target.write("\n")
		check()

	def dlvlanpcp():
		f=raw_input("Enter dlvlanpcp>")
		target.write(name+"msg.match.dl_vlan_pcp="+str(f))
		target.write("\n")
		check()

	def dlsrc():
		f=raw_input("Enter dlsrc>")
		target.write(name+"msg.match.dl_src = EthAddr(\""+f+"\")\n")
		check()

	def dldst():
		f=raw_input("Enter dldst>")
		target.write(name+"msg.match.dl_dst = EthAddr(\""+f+"\")\n")
		check()

	def tpsrc():
		f=raw_input("Enter tpsrc>")
		target.write(name+"msg.match.tp_src="+str(f))
		target.write("\n")
		check()

	def tpdst():
		f=raw_input("Enter tp dst>")
		target.write(name+"msg.match.tp_dst="+str(f))
		target.write("\n")
		check()

	def priority():
		f=raw_input("Enter priority>")
		target.write(name+"msg.priority="+str(f))
		target.write("\n")
		check()	

	options={1:inport,2:dltype,3:nwtos,4:nwproto,5:nwsrc,
	6:nwdst,7:dlvlan,8:dlvlanpcp,9:dlsrc,10:dldst,11:tpsrc,12:tpdst,13:priority}	#func_dictionary
	
	target.write("\n#"+name+" Match structure\n")    
	target.write(baz[int(sw_no)]+"="+dpid+"\n")  	#write dpid
	target.write(name+"msg = of.ofp_flow_mod()\n")
	target.write(name+"msg.cookie = 0\n")
	options[k]()									#call the k'th function depending upon user input

#----------matching structure---------
def actions(k):
	name=bar[int(fl_no)]           #name of current flow instance

	def vlan_id():
		
		v=raw_input("Enter vlan id>")
		target.write(name+"vlan_id = of.ofp_action_vlan_vid (vlan_vid="+str(v)+")")
		target.write("\n")
		check2(name,"vlan_id")							#check if more actions are going to be added

	def stripvlan():
		v=raw_input("Enter stripvlan yes or no>")
		if v=="yes":
			target.write(name+"stripvlan = of.ofp_action_strip_vlan ()")
			target.write("\n")
		else:
			target.write("\n")	
		check2(name,"stripvlan")		

	def out():
		v=raw_input("Enter out port>")
		target.write(name+"out = of.ofp_action_output(port ="+str(v)+")")
		target.write("\n")
		check2(name,"out")

	def vlanPriority():
		v=raw_input("Enter vlan priority>")
		target.write(name+"vlanPriority = of.ofp_action_vlan_pcp (vlan_pcp="+str(v)+")")
		target.write("\n")
		check2(name,"vlanPriority")

	def enqueue():
		v=raw_input("Enter enq>")
		target.write(name+"flow0enqueue = of.ofp_action_enqueue (enqueue = "+str(v)+")")
		target.write("\n")
		check2(name,"enqueue")


	def srcPort():
		v=raw_input("Enter srcport>")
		target.write(name+"srcPort = of.ofp_action_tp_port.set_src = (tp_port = "+str(v)+")")
		target.write("\n")
		check2(name,"srcPort")

	def dstPort():
		v=raw_input("Enter destport>")
		target.write(name+"dstPort = of.ofp_action_tp_port.set_dst = (tp_port = "+str(v)+")")
		target.write("\n")
		check2(name,"dstport")

	def srcMAC():
		v=raw_input("Enter src MAC add>")
		target.write(name+"srcMAC = of.ofp_action_dl_addr.set_src(EthAddr(\""+str(v)+"\"))")
		target.write("\n")
		check2(name,"srcMAC")

	def dstMAC():
		v=raw_input("Enter dst MAC add>")
		target.write(name+"dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr(\""+str(v)+"\"))")
		target.write("\n")
		check2(name,"dstMAC")

	def srcIP():
		v=raw_input("Enter source IP>")
		target.write(name+"srcIP = of.ofp_action_nw_addr.set_src(IPAddr(\""+str(v)+"\"))")
		target.write("\n")
		check2(name,"srcIP")

	def dstIP():
		v=raw_input("Enter dstIP>")
		target.write(name+"dstIP = of.ofp_action_nw_addr.set_dst(IPAddr(\""+str(v)+"\"))")
		target.write("\n")	
		check2(name,"dstIP")

	def tos():
		v=raw_input("Enter tos>")
		target.write(name+"tos = of.ofp_action_nw_tos (nw_tos = "+str(v)+")")
		target.write("\n")
		check2(name,"tos")	

	options={1:vlan_id,2:stripvlan,3:out,4:vlanPriority,5:enqueue,
	6:srcPort,7:dstPort,8:srcMAC,9:dstMAC,10:srcIP,11:dstIP,12:tos}
	
	
	options[k]()             #select action based on user input
#----------actions structure---------	

global foox
x=raw_input("Enter no. of switches\n>")
foox=int(x)
y=[]
baz=[]
msg=[]
bar=[]

#------------main------------
def switch():						#get number of switches,flows & dpid
	global fooflows
	global baz
	global y
	global sw_no
	global dpid 
	global flows
	print "Select switch:\n"
	for i in xrange(0,int(x)):
		print str(i)+":"+"\tswitch"+str(i)
		baz.append("switch"+str(i))
	
	sw_no=raw_input(">")
	tbp=raw_input("Enter DPID of switch(a hex no.)\n>")
	dpid=oct(int(str(int(tbp,16))))
	flows=raw_input("Enter no of flows\n>")
	fooflows=int(flows)						#used for checkswitch func, possibly buggy
	y.append(int(flows)) 					#create list of no. of flowmsgs per switch for sendToDPID msgs

#----------switch structure------------

def fl():							#display available match/actions & get them 
	global msg
	global bar
	global fl_no
	global t
	global t2
	global q
	
	print "Select flow:\n"						#display flows to choose from
	for i in xrange(0,int(flows)):
		print str(i)+":"+"\tflow"+str(sw_no)+"_"+str(i)
		bar.append("flow"+str(sw_no)+"_"+str(i))

	fl_no=raw_input(">")
	
	t= "\n1:inport\n2:dltype\n3:nwtos\n4:nwproto\n5:nwsrc\n6:nwdst\n7:dlvlan\n8:dlvlanpcp\n9:dlsrc\n10:dldst\n11:tpsrc\n12:tpdstn\n13:Priority"
	print t                 #choose a match & call match func
	q=raw_input(">")
	match(int(q))
	#----------------end match
	
	t2="1:vlanid\n2:stripvlan\n3:outport\n4:vlanprior\n5:enqueue\n6:srcport\n7:dstport\n8:srcmac\n9:dstmac\n10:srcip\n11:dstip\n12:tos"
	print t2
	w=raw_input(">")								

	target.write("# ACTIONS----------------\n")
	actions(int(w)) 												#choose a action & call action func
	target.write(name+"msg.actions="+str(msg).replace('\'','')+"\n")   #print the msg arrsy containing actions used
	msg=[]
	#--------end actions
	checkflows()	#check for more flows 

#-----------flows structure------------

switch()
fl()
#call functions in first iteration


target.write("\ndef install_flows(): \n\tlog.info(\"  ### Installing static flows... ###\")\n")  
for i in xrange(0,int(x)):
	for j in xrange(0,y[i]):
	   target.write("\tcore.openflow.sendToDPID(switch"+str(i)+",flow"+str(i)+"_"+str(j)+"msg)\n")
target.write("\tlog.info(\"### Static flows installed. ###\")\n")
#---print function to install flows----- 


target.write("def launch (): \n\tlog.info(\"####Starting...####\")\n\tcore.callDelayed (15, install_flows)\n\tlog.info(\"### Waiting for switches to connect.. ###\")")
#---print the launch function----- 
target.close() #save file
print "Done :)"
