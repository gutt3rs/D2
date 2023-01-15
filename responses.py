import os
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '/hello':
        return 'Shut up!'

    if p_message == '/status':
        hostname = "23.209.84.49"
        response = os.system('ping' + " " + hostname)
        if response == 0:
            return 'Servers are up!'
        else:
            return 'Servers are Under Maintenance!'

    if p_message == '?help':
        return 'The help you need cannot be provided here.'
