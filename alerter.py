alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    if(celcius > 200 ):
        return 'not-ok'
    # stub always succeeds and returns 200
    return 'ok'

def farenheit_to_celcius(faren):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def alert_in_celcius(farenheit):
    celcius = farenheit_to_celcius(farenheit)
    returnCode = network_alert_stub(celcius)
    if returnCode != 'ok':
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5)
alert_in_celcius(303.6)
assert(alert_failure_count == 1)
print('All is well (maybe!)')
