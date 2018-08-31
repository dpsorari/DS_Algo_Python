class kmp :
	def __init__(self):
		pass
	
	def PrefixCalculation(self,pattern):
		
		k=0
		p= [0]*len(pattern)
		#p[i] strores the maximum length of prefix which also a suffix ending at i
		for i in range(1,len(pattern)):
			while k>0 and pattern[k]!=pattern[i] : 
				k=p[k-1]
			if pattern[k]==pattern[i]:
				k=k+1
			p[i]=k
		return p

	def contains(self,text,patt):
		'''finite automation function'''
		P=self.PrefixCalculation(patt)
		j=0
		i=0
		while i < len(text):
			if text[i] == patt[j] :
				i+=1
				j+=1
				if j == len(patt):
					print("found")
					return True
				continue
			if j>0: 
				j= P[j-1]
			else :
				i+=1
		return False

