#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Safe local test account generator (random usernames and passwords)
Created by https://github.com/nuocc
Microsoft signup URL https://outlook.live.com/
"""

import random
import string
import time

class TestAccountGenerator:
    def generate_username(self, length=12):
        # Random username, includes upper/lowercase letters and digits
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def generate_password(self, length=17):
        # Random password, includes upper/lowercase letters and digits
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def generate_account(self, username_length=12, password_length=17, email_type='outlook'):
        username = self.generate_username(username_length)
        password = self.generate_password(password_length)
        if email_type.lower() == 'outlook':
            email = f"{username}@outlook.com"
        elif email_type.lower() == 'hotmail':
            email = f"{username}@hotmail.com"
        else:
            email = f"{username}@example.com"
        return {'email': email, 'password': password, 'username': username}

    def bulk_generate_accounts(self, count=10, username_length=12, password_length=17, email_type='both', output_file='accounts.txt'):
        accounts = []
        for i in range(count):
            if email_type == 'both':
                account_type = 'outlook' if random.choice([True, False]) else 'hotmail'
            else:
                account_type = email_type
            account = self.generate_account(username_length, password_length, account_type)
            accounts.append(account)
            print(f"Generated account {i+1}/{count}: {account['email']}  Password: {account['password']}")
            time.sleep(random.uniform(0.1,0.3))

        # Output TXT
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f"\n# --- Generated on {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            for account in accounts:
                f.write(f"{account['email']}:{account['password']}\n")
        print(f"\nGenerated {count} accounts and saved to {output_file}")

        return accounts

def main():
    # Show header
    print("Safe local test account generator (random usernames and passwords)")
    print("Created by https://github.com/nuocc")
    print("Microsoft signup URL https://outlook.live.com/")

    generator = TestAccountGenerator()
    while True:
        print("\n=== Safe Local Test Account Generator (Randomized) ===")
        try:
            count = int(input("Number of accounts to generate (1-50, default 5): ") or 5)
            count = max(1, min(count, 50))

            username_length = int(input("Username length (5-12, default 12): ") or 12)
            username_length = max(5, min(username_length, 12))

            password_length = int(input("Password length (7-17, default 17): ") or 17)
            password_length = max(7, min(password_length, 17))

            email_type = input("Account type (outlook/hotmail/both, default both): ").lower() or 'both'
            output_file = input("Output file name (default accounts.txt): ") or 'accounts.txt'

            generator.bulk_generate_accounts(
                count=count,
                username_length=username_length,
                password_length=password_length,
                email_type=email_type,
                output_file=output_file
            )
        except ValueError:
            print("Error: Please enter a valid number")
            continue
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

        again = input("\nGenerate again? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nProgram error: {str(e)}")
    finally:
        print("\nCreated by https://github.com/nuocc")
        try:
            import msvcrt
            print("\nProgram ended. Press any key to exit...")
            msvcrt.getch()
        except ImportError:
            input("\nProgram ended. Press Enter to exit...")
