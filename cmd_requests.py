import themes

# Dict Characteristics
response = 'RESPONSE'
action = 'action'

# Requests
help = 'HELP'
error = 'ERROR'
theme = 'THEME'
quit_request = 'QUIT'
reboot = 'REBOOT'
code = 'CODE'


# CODES
# 0 - TEXT RESPONSE TO USER, NO FURTHER ACTION REQUIRED
# 1 - THEME CHANGE
# 2 - QUIT
# 3 - REBOOT

cmd_inputs = {
    help: {
        response: 'OPTIONS: THEME',
        action: 0
    },

    error: {
        response: 'COMMAND INVALID.',
        action: 0
    },

    theme: {
        response: ', '.join(themes.theme_names),
        action: 0
    },

    # TESTING DELETE LATER
    quit_request: {
        response: '',
        action: 2
    },

    reboot: {
        response: '',
        action: 3
    },

    code: {
        response: '',
        action: 4
    }
}

for theme_style in themes.theme_names:
    temp_input = {
        response: 'THEME CHANGED TO ' + theme_style,
        action: 1
    }
    cmd_inputs[theme_style] = temp_input