# we use raise to check for conditions that we expect to happen during normal code execution
# assert to verfiy situations that arent expected but that might cause code to misbehave.



def validate_users(username, minlen):
    assert type(username)==str, "username must be a string"
    if minlen<1:
        raise ValueError ("minlen must be atleast 1")
    if len(username)<minlen:
        return False
    if not username.isalnum(): # verify if there are any non alphanumeric characters
        return False
    return True

#print(validate_users(33, 2))
#print(validate_users([], 2))
#print(validate_users(["test"], 2))
#print(validate_users("rinson", 2))
#print(validate_users("", 2))
#print(validate_users("", -2))