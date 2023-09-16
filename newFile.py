
# Adding a function that can be called to handle new Users

def newUsers(userName):
  if(type(userName) == str):
    print("valid userName")
    return userName
  else:
    print("invalid userName")
    print("please provide a string")
    return ""
