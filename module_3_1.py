calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    string = str(string)
    output = (len(string), string.upper(), string.lower())
    print(output)
    count_calls()


def is_contains(string, list_to_search):
    count_calls()
    string = str(string)
    string = string.lower()
    list_to_search = list(list_to_search)
    for i in range(0, len(list_to_search)):
        list_to_search[i] = str(list_to_search[i])
        list_to_search[i] = list_to_search[i].lower()
    print(list_to_search.__contains__(string))


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
