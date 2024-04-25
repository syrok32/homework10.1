from processing import sorting_dict_status, sorting_dict_reverse

user_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

user_config = input()
user_rever = bool(input())

print(sorting_dict_status(user_list, user_config))

print(sorting_dict_reverse(user_list, user_rever))
