class category_disabler:
	cat_all_str = list()
	cat_in_str = list()
	cat_mask = list()
	global_cat_mask = list()

		
	@staticmethod
	def generate_mask():
		cat_mask = list()
		for e in category_disabler.cat_all_str:
			if e in category_disabler.cat_in_str:
				cat_mask.append(1)
			else:
				cat_mask.append(0)

		category_disabler.global_cat_mask = list(cat_mask)

	@staticmethod
	def cat_all_regist(cat_all):
		category_disabler.cat_all_str = cat_all

	@staticmethod
	def cat_in_regist(cat_in):
		category_disabler.cat_in_str = cat_in
		category_disabler.generate_mask()


