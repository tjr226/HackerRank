#! python3

def main():

	test1 = 'hydrochloric'
	test2 = 'rainbowic'
	test3 = 'idontevenknow'
	test4 = 'hydroeatingaloric'
	test5 = 'ttttttttttttic'
	test6 = 'ic'
	test7 = ''

	acidNaming(test7)





def acidNaming(acid_name):

	if acid_name[-2:len(acid_name)] == 'ic':
		if acid_name[0:5] == 'hydro':
			return('non-metal acid')
		else:
			return('polyatomic acid')
	else:
		return('not an acid')




main()