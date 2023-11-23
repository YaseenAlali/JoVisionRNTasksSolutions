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
    
    return (start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)).isoformat()

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
    'Eleanor', 'Felix', 'Giselle', 'Harrison', 'Isabella', 'Jason', 'Kylie', 'Leonard', 'Megan', 'Nathan',
    'Oscar', 'Penelope', 'Quincy', 'Rebecca', 'Sebastian', 'Tiffany', 'Ulysses', 'Victoria', 'Winston', 'Xena',
    'Yusuf', 'Zoe', 'Abigail', 'Bradley', 'Christina', 'Derek', 'Elaine', 'Frederick', 'Gabriella', 'Howard',
    'Isabel', 'Jeremy', 'Kathryn', 'Lawrence', 'Madeline', 'Nicholas', 'Oliver', 'Patricia', 'Quentin', 'Rosalind',
    'Sylvia', 'Theodore', 'Uma', 'Victor', 'Winifred', 'Xander', 'Yolanda', 'Zeke', 'Ariana', 'Blake',
    'Camilla', 'Drake', 'Esther', 'Finn', 'Gloria', 'Hugo', 'Iris', 'Jesse', 'Kendra', 'Lyle',
    'Monica', 'Nigel', 'Opal', 'Pierce', 'Queenie', 'Rufus', 'Serena', 'Tristan', 'Una', 'Vance',
    'Wilma', 'Xerxes', 'Yvette', 'Zane', 'Astrid', 'Brock', 'Carmen', 'Dexter', 'Esme', 'Flynn'
]

    random_last_names = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Hall', 'Adams', 'Clark', 'Lewis',
    'Walker', 'King', 'Baker', 'Garcia', 'Martinez', 'Lee', 'Rodriguez', 'Martinez', 'Davis', 'Taylor',
    'Wang', 'Li', 'Zhang', 'Chen', 'Liu', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou',
    'Perez', 'Thompson', 'Patel', 'Sanchez', 'Murphy', 'Cook', 'Rogers', 'Bailey', 'Rivera', 'Cooper',
    'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson',
    'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman',
    'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons',
    'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes', 'Myers', 'Ford',
    'Hamilton', 'Graham', 'Sullivan', 'Wallace', 'Woods', 'Cole', 'West', 'Jordan', 'Owens', 'Reynolds',
    'Fisher', 'Ellis', 'Harrison', 'Gibson', 'McDonald', 'Cruz', 'Marshall', 'Ortiz', 'Gomez', 'Murray'
]


    num_entries = 250

    create_csv_file(file_path, random_first_names, random_last_names, num_entries)

    print(f"{num_entries} entries have been created in {file_path}.")