use miniproject;

-- select t_symptom.name from t_symptom inner join t_disease_symptoms on t_symptom.id=t_disease_symptoms.symptom_id  where t_disease_symptoms.disease_id='fever';

-- select * from t_medicine inner join t_disease_medicines on t_medicine.name=t_disease_medicines.medicine_id  where t_disease_medicines.disease_id='fever';

-- select * from t_store inner join t_medicine_stores on t_store.id=t_medicine_stores.store_id  where t_medicine_stores.medicine_id='';

-- select * from t_store inner join t_medicine_stores on t_store.id=t_medicine_stores.store_id  where t_medicine_stores.medicine_id='Imodium' and t_store.city='Allahabad'

-- insert into t_store(name, email, phone, city, location, pincode) values('Star Medical Store', 'bhatia@123.com', 9734985935, 'Noida', '24x7 r.n. 148, Purani haveli, Noida', 788874);

-- select * from t_store;

-- UPDATE t_store SET LOCATION='24x7 R.N. 148, Nayi Haveli, Noida' where id = 12;

DELETE FROM t_store where id = 12;