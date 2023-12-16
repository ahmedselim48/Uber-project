from django.shortcuts import render
from joblib import load


model = load('./saveModels/xgb_model.joblib')
# Create your views here.
def predictor(request) :
    if request.method == 'POST':
        passenger_count = float(request.POST.get('passenger_count'))
        hour = float(request.POST.get('hour'))
        month =float(request.POST.get('month'))
        Weekday =float(request.POST.get('Weekday'))
        year = float(request.POST.get('year'))
        distance =float(request.POST.get('distance'))
        
        # Prepare input for prediction
        input_data = [passenger_count, hour , month ,Weekday ,year ,distance]  # Add other features

        # Make predictions using your ML model
        predicted_fare = model.predict([input_data])

        return render(request, 'index.html', {'result': predicted_fare})
    else:
        return render(request, 'index.html')
#return render(request ,'index.html')

#def formInfo(request):

    
'''
    passenger_count = float(request.POST.get('passenger_count'))
    hour = float(request.POST.get('hour'))
    month =float(request.POST.get('month'))
    Weekday =float(request.POST.get('Weekday'))
    year = float(request.POST.get('year'))
    distance =float(request.POST.get('distance'))
        
        # Prepare input for prediction
    input_data = [passenger_count, hour , month ,Weekday ,year ,distance]  # Add other features

    predicted_fare = model.predict(input_data)

    return render(request,'result.html' ,{'result' : predicted_fare})


    
    def prediction_view(request):
    if request.method == 'POST':
        passenger_count = float(request.POST.get('passenger_count'))
        hour = float(request.POST.get('hour'))
        month =float(request.POST.get('month'))
        Weekday =float(request.POST.get('Weekday'))
        year = float(request.POST.get('year'))
        distance =float(request.POST.get('distance'))
        
        # Prepare input for prediction
        input_data = [passenger_count, hour , month ,Weekday ,year ,distance]  # Add other features

        # Make predictions using your ML model
        predicted_fare = predict_fare_amount(input_data)  # Replace with your ML function

        return render(request, 'result.html', {'predicted_fare': predicted_fare})
    else:
        return render(request, 'index.html')
    '''