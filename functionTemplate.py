"""
author: ankit anand
created on: ___DATE___
"""

from FBC import FBC

class ___FILEBASENAME___(FBC):
	"""
	<##>
	
	inps
	----
	
	
	outs
	----
	
	
	"""
	
	def __init__(self):
		"""set parameters"""
		super().__init__() # pass the parameters as kwargs
	
	
	def test(self):
		"""runs custom tests on function"""
		
		pass
				
	def validate(self):
		"""validate inputs"""
		
		for k, v in self.inps.items(): # validating if input is passed
			if v is None:
				raise PermissionError(f"inputs ({k}) need to be initialized before calling run")
		
			
	def run(self, debugMode=False):
		"""main implementation of the code"""
		
		self.ran = True # flag to check if run command was called
		self.debugMode = debugMode # turn on debug mode
		self.validate() # inputs validation
		
		# INPS EXTRACTION
		
		
		# LOGIC IMPLEMENTATION
		pass
		
		# OUPUTS
		
		
		# DEBUGS
		if self.debugMode:
			self.debugs = {} # add all the debug varibles
			
		return self
	
	def plot(self, show=False):
		"""plot to debug"""
		
		if not self.ran:
			raise PermissionError("run method needs to be called before plotting")
			
		pass
		
	def save(self, outputPath=None):
		"""save debug/output files"""
		
		from pathlib import Path
		
		if not self.ran:
			raise PermissionError("run method needs to be called before saving output")
		if outputPath is None:
			raise ValueError("outputPath can't be None")
		if isinstance(outputPath, str):
			outputPath = Path(outputPath)
		if not outputPath.exists():
			outputPath.mkdir(exist_ok=True, parents=True) 
			
		pass