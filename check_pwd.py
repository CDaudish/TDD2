def check_pwd(password):
  if len(password) < 8:
    return False
  if len(password) > 20:
    return False
  if password[0].islower() == False or password[1].islower() == False or password[8].islower() == False:
    return False
  return True
