# Ludi Project
This project is a simple web application that summarizes information related to Ludi. The data is sourced from the `users.json` and `simulations.json` files. The web application has two views:
1. **Users Per Company**: This view displays the number of users per company.
2. **Daily User Growth**: This view displays the daily user growth of Ludi.

## Run Locally
To run this project locally, follow these steps:
1. Clone the repository.
```bash
git clone https://github.com/Abdusshh/LudiSoftwareEngineerInternCase
```
2. Install the required dependencies: 
```bash
cd ludi_project
pip install -r requirements.txt
```
3. Migrate the database:
```bash
python manage.py migrate
ptyhon manage.py load_data
```
4. To start the web application, run the following command:
```bash
python manage.py runserver
```
Then, open your browser and navigate to `http://localhost:8000/ludi_app/users_per_company/` or `http://localhost:8000/ludi_app/daily_user_growth/` to view the data.

## Minor Modifications
I deleted two users in the `users.json` file to avoid conflicts of having the same `user_id`.