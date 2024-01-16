class Sorter:
    def __init__(self, users):
        # users table
        self.users = users

    def sort_users_by_parameter(self, sort_by, order):
        if sort_by == "age" or not sort_by:
            self.sort_by_age(order)

        elif sort_by == "lang_count":
            for i in self.users:
                i.update_lang_count()
            self.sort_by_lang_count(order)

        elif sort_by == "name":
            self.sort_by_name(order)

        else:
            print(f"Sort by a valid parameter: {sort_by} is not a valid parameter")

    def sort_by_lang_count(self, order):
        if order == "asc":
            arr = self.users
            n = len(arr)

            for i in range(n):
                for j in range(1, n - i):
                    if arr[j - 1].lang_count > arr[j].lang_count:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]

            self.users = arr
        elif order == "desc":
            arr = self.users
            n = len(arr)

            for i in range(n):
                for j in range(1, n - i):
                    if arr[j - 1].lang_count < arr[j].lang_count:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]

            self.users = arr
        else:
            print("Order is not asc or desc")

    def sort_by_age(self, order):
        if order == "asc":
            arr = self.users
            n = len(arr)

            for i in range(n):
                for j in range(1, n - i):
                    if arr[j - 1].user_age > arr[j].user_age:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]

            self.users = arr
        elif order == "desc":
            arr = self.users
            n = len(arr)

            for i in range(n):
                for j in range(1, n - i):
                    if arr[j - 1].user_age < arr[j].user_age:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]

            self.users = arr
        else:
            print("Order is not asc or desc")

    def sort_by_name(self, order):
        def key_func(x):
            return x.user_name

        if order == "asc":

            arr = self.users

            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key_func(key) < key_func(arr[j]):
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            self.users = arr
        elif order == "desc":

            arr = self.users

            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key_func(key) > key_func(arr[j]):
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            self.users = arr
        else:
            print("Order is not asc or desc")
