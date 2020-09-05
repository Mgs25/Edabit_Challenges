def get_discounts(nums, d):
    return [x*int(d.replace('%',""))/100 for x in nums]
print(get_discounts([2, 4, 6, 11], "50%"))
