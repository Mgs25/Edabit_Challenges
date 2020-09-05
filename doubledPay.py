import datetime
def doubled_pay(value):
	Type = type(value).__name__
	dataTypes = {
		'int' :'integer',
		'dict':'dictionary',
		'str' :'string',
	}
	if Type in dataTypes:
		return dataTypes[Type]
	else:
		return Type

print(doubled_pay(({'key': "value"})))