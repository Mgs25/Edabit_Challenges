def banner():
   print(50*'*')
def ETA(speed,size):
   banner()   
   speed,size = float(speed),float(size)
   #Calculations------------
   raw = (size/(speed*8))
   secs = raw*60
   mins = round(secs//60)
   hours = round(mins//60)
   secs = secs - (mins*60)
   mins = mins - (hours*60)
   #------------------------
   return ' ETA -> {} HOURS: {} MINUTES: {} SECONDS (Approx)'.format(hours,mins,round(secs))

print(ETA(input("Internet Speed(Mbps): "),input("File Size(MB): ")))
banner()