

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
# greatest_number_of_hours = 0
# greatest_name = ""
# for name, hours in work_hours:
#     if hours > greatest_number_of_hours:
#         greatest_number_of_hours = hours
#         greatest_name = name
# print(name, greatest_number_of_hours)


def employee_of_month(work_hours):
    greatest_number_of_hours = 0
    greatest_name = ""
    for name, hours in work_hours:
        if hours > greatest_number_of_hours:
            greatest_number_of_hours = hours
            greatest_name = name
    return greatest_name, greatest_number_of_hours

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
print(employee_of_month(work_hours))