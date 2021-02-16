import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
user_word = input('Enter a word: ').upper()
wrong_input = True
while wrong_input:
    try:
        phonetic_list = [nato_dict[f'{letter}'] for letter in user_word]
    except KeyError:
        print('Sorry, you must only enter letters in the alphabet')
        user_word = input('Enter a word: ').upper()
    else:
        print(phonetic_list)
        wrong_input = False



