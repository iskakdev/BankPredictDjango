from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import BankSerializers
import joblib
import os
from django.conf import settings

scaler_path = os.path.join(settings.BASE_DIR, 'scaler_bank.pkl')
model_path = os.path.join(settings.BASE_DIR, 'log_model_bank.pkl')

scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

person_gender = ['male']
person_education = ['Bachelor', 'Doctorate', 'High School', 'Master']
person_home_ownership = ['OTHER', 'OWN', 'RENT']
loan_intent = ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE']
previous_loan_defaults_on_file = ['Yes']

class BankPredict(views.APIView):
    def post(self, request):
        serializer = BankSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_gender = data.get('person_gender')
            gender1or_0 = [1 if new_gender == i else 0 for i in person_gender]

            new_education = data.get('person_education')
            education1or_0 = [1 if new_education == i else 0 for i in person_education]

            new_ownership = data.get('person_home_ownership')
            ownership1or_0 = [1 if new_ownership == i else 0 for i in person_home_ownership]

            new_intent = data.get('loan_intent')
            intent1or_0 = [1 if new_intent == i else 0 for i in loan_intent]

            new_defaults = data.get('previous_loan_defaults_on_file')
            defaults1or_0 = [1 if new_defaults == i else 0 for i in previous_loan_defaults_on_file]

            features = ([data['person_age'], data['person_income'], data['person_emp_exp'],
                        data['loan_amnt'], data['loan_int_rate'], data['loan_percent_income'],
                        data['cb_person_cred_hist_length'], data['credit_score']] + gender1or_0
                        + education1or_0 + ownership1or_0 + intent1or_0 + defaults1or_0)
            scaled_data = scaler.transform([features])
            proba = model.predict_proba(scaled_data)[0]
            probability = float(proba[1])
            if probability > 0.5:
                bank_label = 'Yes'
            else:
                bank_label = 'No'
            return Response({'Approved': bank_label , 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
