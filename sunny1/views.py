from django.shortcuts import render
import datetime
def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg='hello guest!!!Good morning!!!'
    elif h<16:
        msg='hello guest!!Good evening'
    else:
        msg='Hello Guest!!!Good Night!!!'
    my_dict={'date':date,'msg':msg}
    return render(request,'results.html',my_dict)
