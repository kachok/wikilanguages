# -*- coding: utf-8 -*-
# library to work with languages and their properites in relationship to Wikipedia projects

try:
	import pkgutil
	langs_data = pkgutil.get_data(__name__, 'resources/wikilanguages.txt')
	scripts_data = pkgutil.get_data(__name__, 'resources/scripts.txt')
except ImportError:
	import pkg_resources
	langs_data = pkg_resources.resource_string(__name__, 'resources/wikilanguages.txt')
	scripts_data = pkg_resources.resource_string(__name__, 'resources/scripts.txt')


langs={}

# wikilanguages.txt
#№	Language	Language (local)	Wiki	Articles	Total	Edits	Admins	Users	Active Users	Images	Depth	Date	Class

data=langs_data.decode('utf-16')

for i,line in enumerate(data.split('\n')):
	#skip headers
	if i==0: pass

	line=line.strip()
	tabs=line.split('\t')
	
	lang=tabs[3]
	number=tabs[0]
	name=tabs[1]
	native_name=tabs[2]
	articles=tabs[4]
	active_users=tabs[9]
	size=tabs[13]
	
	langs[lang]={"number":number, "name":name, "native_name":native_name, "stats":{"articles":articles, "active_users":active_users}, "size":size}

# scripts.txt
#№	Language	Wiki	Direction	Non-latin	Rendering	Constructed

data=scripts_data.decode('utf-16')

for i, line in enumerate(data.split('\n')):
	#skip headers
	if i==0: pass
	
	line=line.strip()
	tabs=line.split('\t')
	
	lang=tabs[2]
	direction=tabs[3]
	non_latin=tabs[4]
	rendering=tabs[5]
	constructed=tabs[6]
	
	langs[lang]["script"]={"direction":direction, "non_latin": non_latin, "rendering":rendering, "constructed":constructed}


#print langs