def check_pwd(password):
  if len(password) < 8:
    return False
  if len(password) > 20:
    return False
  if password[0].islower() == False:
    return False
  return True
