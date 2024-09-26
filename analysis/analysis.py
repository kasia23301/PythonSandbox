import csv
import matplotlib.pylab as plt


def load_patients():
    with open('../heart-disease-uci/heart.csv', mode='r') as File:
        csv_data = csv.reader(File)
        patients = []
        for row in csv_data:
            patients.append(
                Patient(age=row[0], sex=row[1], cp=row[2], trestbps=row[3], chol=row[4], fbs=row[5], restecg=row[6],
                        thalach=row[7],
                        exang=row[8], oldpeak=row[9], slope=row[10], ca=row[11], thal=row[12], target=row[13]))
        patients.pop(0)
        return patients


def number_of_women_and_men(patients):
    male = 0
    female = 0
    for patient in patients:
        if patient.sex == "1":
            male += 1
        else:
            female += 1
    return male, female


def average_cholesterol(patients):
    chol_men = []
    chol_women = []
    for patient in patients:
        if patient.sex == "1":
            chol_men.append(patient.chol)
        if patient.sex == "0":
            chol_women.append(patient.chol)
    average_chol_men = sum([int(c) for c in chol_men]) / len(chol_men)
    average_chol_women = sum([int(i) for i in chol_women]) / len(chol_women)
    return average_chol_men, average_chol_women


def average_cholesterol_by_age(patients):
    chol_below_50 = []
    chol_over_50 = []
    for patient in patients:
        if patient.age <= "50":
            chol_below_50.append(patient.chol)
        if patient.age > "50":
            chol_over_50.append(patient.chol)
    average_chol_below_50 = sum([int(c) for c in chol_below_50]) / len(chol_below_50)
    average_chol_over_50 = sum([int(c) for c in chol_over_50]) / len(chol_over_50)
    return average_chol_below_50, average_chol_over_50


def average_age_of_the_examined_persons(patients):
    age = []
    for patient in patients:
        age.append(patient.age)
    average_of_age = sum([int(c) for c in age]) / len(age)
    return average_of_age


def group_by_age(patients):
    dict = {}
    for patient in patients:
        if patient.age in dict:
            dict[patient.age].append(patient.chol)
        else:
            dict[patient.age] = [patient.chol]

    avg_chol_dict = {}
    for age, chols in dict.items():
        new_val = sum([int(c) for c in chols]) / len(chols)
        avg_chol_dict[age] = new_val

    print(avg_chol_dict)
    ages = sorted(avg_chol_dict.keys())

    plt.bar(range(len(avg_chol_dict)), [avg_chol_dict[age] for age in ages], align='center')
    plt.xticks(range(len(avg_chol_dict)), ages)
    plt.show()



class Patient:
    def __init__(self, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.target = target


if __name__ == "__main__":
    patients = load_patients()
    number_of_women_and_men(patients)
    result = average_cholesterol(patients)
    for i in result:
        print("{:10.2f}".format(i))
    result2 = average_cholesterol_by_age(patients)
    for i in result2:
        print("{:10.2f}".format(i))
    result3 = average_age_of_the_examined_persons(patients)
    print(result3)
    group_by_age(patients)
