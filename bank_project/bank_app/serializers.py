from rest_framework import serializers

class BankSerializers(serializers.Serializer):
    person_age = serializers.IntegerField()
    person_gender = serializers.CharField(max_length=32)
    person_education = serializers.CharField(max_length=32)
    person_income = serializers.IntegerField()
    person_emp_exp = serializers.IntegerField()
    person_home_ownership = serializers.CharField(max_length=32)
    loan_amnt = serializers.IntegerField()
    loan_intent = serializers.CharField(max_length=32)
    loan_int_rate = serializers.FloatField()
    loan_percent_income = serializers.FloatField()
    cb_person_cred_hist_length = serializers.IntegerField()
    credit_score = serializers.IntegerField()
    previous_loan_defaults_on_file = serializers.CharField(max_length=32)
