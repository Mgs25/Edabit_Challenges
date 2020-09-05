import re
def CodelandUsernameValidation(strParam):
  pattern = '[^(\w)]'
  return bool(re.match(pattern,strParam))

print(CodelandUsernameValidation('This is fine'))