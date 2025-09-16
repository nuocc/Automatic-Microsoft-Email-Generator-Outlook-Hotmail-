#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安全的本地測試账号生成器（全亂碼账号與密码）
由 https://github.com/nuocc 制作
微软邮箱注册链接 https://outlook.live.com/
"""

import random
import string
import time

class TestAccountGenerator:
    def generate_username(self, length=12):
        # 亂碼账号，包含大小寫英文字母與數字
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def generate_password(self, length=17):
        # 密码包含大小寫英文字母與數字
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
            print(f"生成账号 {i+1}/{count}: {account['email']}  密码: {account['password']}")
            time.sleep(random.uniform(0.1,0.3))

        # 輸出 TXT
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f"\n# --- 生成於 {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            for account in accounts:
                f.write(f"{account['email']}:{account['password']}\n")
        print(f"\n已生成 {count} 個账号並保存到 {output_file}")

        return accounts

def main():
    # 啟動時顯示標題
    print("安全的本地測試账号生成器（全亂碼账号與密码）")
    print("由 https://github.com/nuocc 制作")
    print("微软邮箱注册链接 https://outlook.live.com/")
    generator = TestAccountGenerator()
    while True:
        print("\n=== 安全的本地測試账号生成器（全亂碼账号） ===")
        try:
            count = int(input("要生成的账号數量 (1-50, 默认5): ") or 5)
            count = max(1, min(count, 50))
            username_length = int(input("账号長度 (5-12, 默认12): ") or 12)
            username_length = max(5, min(username_length, 12))
            password_length = int(input("密码長度 (7-17, 默认17): ") or 17)
            password_length = max(7, min(password_length, 17))
            email_type = input("账号類型 (outlook/hotmail/both, 默认both): ").lower() or 'both'
            output_file = input("輸出檔案名 (默认 accounts.txt): ") or 'accounts.txt'

            generator.bulk_generate_accounts(
                count=count,
                username_length=username_length,
                password_length=password_length,
                email_type=email_type,
                output_file=output_file
            )
        except ValueError:
            print("錯誤: 请输入有效数字")
            continue
        except KeyboardInterrupt:
            print("\n操作已取消")
            break
        except Exception as e:
            print(f"发生错误: {str(e)}")
            continue

        again = input("\n是否要重新生成账号？(y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n程序异常: {str(e)}")
    finally:
        print("\n由 https://github.com/nuocc 制作")
        try:
            import msvcrt
            print("\n程序結束，請按任意鍵退出...")
            msvcrt.getch()
        except ImportError:
            input("\n程序結束，請按下 Enter 鍵退出...")
