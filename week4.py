# a = 1
# try:
#     b = int(input("Give us the number: "))
#     a = a/b
# except ZeroDivisionError:
#     print("Impossible divide by 0")
# except ValueError:
#     print("Invalid value")
# except:
#     print("Something went wrong")
# else:
#     print(f"Result: {a}")
# finally:
#     print(f"Processing Completed")
# ==================================================================================
# def main():
#     sample_dict = {'a': 1, 'b': 2, 'c': 3}

#     result1 = dict_get_value(sample_dict,"b")
#     result2 = dict_get_value(sample_dict,"g")

#     print(result1)
#     print(result2)

# def dict_get_value(dictionary, key):
#     try:
#         value = dictionary[key]
#     except KeyError:
#         return "Key not found"
#     else:
#         return value
# main()
# ==================================================================================
# def main():
#     numbers_list = [15, 62, 17, 85, 8]
#     test_list = []
#     print(get_average(test_list))
#     print(f"{get_average(numbers_list):.2f}")

# def get_average(data):
#     try:
#         # if not data:
#         #     raise ValueError("Data is Empty")
#         return sum(data)/len(data)
#     except ZeroDivisionError:
#         return "Data is Empty"
# main()
# ==================================================================================
# def main():
#     try:
#         amount = int(input("What is the amount: "))
#         years = int(input("What is the years: "))
#         percent = int(input("What is the percentage: "))

#     except ValueError as a:
#         print(f"Wrong Value {a}")
#     else:
#         print(calculate_interest(amount, years, percent))


# def calculate_interest(amount, years, percent):
#     try:
#         if percent > 100:
#             raise ValueError
#         result = (amount * years * percent)/100
#         return result
#     except:
#         return "Percent is grater then 100"

# main()
# ==================================================================================
# def main():
#     input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#     print(new_matrix(input_matrix))
#     print(new_matrix_V2(input_matrix))

# def new_matrix(list):
#     container = []
#     for i in range(len(list)):
#         temp = []
#         for item in list:
#             temp.append(item[i])
#         container.append(temp)
#     return container

# def new_matrix_V2(list):
#     return [[item[i] for item in list] for i in range(len(list[0]))]

# main()
# ==================================================================================
# def main():
#     people_data = [
#         {'name': 'Alice', 'age': 25, 'salary': 55000},
#         {'name': 'Bob', 'age': 13, 'salary': 72000},
#         {'name': 'Charlie', 'age': 30, 'salary': 48000},
#     ]

#     average, oldest, filtered = get_results(people_data)
#     print(f"Average Salary: {average:.2f}")
#     print(f"Oldest person is {oldest['name']} his age is {oldest['age']}")

#     for index, item in enumerate(filtered):
#         print(f"{index+1} - name: {item['name']}; age: {item['age']}")

# def get_results(data):
#     try:
#         salaris = [i["salary"] for i in data]
#         average_salary = sum(salaris) / len(salaris)
#         oldest_age = max(data, key = lambda x : x["age"])
#         filtered_persons = [person for person in data if person['age']>=18]
#     except ValueError:
#         return "Something went wrong"
#     else:
#         return average_salary, oldest_age, filtered_persons

# main()
