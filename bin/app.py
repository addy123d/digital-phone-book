from database import Database
from credentials import Credentials
import user, click, os
import psycopg2
from colorama import Fore, Style

import sys
import time

# from LOGO import x, github
BOLD = '\033[1m'
DEBUG = True



os.system('cls' if os.name == 'nt' else 'clear')
@click.command()
@click.option('--signup', is_flag=True, help='to sign up as a user ')
@click.option('--login', is_flag=True, help='to login the account')

def cli(login, signup):
    Database.initialise(database="",
                        user="",
                        password="",
                        host="localhost",
                        port="5432"
                        ) #create a database connection

    message = f"{BOLD}{Fore.BLACK}You should Login to add/view contacts...{Style.RESET_ALL}\n" \
              f"{BOLD}{'--login':10}{Style.RESET_ALL} To Login as existing user\n" \
              f"{BOLD}{'--signup':10}{Style.RESET_ALL} To Signup as a new user\n"
    if login:

        print("Login Block") if DEBUG else None

        data = user.UserLogin.login_information()
        user.UserLogin.check_login(data)

    if signup:

        print("Registration Block") if DEBUG else None

        data = user.UserSignUp.signup_information()
        user.UserSignUp.save_to_db(data)

   


    else:
        print(message)
    
    

def db_connect():
    
    #Check whether database is created or not.
    connection = psycopg2.connect(host=Credentials.HOST, database=Credentials.DATABASE, user=Credentials.USER, password=Credentials.PASSWORD)

    #Create Database
    connection.autocommit = True
    cursor = connection.cursor()
    
    return cursor


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
            
if __name__ == '__main__':
    cli()
