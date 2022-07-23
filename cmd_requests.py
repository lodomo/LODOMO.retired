import themes

# Dict Characteristics
response = 'RESPONSE'
code = 'CODE'

# Requests
help = 'HELP'
error = 'ERROR'
theme = 'THEME'

# CODES
    # 0 - TEXT RESPONSE TO USER, NO FURTHER ACTION REQUIRED
    # 1 - THEME CHANGE

cmd_inputs = {
    help: {
        response: 'OPTIONS: THEME',
        code: 0
    },

    error: {
        response: 'COMMAND INVALID.',
        code: 0
    },

    theme: {
        response: 'TODAY\'S FLAVORS ARE: ' + ', '.join(themes.theme_names),
        code: 0
    },
}

for theme_style in themes.theme_names:
    temp_input = {
        response: 'THEME CHANGED TO ' + theme_style,
        code: 1
    }
    cmd_inputs[theme_style] = temp_input