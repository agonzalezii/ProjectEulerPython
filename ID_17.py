fourth_digit_suffix_count = len("thousand")
third_digit_suffix_count = len("hundred")
and_count = len("and")
teens_count_table = {10:len("ten"), 
					11:len("eleven"),
					12:len("twelve"),
					13:len("thirteen"),
					14:len("fourteen"),
					15:len("fifteen"),
					16:len("sixteen"),
					17:len("seventeen"),
					18:len("eighteen"),
					19:len("nineteen")}

tens_digit_count_table = {2:len("twenty"), 
					3:len("thirty"),
					4:len("forty"),
					5:len("fifty"),
					6:len("sixty"),
					7:len("seventy"),
					8:len("eighty"),
					9:len("ninety")}

digit_name = {
	1: len("one"),
	2: len("two"),
	3: len("three"),
	4: len("four"),
	5: len("five"),
	6: len("six"),
	7: len("seven"),
	8: len("eight"),
	9: len("nine"),
}

def get_letters_in_number(number):
	letter_count = 0
	
	thousands = int(number/ 1000)
	if(thousands > 0):
		letter_count += digit_name[thousands]
		letter_count += fourth_digit_suffix_count

		
	
	hundreds = int((number%1000) /100)
	if(hundreds > 0):
		letter_count += third_digit_suffix_count
		letter_count += digit_name[hundreds]

	tens = int((number%100)/10)
	ones = number % 10
	if(thousands > 0 or hundreds > 0):
		if(ones > 0 or tens > 0):
			letter_count += and_count

	if(tens > 0):
		if(tens == 1):
			letter_count += teens_count_table[number%100]
			#print(number, letter_count)
			return letter_count
		letter_count += tens_digit_count_table[tens]

	if(ones > 0):
		letter_count += digit_name[ones]
	return letter_count

total_count = 0
for i in range(1,1001):
	letter_count = get_letters_in_number(i)
	total_count += letter_count
	#print((i, letter_count))
print(total_count)
