def greeting(text):

    # Greeting inputs
    greeting_inputs = ['hi','hey','hola','greetngs','wassup','hello']

    # Greeting responses
    greeting_responses = ['hello','hey there']

    # If the users input is a greeting, then return a randomly choosen greeting response
    for word in text.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)+'.'

    # If no greeting was detected then return an empty string
    return ''
