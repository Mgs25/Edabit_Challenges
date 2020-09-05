def progress_bar(bar, progress):
	return '|'+(' '*10).replace(' ',bar,int(progress/10))+'| Progress: {}%'.format(progress)

print(progress_bar("=", 40))