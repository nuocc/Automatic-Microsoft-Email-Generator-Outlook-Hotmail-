#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""安全なローカルテスト用アカウント生成器（ランダムユーザー名とパスワード）
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
    print("安全なローカルテスト用アカウント生成器（ランダムユーザー名とパスワード）")
    print("Author: https://github.com/nuocc")
    print("Microsoft email registration: https://outlook.live.com/")
    generator = TestAccountGenerator()
    while True:
        print("\n=== Secure Local Test Account Generator ===")
        try:
            count = int(input("生成するアカウント数 (1-50, デフォルト5): ") or 5)
            count = max(1, min(count, 50))
            username_length = int(input("ユーザー名の長さ (5-12, デフォルト7): ") or 7)
            username_length = max(5, min(username_length, 12))
            password_length = int(input("パスワードの長さ (7-17, デフォルト10): ") or 10)
            password_length = max(7, min(password_length, 17))

            print("\nメールタイプを選択してください:")
            print("  1. outlook")
            print("  2. hotmail")
            print("  3. both (default)")
            choice = input("数字を入力してください (1/2/3): ").strip() or "3"
            email_type = {'1':'outlook','2':'hotmail','3':'both'}.get(choice, 'both')

            output_file = input("出力ファイル名 (デフォルト accounts.txt): ") or 'accounts.txt'

            generator.bulk_generate_accounts(count, username_length, password_length, email_type, output_file)
        except ValueError:
            print("エラー: 有効な数字を入力してください")
            continue
        except KeyboardInterrupt:
            print("\n操作がキャンセルされました")
            break
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            continue

        again = input("\n再生成しますか？(y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nプログラムエラー: {str(e)}")
    finally:
        print("\nAuthor: https://github.com/nuocc")
        try:
            import msvcrt
            print("\nプログラム終了。任意のキーを押して終了してください...")
            msvcrt.getch()
        except ImportError:
            input("\nProgram finished. Press Enter to exit...")