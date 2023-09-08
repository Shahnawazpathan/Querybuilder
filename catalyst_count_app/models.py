from django.db import models

class csv_data(models.Model):
    company_data = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=255, null=True)
    domain = models.CharField(max_length=255, null=True)
    year_founded = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    size_range = models.CharField(max_length=255, null=True)
    locality = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    linkedin_url = models.URLField(max_length=200)
    current_employee_estimate = models.CharField(max_length=255, null=True)
    total_employee_estimate = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=25, default=None, null=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name







