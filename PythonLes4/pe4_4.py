def new_password(oldpassword, newpassword):
    ''''Checkt of het nieuwe wachtwoord aan de eisen voldoet: 1. Mag niet hetzelfde zijn als het oude wachtwoord, 2. Moet langer zijn dan 4 tekens, 3. Moet minstens 1 cijfer bevatten.'''
    if oldpassword != newpassword and len(newpassword) > 4 and any(char.isdigit() for char in newpassword):
        print('True!')

    else:
        print('False!')

new_password('JavaIsNietLeuk!', 'PythonIsWelLeuk!1')
