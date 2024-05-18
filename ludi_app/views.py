from django.shortcuts import render
from django.db.models import Count
from .models import User, Simulation
import json

def users_per_company(request):
    companies = Simulation.objects.values('company_name').annotate(total_users=Count('user'))
    context = {'companies': companies}
    return render(request, './ludi_app/users_per_company.html', context)

def daily_user_growth(request):
    users = User.objects.all()
    user_growth = {}
    total_daily_user_growth = {}
    total_users = 0
    
    for user in users:
        date = user.signup_datetime.date()
        if date not in user_growth:
            user_growth[date] = 0
        user_growth[date] += 1
    # print(user_growth)
    
    sorted_growth = dict(sorted(user_growth.items()))
    # print(sorted_growth)

    for date, growth in sorted_growth.items():
        total_users += growth
        total_daily_user_growth[date] = total_users

    labels = [str(date) for date in total_daily_user_growth.keys()]
    data = list(total_daily_user_growth.values())

    # print(labels)
    # print(data)

    context = {
        # Convert to JSON string
        'context_labels': json.dumps(labels),  
        'context_data': json.dumps(data)  
    }
    return render(request, 'ludi_app/daily_user_growth.html', context)