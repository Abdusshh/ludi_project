from django.db import models

class Simulation(models.Model):
    simulation_id = models.IntegerField(primary_key=True)
    simulation_name = models.CharField(max_length=255)
    company_id = models.IntegerField()
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.simulation_name

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, default=None)
    signup_datetime = models.DateTimeField()
    progress_percent = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} {self.user_surname}"
