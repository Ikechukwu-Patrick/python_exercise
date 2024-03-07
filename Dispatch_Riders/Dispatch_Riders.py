def calculate_dispatch_riders_wage(number_of_successful_delivery: int):
    if number_of_successful_delivery < 0:
        raise ValueError("Invalid input")
    elif number_of_successful_delivery < 50:
        return number_of_successful_delivery * 160 + 5000

    elif number_of_successful_delivery == 50 and number_of_successful_delivery < 59:
        return number_of_successful_delivery * 200 + 5000

    elif number_of_successful_delivery == 60 and number_of_successful_delivery < 69:
        return number_of_successful_delivery * 250 + 5000

    elif number_of_successful_delivery >= 70:
        return number_of_successful_delivery * 500 + 5000

    else:
        return number_of_successful_delivery


print(calculate_dispatch_riders_wage(80))
