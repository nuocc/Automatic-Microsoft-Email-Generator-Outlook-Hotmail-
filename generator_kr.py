#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""안전한 로컬 테스트 계정 생성기 (무작위 사용자 이름 및 비밀번호)
Author: https://github.com/nuocc
Microsoft email registration: https://outlook.live.com/
"""

import random
import string
import time

class TestAccountGenerator:
    def generate_username(self, length=7):
        first_char = random.choice(string.ascii_letters)
        if length > 1:
            chars = string.ascii_letters + string.digits
            rest = ''.join(random.choices(chars, k=length - 1))
            return first_char + rest
        else:
            return first_char

    def generate_password(self, length=10):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def generate_account(self, username_length=7, password_length=10, email_type='outlook'):
        username = self.generate_username(username_length)
        password = self.generate_password(password_length)
        if email_type.lower() == 'outlook':
            email = f"{username}@outlook.com"
        elif email_type.lower() == 'hotmail':
            email = f"{username}@hotmail.com"
        else:
            email = f"{username}@example.com"
        return {'email': email, 'password': password, 'username': username}

    def bulk_generate_accounts(self, count=10, username_length=7, password_length=10, email_type='both', output_file='accounts.txt'):
        accounts = []
        for i in range(count):
            if email_type == 'both':
                account_type = 'outlook' if random.choice([True, False]) else 'hotmail'
            else:
                account_type = email_type
            account = self.generate_account(username_length, password_length, account_type)
            accounts.append(account)
            print(f"Account {i+1}/{count}: {account['email']}  Password: {account['password']}")
            time.sleep(random.uniform(0.1,0.3))

        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f"\n# --- Generated at {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            for account in accounts:
                f.write(f"{account['email']}:{account['password']}\n")
        print(f"\n{count} accounts generated and saved to {output_file}")
        return accounts

def main():
    print("안전한 로컬 테스트 계정 생성기 (무작위 사용자 이름 및 비밀번호)")
    print("Author: https://github.com/nuocc")
    print("Microsoft email registration: https://outlook.live.com/")
    generator = TestAccountGenerator()
    while True:
        print("\n=== Secure Local Test Account Generator ===")
        try:
            count = int(input("생성할 계정 수 (1-50, 기본값 5): ") or 5)
            count = max(1, min(count, 50))
            username_length = int(input("사용자 이름 길이 (5-12, 기본값 7): ") or 7)
            username_length = max(5, min(username_length, 12))
            password_length = int(input("비밀번호 길이 (7-17, 기본값 10): ") or 10)
            password_length = max(7, min(password_length, 17))

            print("\n계정 유형을 선택하세요:")
            print("  1. outlook")
            print("  2. hotmail")
            print("  3. both (default)")
            choice = input("번호 입력 (1/2/3): ").strip() or "3"
            email_type = {'1':'outlook','2':'hotmail','3':'both'}.get(choice, 'both')

            output_file = input("출력 파일 이름 (기본값 accounts.txt): ") or 'accounts.txt'

            generator.bulk_generate_accounts(count, username_length, password_length, email_type, output_file)
        except ValueError:
            print("오류: 유효한 숫자를 입력하세요")
            continue
        except KeyboardInterrupt:
            print("\n작업이 취소되었습니다")
            break
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            continue

        again = input("\n다시 생성하시겠습니까? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n프로그램 오류: {str(e)}")
    finally:
        print("\nAuthor: https://github.com/nuocc")
        try:
            import msvcrt
            print("\n프로그램 종료. 아무 키나 눌러 종료하세요...")
            msvcrt.getch()
        except ImportError:
            input("\nProgram finished. Press Enter to exit...")