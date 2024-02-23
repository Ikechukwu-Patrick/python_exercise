def decorate(fn):
    print('***********')
    print(fn())
    print('***********')


@decorate
def show_name():
    return "Omi Ewa"






#show_name("miriam")
