#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):

  calculo_min = math.floor(secs / 60) 
  calculo_horas = math.floor(calculo_min / 60)

  return (calculo_horas, calculo_min)

  

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))


#  1h = 60 min = 3600 sg
#  1m = 60sg
