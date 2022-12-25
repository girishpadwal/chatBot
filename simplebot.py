import random

hellow=['hi','hello','hello there','is anyone there']
howareyou=['how are you','whatsup','how are you doing']
bye=['see ya','see you later','bye','good bye','i am leaving','have a good day']
name=['whats your name','whats is your name','do you have any name','what should i call you']
inq=['i want to take admition','which courses available','what do you reccommend']
hours=['when are you guys open','what are your hours','hours of operation','time','work time','time period']

while True:
    a=input('user said : ')
    if a.lower() in hellow:
        botans=['hello !','hii','hi there','welcome']
        print('Bot said : '+random.choice(botans)+'\n')
    elif a.lower() in bye:
        botans=['sad to see you go','bye','miss you','bye come again']
        print('Bot said : '+random.choice(botans)+'\n')
    elif a.lower() in howareyou:
        botans=['i am fine','good,what about you','i am good','good']
        print('Bot said : '+random.choice(botans)+'\n')
    elif a.lower() in name:
        botans=['my name is clg bot','clg bot in your service','you can call me clg bot']
        print('Bot said : '+random.choice(botans)+'\n')
    elif a.lower() in inq:
         botans=['scince commerce arts this are the cources']
         print('Bot said : '+random.choice(botans)+'\n')
    elif a.lower() in hours:
        botans=['10am to 5pm','we are open 10 am to 5 pm monday to friday']
        print('Bot said : '+random.choice(botans)+'\n')
    else:
        print('Bot said : sorry what? i cannot get what you said''\n')



