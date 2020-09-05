def cms_selector(lst, txt):
	result = []	
	for word in lst:
		if word.find(txt) != -1:
			result.append(word)
	return result
print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento" ], "ru"))