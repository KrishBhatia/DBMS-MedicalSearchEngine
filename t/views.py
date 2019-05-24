from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Disease, Medicine, Store, Symptom
from .form import DiseaseForm


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def index(request):
    c = connection.cursor()
    try:
        c.execute('SELECT * FROM t_store')
        q = dictfetchall(c)
    finally:
        c.close()
    for i in q:
        print(i['id'])
    return render(request, "t/index.html", {'title': 'Medical Search Engine', 'query': q})


# def home(request):
#     if request.method == "POST":
#         form = DiseaseForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             # disease = get_object_or_404(Disease, pk=name)
#             c = connection.cursor()
#             try:
#                 c.execute('SELECT * FROM t_disease where name=%s', [name])
#                 q = dictfetchall(c)
#             finally:
#                 c.close()
#             return redirect('disease_detail', pk=q[0]['name'])
#     else:
#         form = DiseaseForm()
#     c = connection.cursor()
#     try:
#         c.execute('SELECT * FROM t_disease')
#         q = dictfetchall(c)
#     finally:
#         c.close()
#     return render(request, 't/home.html', {'query': q})


def disease_detail(request, pk):
    c = connection.cursor()
    try:
        c.execute('SELECT * FROM t_disease where name=%s', [pk])
        disease = dictfetchall(c)
        print(disease)
        c.execute(
            'select t_symptom.name from t_symptom inner join t_disease_symptoms on t_symptom.id=t_disease_symptoms.symptom_id  where t_disease_symptoms.disease_id=%s', [pk])
        symptoms = dictfetchall(c)
    finally:
        c.close()
    return render(request, 't/disease_detail.html', {'disease': disease[0], 'symptoms': symptoms, 'pk': pk})


def disease_medicine(request, pk):
    c = connection.cursor()
    try:
        c.execute(
            'select * from t_medicine inner join t_disease_medicines on t_medicine.name=t_disease_medicines.medicine_id  where t_disease_medicines.disease_id=%s', [pk])
        medicines = dictfetchall(c)
    finally:
        c.close()
    return render(request, 't/medicine_detail.html', {'medicines': medicines, 'pk': pk})


def medicine_store(request, pk):
    c = connection.cursor()
    try:
        c.execute(
            'select * from t_store inner join t_medicine_stores on t_store.id=t_medicine_stores.store_id  where t_medicine_stores.medicine_id=%s', [pk])
        stores = dictfetchall(c)
    finally:
        c.close()
    return render(request, 't/store_detail.html', {'stores': stores, 'pk': pk})


def store(request, pk):
    name = request.GET.get('search')

    if name == "" or name == None:
        return render(request, 't/store_detail.html', {'pk': pk})
    else:
        c = connection.cursor()
        try:
            c.execute(
                'select * from t_store inner join t_medicine_stores on t_store.id=t_medicine_stores.store_id  where t_medicine_stores.medicine_id=%s and t_store.city=%s', ([pk], [name]))
            stores = dictfetchall(c)
            if len(stores) == 0:
                messages = {
                    "message": 'Medicine Does Not Available On Any Store In This City.'}
            else:
                messages = {}
        finally:
            c.close()
        return render(request, 't/store_detail.html', {'stores': stores, 'messages': messages})


def search(request):
    c = connection.cursor()
    try:
        c.execute('SELECT * FROM t_disease')
        q = dictfetchall(c)
        c.execute('SELECT * FROM t_medicine')
        q1 = dictfetchall(c)
        c.execute('SELECT * FROM t_symptom')
        q2 = dictfetchall(c)
    finally:
        c.close()

    name = request.GET.get('search')
    medicine = request.GET.get('medicine')

    if name != None:
        c = connection.cursor()
        try:
            c.execute('SELECT name FROM t_disease')
            e = dictfetchall(c)
            d = []
            for i in e:
                d.append(i['name'])

            if name not in d:
                messages = {
                    "message": ' Disease does not exists in database.'}
                return render(request, 't/w3.html', {'diseases': q, 'medicines': q1, 'symptoms': q2, 'messages': messages})

            else:
                c.execute('SELECT * FROM t_disease where name=%s', [name])
                disease = dictfetchall(c)
                c.execute(
                    'select t_symptom.name from t_symptom inner join t_disease_symptoms on t_symptom.id=t_disease_symptoms.symptom_id  where t_disease_symptoms.disease_id=%s', [name])
                symptoms = dictfetchall(c)

        finally:
            c.close()

        return render(request, 't/disease_detail.html', {'disease': disease[0], 'symptoms': symptoms, 'pk': name})

    elif medicine != None:
        c = connection.cursor()
        try:
            c.execute('SELECT name FROM t_medicine')
            e = dictfetchall(c)
            d = []
            for i in e:
                print(i)
                d.append(i['name'])

            if medicine not in d:
                messages = {
                    "message": ' Medicine does not exists in database.'}
                return render(request, 't/w3.html', {'diseases': q, 'medicines': q1, 'symptoms': q2, 'messages': messages})

            else:
                c.execute('SELECT * FROM t_medicine where name=%s', [medicine])
                medicines = dictfetchall(c)

        finally:
            c.close()

        return render(request, 't/medicine_detail.html', {'medicines': medicines, 'pk': medicine})

    else:
        return render(request, 't/w3.html', {'diseases': q, 'medicines': q1, 'symptoms': q2})
