# Medium Level Problem

def fun(s):
    # return True if s is a valid email, else return False
    
    # First check if there are all 3 parts available for splitting
    at_count = s.count("@")
    dot_count = s.count(".")
    if at_count != 1 or dot_count != 1:
        return False
        
    s = s.replace("@", ".")
    parts = s.split(".")
    
    # Username Check
    username = parts[0]
    
    # Simply remove "-,_" from the username and check for alphanumeric
    username = username.replace("_" ,"a")
    username = username.replace("-", "a")
    if not(username.isalnum()):
        return False
    
    # Website Name Check
    if not(parts[1].isalnum()):
        return False
        
    # Extension Check
    if not(parts[2].isalpha()) or len(parts[2]) > 3:
        return False
    
    # If it passed all checks, then it is a valid email
    return True
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)