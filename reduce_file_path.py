def reduce_file_path(str):
	
	if str == '/':
		return str
	
	path = ''
	list_path = str.split('/')
	temp_list = []

	for i in list_path:
		if i == '' or i == '.':
			continue
		if i == '..' and len(temp_list) != 0:
			temp_list.remove(temp_list[-1])
			continue
		if i == '..':
			continue
		temp_list.append(i)

	temp_str = ''

	if len(temp_list) == 0:
		temp_str = '/'

	for i in temp_list:
		temp_str+='/'
		temp_str+=i


	return temp_str

