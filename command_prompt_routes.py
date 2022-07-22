def command_prompt(user_input):
    input = user_input.upper()
    response = [input]
    maximum_request = 50

    # restrict request length
    while len(input) > maximum_request:
        input = input[:-1]
    if input == 'HELP':
        help = 'THERE IS NO HELP HERE. ONLY SUFFERING'
        response.append(help)
        return response
    elif input == '' or input == ' ':
        return response
    else:
        error = '\'' + input + '\'' + ' IS NOT A COMMAND'
        response.append(error)
        return response