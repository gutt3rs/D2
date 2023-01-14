def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '/hello':
        return 'Shut up!'

    if p_message == '/status':
        return 'You have not connected the API yet.'

    if p_message == 'help':
        return 'The help you need cannot be provided here.'
