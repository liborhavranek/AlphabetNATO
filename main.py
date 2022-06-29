import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

result_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(result_dictionary)


def generate_phonetic():
	user_input = input("Your word: ").upper()
	try:
		output_list = [result_dictionary[letter] for letter in user_input]
		print("Thanks to you for use my program")
	except KeyError:
		print("Sorry only alphabet please")
		generate_phonetic()
	else:
		print(output_list)


generate_phonetic()
