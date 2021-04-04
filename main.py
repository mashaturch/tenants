"""Программа нужна для сортировки данных о жильцах дома. На вход подаются данные о жильцах.
Затем пользователю задаются 5 вопросов. Он выбирает один, на который ему нужен ответ
(он хочет узнать про жителей какой-то квартиры, получить список всех жильцов в алфавитном порядке,
список квартир, которые что-то должны, разультаты голосования или домашний телефон какой-то квартиры).
После того, как пользователь отвечает на вопрос, то в другом файле выводится нужная информация.

"""

"""Obtaining data about tenants of the house """

def questions (list_of_residents, list_debtor, list_phones, decision_making, list_of_tenants_alphabet):
    """Questions and answers for the user """
    question_1 = '1) Кто живёт в определённой квартре?'
    question_2 = '2) Список всех жильцов в алфавитном порядке?'
    question_3 = '3) Список квартир, которые что-то должны?'
    question_4 = '4) Результаты голосования насчёт постройки футбольного поля?'
    question_5 = '5) Номер домашнего телефона определённой квартиры?'
    print ('Что вы бы хотели узнать?')
    print (question_1, question_2, question_3, question_4, question_5, sep = '\n')
    answer = int (input())
    with open ('answer_output.txt', 'w', encoding = 'utf-8') as f_ans:
        if answer == 1:
            n = int (input ('Насчёт какой квартиры вы бы хотели узнать? '))
            print('В квартире номер', n, 'живут:', end = ' ', file = f_ans)
            for i in range (len(list_of_residents[n - 1]) - 1):
                print (list_of_residents[n-1][i], end = ', ', file = f_ans)
            print (list_of_residents[n-1][len(list_of_residents[n-1]) - 1], file = f_ans)
        if answer == 2:
            print ('Список всех жильцов дома в алфавитном порядке:', file = f_ans)
            for name in list_of_tenants_alphabet:
                print (name, file = f_ans)
        if answer == 3:
            print ('Список всех квартир-должников дома:', file = f_ans)
            for apartment in list_debtor:
                print (apartment, file = f_ans)
        if answer == 4:
            print (decision_making, file = f_ans)
        if answer == 5:
            n = int(input('Насчёт какой квартиры вы бы хотели узнать? '))
            print ('Домашний телефон квартиры номер', n, ': ', end = '', file = f_ans )
            print (list_phones[n - 1], file = f_ans)


with open ('input.txt', encoding = 'utf-8') as f_in:
    list_of_residents = [] # House tenants list
    list_debtor = [] # House debtors list
    list_phones = [] # Household Phones List
    vote = [] # List for voices of the house
    apartment = [] # List for residents of one apartment
    list_of_tenants_alphabet = [] # List of apartment tenants in alphabetical order
    list_information = [] # List with all file data

    # Filling out the list with all the data at home
    for lines in f_in:
        line = lines[:len(lines) - 1]
        if line != '':
            list_information.append(line)
    # Finding the index of a specific line in a file
    number_phone = list_information.index('Домашние телефоны:')
    number_debt = list_information.index('Долг квартир:')
    number_vote = list_information.index('Голосование:')
    number = 1

    # Filling out the list with tenants by apartment
    for i in range (1, number_phone):
        apartment_number, full_name = list_information[i].split(' - ')
        list_of_tenants_alphabet.append(full_name)
        if number != int(apartment_number):
            list_of_residents.append(apartment)
            number += 1
            apartment = []
        apartment.append(full_name)
    list_of_residents.append(apartment)
    list_of_tenants_alphabet.sort()

    # Filling in the list of home phones for each apartment
    for i in range (number_phone + 1, number_debt):
        apartment_number, phone = list_information[i].split(' - ')
        list_phones.append(phone)

    # Filling out the list of debtors
    for i in range (number_debt + 1, number_vote):
        apartment_number, debt = list_information[i].split(' - ')
        if debt == 'долг':
            list_debtor.append(apartment_number)

    # Determination of the voting result
    for i in range (number_vote + 1, len(list_information)):
        apartment_number, vote_apartment = list_information[i].split(' - ')
        vote.append(vote_apartment)
    number_of_votes_consent = vote.count('за')
    number_of_votes_disagreement = len(vote) - number_of_votes_consent
    if number_of_votes_consent > number_of_votes_disagreement:
        decision_making = 'Большинство людей за постройку футбольного поля.'
    elif number_of_votes_consent < number_of_votes_disagreement:
        decision_making = 'Большинство людей против постройки футбольного поля.'
    else:
        decision_making = 'Жильцы не смогли принять общего решения, поэтому будет переголосование.'

    # Calling a function with questions
    questions(list_of_residents, list_debtor, list_phones, decision_making, list_of_tenants_alphabet)


