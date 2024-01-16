import user as us
import sorter as sr
import pprint


def average_value(arr):
    elements_sum = 0
    for k in arr:
        elements_sum += k
    return elements_sum / len(arr)


def check_if_age_is(op, age, number):
    if op == "greater":
        return age > number
    elif op == "smaller":
        return age < number
    else:
        print("Wrong operator")
        return None


def starts_with(letter, string):
    return string[0] == letter


def users_init():
    users_arr = [
        us.User("Jakub", 15, ["Python", "Lua", "Javascript", "C++", "Php"], True),
        us.User("Bartosz", 13, ["Python", "Go", "Rust", "Lua", "Javascript", "Assembly", "C", "Java", "C++", "Php",
                                "Html", "Css", "Luaua", "Typescript"], True),
        us.User("Zygmunt", 31, ["Lua", "Cobol", "C", "Php"], False),
        us.User("Piotr", 16, ["Python", "Javascript", "C++", "Php", "Gimp", "Blender"], True),
        us.User("Szymon", 24, ["Python", "Javascript", "Css"], True),
        us.User("Zbigniew", 69, ["Lua", "Assembly", "Go", "Php"], False),
        us.User("Paweł", 15, ["Python"], True),
        us.User("Stanisław", 72, ["Python", "Lua", "Javascript", "C++", "Php", "Cobol", "C"], False)
    ]
    return users_arr


users = users_init()

print("Oni znają Pythona: ")
for i in users:
    if "Python" in i.user_languages:
        i.info()

print("Oni są nieaktywni (imie, wiek):")
for i in users:
    if not i.user_is_active:
        print(f"Info: {i.user_name} {i.user_age}")

print("Oni znają co najmniej trzy języki: ")
for i in users:
    if i.lang_count >= 3:
        lang_str = ""
        for j in i.user_languages:
            lang_str += j + " "
        print(f"Info: {i.user_name} {lang_str}")

print("Średni wiek aktywnych użytkowników: ")
age_active_arr = []
age_inactive_arr = []
for i in users:
    if i.user_is_active:
        age_active_arr.append(i.user_age)
    else:
        age_inactive_arr.append(i.user_age)

print(average_value(age_active_arr))

print("Średni wiek nieaktywnych użytkowników: ")
print(average_value(age_inactive_arr))

print("Trzy najbardziej edukowane osoby: ")
sorter = sr.Sorter(users)
sorter.sort_users_by_parameter("lang_count", "desc")
for i in range(0, 3):
    lang_str = ""
    for j in sorter.users[i].user_languages:
        lang_str += j + " "
    print(f"{i + 1}. {sorter.users[i].user_name} {lang_str}")

print("Posortowani: \n Alfabetycznie: ")
sorter.sort_users_by_parameter("name", "asc")
for i in sorter.users:
    i.info()

print(" Przeciwnie do alfabetycznego:")
sorter.sort_users_by_parameter("name", "desc")
for i in sorter.users:
    i.info()

lang_count_arr = []
for i in users:
    lang_count_arr.append(i.lang_count)

print("Użytkownik zna średnio: ", average_value(lang_count_arr), " technologii.")

print("To jest grupa, która zan python: ")
not_python_group = []
for i in users:
    if "Python" in i.user_languages:
        i.info()
    else:
        not_python_group.append(i)

print("Grupa nie znająca python:")
for i in not_python_group:
    i.info()

print("Czy wszyscy są starsi niż 18 lat?")
are_older = True
for i in users:
    if check_if_age_is("smaller", i.user_age, 18):
        print("Nie wszyscy są starsi od 18 lat")
        are_older = False
        break

if are_older:
    print("Wszyscy są starsi od 18 lat")

print("Czy isnieje użytkownik starszy od 30 lat? ")
is_older = False
for i in users:
    if check_if_age_is("greater", i.user_age, 30):
        print("Isnieje starszy od 30 lat, np:", i.user_name)
        is_older = True
        break

if not is_older:
    print("Nie isnieje")

print("Najstarszy użytkownik znający Go: ")
max_age = users[0]
for i in users:
    if i.user_age > max_age.user_age and "Go" in i.user_languages:
        max_age = i

max_age.info()

print("Użytkownicy, którzy znają technologię na c: ")
has_lang_that_starts_with_a_letter = False
for i in users:
    has_lang_that_starts_with_a_letter = False
    for j in i.user_languages:
        if starts_with("C", j):
            has_lang_that_starts_with_a_letter = True
    if has_lang_that_starts_with_a_letter:
        i.info()

print("Słownik: ")
users_dict = {}
for i in users:
    users_dict.update({i.user_name: i.lang_count})
pprint.pprint(users_dict)
