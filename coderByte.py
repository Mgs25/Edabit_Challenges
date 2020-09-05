def LongestWord(sen):
  sen = sen.split()
  flag = len(sen[0])
  print(flag)
  for i in range(1,len(sen)):
    if len(sen[i]) > flag:
      flag = sen[i]
  return flag
# keep this function call here 
print(LongestWord(input()))