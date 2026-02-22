from django.db import models

class Bank(models.Model):
    person_age = models.IntegerField()
    person_gender = models.CharField(max_length=32)
    person_education = models.CharField(max_length=32)
    person_income = models.IntegerField()
    person_emp_exp = models.IntegerField()
    person_home_ownership = models.CharField(max_length=32)
    loan_amnt = models.IntegerField()
    loan_intent = models.CharField(max_length=32)
    loan_int_rate = models.FloatField()
    loan_percent_income = models.FloatField()
    cb_person_cred_hist_length = models.IntegerField()
    credit_score = models.IntegerField()
    previous_loan_defaults_on_file = models.CharField(max_length=32)
