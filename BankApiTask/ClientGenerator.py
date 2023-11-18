import csv
import uuid
import random
from datetime import datetime, timedelta

def generate_guid():
    return str(uuid.uuid4())

def generate_salary():
    return round(random.uniform(300, 2000), 2)

def generate_balance():
    return round(random.uniform(100, 5000), 2)

def generate_creation_date():
    today = datetime.now()
    start_date = today - timedelta(days=365 * 10)
    random_days = random.randint(0, (today - start_date).days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    
    return (start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)).strftime('%Y-%m-%d %H:%M:%S')

def create_csv_file(file_path, first_names, last_names, num_entries):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name', 'Salary', 'Balance', 'RegistrationDate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        random.shuffle(first_names)
        random.shuffle(last_names)

        for i in range(num_entries):
            first_name = first_names[i % len(first_names)]
            last_name = last_names[i % len(last_names)]
            full_name = f"{first_name} {last_name}"
            guid = generate_guid()
            salary = generate_salary()
            balance = generate_balance()
            creation_date = generate_creation_date()

            writer.writerow({'ID': guid, 'Name': full_name, 'Salary': salary, 'Balance': balance, 'RegistrationDate': creation_date})

if __name__ == "__main__":
    file_path = 'clients.csv'
    random_first_names = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
        'Kate', 'Liam', 'Mia', 'Noah', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tyler',
        'Ursula', 'Vincent', 'Wendy', 'Xavier', 'Yvonne', 'Zachary', 'Amelia', 'Benjamin', 'Catherine', 'Daniel',
        'Eleanor', 'Felix', 'Giselle', 'Harrison', 'Isabella', 'Jason', 'Kylie', 'Leonard', 'Megan', 'Nathan'
    ]

    random_last_names = [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
        'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Hall', 'Adams', 'Clark', 'Lewis',
        'Walker', 'King', 'Baker', 'Garcia', 'Martinez', 'Lee', 'Rodriguez', 'Martinez', 'Davis', 'Taylor',
        'Wang', 'Li', 'Zhang', 'Chen', 'Liu', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou'
    ]
    num_entries = 250

    create_csv_file(file_path, random_first_names, random_last_names, num_entries)

    print(f"{num_entries} entries have been created in {file_path}.")
