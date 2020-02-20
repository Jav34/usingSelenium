def action():
    yes = 'y'
    no = 'n'
    print('For translation, please select "y", if not type "n"')
    select = input("-->")
    import próby
    if select == yes:
        return próby
    elif select == no:
        print("If you change your mind, please let me know")
    else:
        print("I'm afraid I don't understand your wishes")


action()
