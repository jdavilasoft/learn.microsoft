def generate_report(tanque_principal, tanque_externo, tanque_hidrogeno):
    output = f"""Fuel Report:
    Tanque principal: {tanque_principal}
    Tanque externo: {tanque_externo}
    Tanque Hidrógeno: {tanque_hidrogeno}
    """
    print(output)

generate_report(80, 70, 75)