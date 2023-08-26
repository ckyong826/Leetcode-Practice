def add_time(start, duration,d=None):
  
  #declare variable
  p=["AM","PM"]
  day={0:"Sunday", 1:"Monday", 2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
  count=0
  dCount=0

  #find day
  if d!=None:
    d=d.lower()
    d=d.capitalize()
    #find day
    for it in range(7):
      if d==day[it]:
        dCount=it
  
  #find hour and minute
  S=start.find(':')
  D=duration.find(':')
  sHour=int(start[:S])
  sMin=int(start[S+1:S+3])
  dHour=int(duration[:D])
  dMin=int(duration[D+1:D+3])

  #Add time and initialize period
  sHour+=dHour
  sMin+=dMin
  if p[0] in start:
    i=0
  else:
    i=1

  #Calculate the time
  while sMin>60:
    sMin-=60
    sHour+=1
  while sHour>=12:
    if i%2==0:  
      if (sHour/12)==1:
        i+=1
        break
      else:
        sHour-=12
        i+=1
    else:
      if (sHour/12)==1:
        i+=1
        count+=1
        break
      else:
        sHour-=12
        i+=1
        count+=1  
  period=p[i%2]
  dCount+=count

  #int to string
  sHour=str(sHour)
  if sMin<10:
    sMin=str(sMin)
    sMin="0"+ sMin
  else:
    sMin=str(sMin)
  
  #print time
  new_time=sHour+":"+sMin+" "+period
  if d!=None:
    new_time+=", "+day[dCount%7]
  if count==1:
    new_time+=" (next day)"
  elif count>1:
    new_time+=" (" + str(count) +" days later)"
    
  return new_time