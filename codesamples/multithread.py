import threading
import time
import random
class Account:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print("Depositing {}...".format(amount))
            current_balance = self.balance
            random.seed(time.time())
            sleep_time = random.uniform(0.5, 2.5)  
            time.sleep(sleep_time)
            self.balance = current_balance + amount
            print("Deposit complete. New balance: {}".format(self.balance))

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print("Withdrawing {}...".format(amount))
                current_balance = self.balance
                random.seed(time.time())
                sleep_time = random.uniform(0.5, 2.5)  
                time.sleep(sleep_time)
                self.balance = current_balance - amount
                print("Withdrawal complete. New balance: {}".format(self.balance))
            else:
                print("Insufficient funds for withdrawal.")

def deposit_worker(account, amount):
    account.deposit(amount)

def withdraw_worker(account, amount):
    account.withdraw(amount)

def main():
    account = Account()
    threads = []

    # Create deposit and withdrawal threads
    for _ in range(5):
        deposit_thread = threading.Thread(target=deposit_worker, args=(account, 100))
        withdraw_thread = threading.Thread(target=withdraw_worker, args=(account, 50))
        threads.append(deposit_thread)
        threads.append(withdraw_thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Final balance:", account.balance)

if __name__ == "__main__":
    random.seed(time.time()) 
    main()
