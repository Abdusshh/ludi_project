import json
from django.core.management.base import BaseCommand
from ludi_app.models import User, Simulation
import datetime
import xlrd

class Command(BaseCommand):
    help = 'Load data from JSON files'

    def handle(self, *args, **kwargs):

        #  clear existing data
        Simulation.objects.all().delete()
        User.objects.all().delete()

        with open('simulations.json', encoding='utf-8') as f:
            simulations_data = json.load(f)
            for sim in simulations_data['simulations']:
                Simulation.objects.create(
                    simulation_id=sim['simulation_id'],
                    simulation_name=sim['simulation_name'],
                    company_id=sim['company_id'],
                    company_name=sim['company_name']
                )
        
        with open('users.json', encoding='utf-8') as f:
            users_data = json.load(f)
            for user in users_data['users']:
                simulation = Simulation.objects.get(simulation_id=user['simulation_id'])
                signup_date = xlrd.xldate.xldate_as_datetime(user['signup_datetime'], 0)
                User.objects.create(
                    user_id=user['user_id'],
                    user_name=user['user_name'],
                    user_surname=user['user_surname'],
                    simulation=simulation,
                    signup_datetime=signup_date,
                    progress_percent=user['progress_percent']
                )
