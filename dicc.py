class Dicc:
	registros={}
	mnemonicos={}
	
	def __init__(self):
		self.registros={'r01':'0000','r02':'0001','r03':'0002','r04':'0003','r05':'0004','r06':'0005','r07':'0006','r08':'0007','r09':'0008','r10':'0009','r11':'000A','r12':'000B','r13':'000C','r14':'000D','r15':'000E','r16':'000F',}

		self.mnemonicos={'push':'0014','pop':'0015', 'add':['0016','0017','0018','0019'], 'dec':'001A', 'sub':['001B','001C','001D','001E'], 'mul':['001F','0020','0021','0022'], 'div':['0023','0024','0025','0026'], 'inc':'0027', 'CMP':'0028', 'AND':'0029', 'readN':'003B', 'readCh':'003C', 'readS':'002D', 'tff':'003E', 'call':'002F', 'ret':'0030', 'jmpz':'0031', 'mjmpnz':'0032', 'jmp':'0033', 'jmpp':'0034', 'jmpn':'0035', 'test':'002E', 'nop':'002D', 'NOT':'002C', 'xor':'002B', 'OR':'002A','mov':['0010','0011','0012','0013'],'printN':['0036','0037'],'printCh':['0038','0039'],'printS':['003A']}

		
	def GettReg(self):
		return self.registros
	def GettMnemonicos(self):
		return self.mnemonicos


