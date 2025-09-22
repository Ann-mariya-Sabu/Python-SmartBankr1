import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
from functools import reduce
from datetime import datetime

# Custom banking module - defined within the same file
class BankingModule:
    @staticmethod
    def create_account(acc_num, name, email, phone, balance, pin):
        """Create a new bank account"""
        return {
            'acc_num': acc_num,
            'name': name,
            'email': email,
            'phone': phone,
            'balance': balance,
            'pin': pin,
            'created_at': datetime.now().strftime('%Y-%m-%d'),
            'account_type': 'Savings',
            'status': 'Active'
        }
    
    @staticmethod
    def validate_transaction(amount, balance, transaction_type='withdrawal'):
        """Validate if a transaction can be processed"""
        if transaction_type.lower() == 'withdrawal':
            return 0 < amount <= balance
        return amount > 0
    
    @staticmethod
    def calculate_interest(principal, rate, time):
        """Calculate simple interest"""
        return principal * rate * time / 100
    
    @staticmethod
    def generate_account_statement(transactions, num_transactions=5):
        """Generate account statement using list slicing"""
        recent_transactions = transactions[-num_transactions:] if transactions else []
        return recent_transactions
    
    @staticmethod
    def analyze_transactions(transactions):
        """Analyze transactions using functional programming concepts"""
        if not transactions:
            return {}
        
        # Using map and lambda to extract amounts
        amounts = list(map(lambda t: t[2], transactions))
        
        # Using filter to get deposits and withdrawals
        deposits = list(filter(lambda t: t[1] == 'Deposit', transactions))
        withdrawals = list(filter(lambda t: t[1] == 'Withdrawal', transactions))
        transfers = list(filter(lambda t: t[1] == 'Transfer', transactions))
        
        # Using reduce to calculate totals
        total_deposits = reduce(lambda x, y: x + y, [t[2] for t in deposits], 0)
        total_withdrawals = reduce(lambda x, y: x + y, [abs(t[2]) for t in withdrawals], 0)
        
        # Using set to get unique transaction types
        transaction_types = set(t[1] for t in transactions)
        
        # Using dictionary comprehension
        type_stats = {t_type: len([t for t in transactions if t[1] == t_type]) 
                     for t_type in transaction_types}
        
        return {
            'total_transactions': len(transactions),
            'transaction_types': transaction_types,
            'type_stats': type_stats,
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals,
            'net_flow': total_deposits - total_withdrawals
        }

# Create an instance of the banking module
banking_module = BankingModule()

class SmartBankr:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartBankr - Banking System")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f8ff')
        
        # Apply a modern theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Customize styles
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'), 
                            background='#f0f8ff', foreground='#2c3e50')
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'), 
                            background='#f0f8ff', foreground='#34495e')
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TNotebook', background='#f0f8ff')
        self.style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'))
        
        # Initialize data structures
        self.accounts = {}  # Dictionary to store account information
        self.transactions = {}  # Dictionary to store transaction history
        self.current_user = None
        
        # Create some sample accounts for testing
        self.create_sample_data()
        
        # Create the main interface
        self.create_welcome_screen()
    
    def create_sample_data(self):
        """Create sample accounts and transactions for demonstration"""
        # Sample accounts
        sample_accounts = {
            '1234567890': banking_module.create_account('1234567890', 'John Doe', 
                                                       'john@email.com', '1234567890', 
                                                       5000.00, '1234'),
            '0987654321': banking_module.create_account('0987654321', 'Jane Smith', 
                                                       'jane@email.com', '0987654321', 
                                                       3000.00, '5678')
        }
        
        # Sample transactions using tuples
        sample_transactions = {
            '1234567890': [
                ('2023-01-15', 'Deposit', 1000.00, 'Initial Deposit', 1000.00),
                ('2023-02-01', 'Withdrawal', 200.00, 'ATM Withdrawal', 800.00),
                ('2023-02-15', 'Deposit', 500.00, 'Salary', 1300.00),
                ('2023-03-01', 'Transfer', 300.00, 'To Jane Smith', 1000.00),
            ],
            '0987654321': [
                ('2023-01-20', 'Deposit', 500.00, 'Initial Deposit', 500.00),
                ('2023-02-05', 'Deposit', 1000.00, 'Salary', 1500.00),
                ('2023-02-20', 'Withdrawal', 100.00, 'Shopping', 1400.00),
                ('2023-03-01', 'Transfer', 300.00, 'From John Doe', 1700.00),
            ]
        }
        
        self.accounts.update(sample_accounts)
        self.transactions.update(sample_transactions)
        
    def create_welcome_screen(self):
        """Create the welcome screen with login and registration options"""
        self.clear_screen()
        
        # Title frame
        title_frame = ttk.Frame(self.root, style='TFrame')
        title_frame.pack(pady=30)
        
        title_label = ttk.Label(title_frame, text="SmartBankr", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Your Smart Banking Solution", 
                                  font=('Arial', 14), background='#f0f8ff', foreground='#7f8c8d')
        subtitle_label.pack(pady=10)
        
        # Button frame
        button_frame = ttk.Frame(self.root, style='TFrame')
        button_frame.pack(pady=50)
        
        login_btn = ttk.Button(button_frame, text="Login", 
                              command=self.create_login_screen, width=20)
        login_btn.pack(pady=10)
        
        register_btn = ttk.Button(button_frame, text="Register New Account", 
                                 command=self.create_registration_screen, width=20)
        register_btn.pack(pady=10)
        
        # Features frame
        features_frame = ttk.LabelFrame(self.root, text="SmartBankr Features", 
                                       style='TFrame', padding=20)
        features_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        features = [
            "• Secure Account Management",
            "• Easy Fund Transfers",
            "• Transaction History",
            "• Account Analytics",
            "• 24/7 Banking Access"
        ]
        
        for feature in features:
            feature_label = ttk.Label(features_frame, text=feature, 
                                     font=('Arial', 12), background='#f0f8ff')
            feature_label.pack(anchor='w', pady=5)
    
    def create_login_screen(self):
        """Create the login screen"""
        self.clear_screen()
        
        # Back button
        back_btn = ttk.Button(self.root, text="← Back", command=self.create_welcome_screen)
        back_btn.place(x=10, y=10)
        
        # Login frame
        login_frame = ttk.Frame(self.root, style='TFrame')
        login_frame.pack(expand=True)
        
        title_label = ttk.Label(login_frame, text="Login to SmartBankr", style='Header.TLabel')
        title_label.pack(pady=20)
        
        # Account number
        acc_num_label = ttk.Label(login_frame, text="Account Number:", 
                                 font=('Arial', 12), background='#f0f8ff')
        acc_num_label.pack(pady=10)
        
        self.acc_num_entry = ttk.Entry(login_frame, font=('Arial', 12), width=20)
        self.acc_num_entry.pack(pady=5)
        
        # PIN
        pin_label = ttk.Label(login_frame, text="PIN:", 
                             font=('Arial', 12), background='#f0f8ff')
        pin_label.pack(pady=10)
        
        self.pin_entry = ttk.Entry(login_frame, font=('Arial', 12), 
                                  width=20, show='*')
        self.pin_entry.pack(pady=5)
        
        # Login button
        login_btn = ttk.Button(login_frame, text="Login", 
                              command=self.validate_login, width=20)
        login_btn.pack(pady=20)
        
        # Demo accounts info
        demo_frame = ttk.Frame(login_frame, style='TFrame')
        demo_frame.pack(pady=10)
        
        demo_label = ttk.Label(demo_frame, text="Demo Accounts:\n1234567890 (PIN: 1234)\n0987654321 (PIN: 5678)", 
                              font=('Arial', 10), background='#f0f8ff', foreground='#7f8c8d')
        demo_label.pack()
        
        # Error label
        self.login_error = ttk.Label(login_frame, text="", 
                                    foreground='red', background='#f0f8ff')
        self.login_error.pack()
    
    def validate_login(self):
        """Validate login credentials"""
        acc_num = self.acc_num_entry.get().strip()
        pin = self.pin_entry.get().strip()
        
        # Validation using regular expressions
        if not re.match(r'^\d{10}$', acc_num):
            self.login_error.config(text="Account number must be 10 digits")
            return
        
        if not re.match(r'^\d{4}$', pin):
            self.login_error.config(text="PIN must be 4 digits")
            return
        
        # Check if account exists and PIN is correct
        if acc_num in self.accounts:
            if self.accounts[acc_num]['pin'] == pin:
                self.current_user = acc_num
                self.create_dashboard()
            else:
                self.login_error.config(text="Invalid PIN")
        else:
            self.login_error.config(text="Account not found")
    
    def create_registration_screen(self):
        """Create the account registration screen"""
        self.clear_screen()
        
        # Back button
        back_btn = ttk.Button(self.root, text="← Back", command=self.create_welcome_screen)
        back_btn.place(x=10, y=10)
        
        # Registration frame
        reg_frame = ttk.Frame(self.root, style='TFrame')
        reg_frame.pack(expand=True, padx=50)
        
        title_label = ttk.Label(reg_frame, text="Create New Account", style='Header.TLabel')
        title_label.pack(pady=20)
        
        # Form fields
        fields = [
            ("Full Name:", "name_entry"),
            ("Email:", "email_entry"),
            ("Phone:", "phone_entry"),
            ("Initial Deposit ($):", "deposit_entry"),
            ("Create 4-digit PIN:", "pin_entry")
        ]
        
        self.reg_entries = {}
        
        for label_text, entry_name in fields:
            label = ttk.Label(reg_frame, text=label_text, 
                             font=('Arial', 12), background='#f0f8ff')
            label.pack(pady=5)
            
            entry = ttk.Entry(reg_frame, font=('Arial', 12), width=25)
            entry.pack(pady=5)
            
            self.reg_entries[entry_name] = entry
        
        # Register button
        register_btn = ttk.Button(reg_frame, text="Register Account", 
                                 command=self.validate_registration, width=20)
        register_btn.pack(pady=20)
        
        # Error label
        self.reg_error = ttk.Label(reg_frame, text="", 
                                  foreground='red', background='#f0f8ff')
        self.reg_error.pack()
    
    def validate_registration(self):
        """Validate registration form and create account"""
        # Get form data
        name = self.reg_entries['name_entry'].get().strip()
        email = self.reg_entries['email_entry'].get().strip()
        phone = self.reg_entries['phone_entry'].get().strip()
        deposit = self.reg_entries['deposit_entry'].get().strip()
        pin = self.reg_entries['pin_entry'].get().strip()
        
        # Validation using regular expressions
        if not re.match(r'^[A-Za-z\s]{3,}$', name):
            self.reg_error.config(text="Please enter a valid name")
            return
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.reg_error.config(text="Please enter a valid email")
            return
        
        if not re.match(r'^\d{10}$', phone):
            self.reg_error.config(text="Phone must be 10 digits")
            return
        
        if not re.match(r'^\d+(\.\d{1,2})?$', deposit) or float(deposit) < 10:
            self.reg_error.config(text="Deposit must be at least $10")
            return
        
        if not re.match(r'^\d{4}$', pin):
            self.reg_error.config(text="PIN must be 4 digits")
            return
        
        # Generate account number
        acc_num = self.generate_account_number()
        
        # Create account using custom module
        account_data = banking_module.create_account(acc_num, name, email, phone, float(deposit), pin)
        
        # Store account information
        self.accounts[acc_num] = account_data
        self.transactions[acc_num] = []
        
        # Add initial deposit transaction
        initial_transaction = (
            datetime.now().strftime('%Y-%m-%d'),
            'Deposit',
            float(deposit),
            'Initial Deposit',
            float(deposit)
        )
        self.transactions[acc_num].append(initial_transaction)
        
        # Show success message
        messagebox.showinfo("Registration Successful", 
                           f"Account created successfully!\nYour account number is: {acc_num}")
        
        self.create_welcome_screen()
    
    def generate_account_number(self):
        """Generate a unique 10-digit account number"""
        while True:
            acc_num = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            if acc_num not in self.accounts:
                return acc_num
    
    def create_dashboard(self):
        """Create the main dashboard after login"""
        self.clear_screen()
        
        # Header with user info
        header_frame = ttk.Frame(self.root, style='TFrame')
        header_frame.pack(fill='x', padx=20, pady=10)
        
        user_info = self.accounts[self.current_user]
        welcome_label = ttk.Label(header_frame, 
                                 text=f"Welcome, {user_info['name']}!", 
                                 style='Header.TLabel')
        welcome_label.pack(side='left')
        
        balance_label = ttk.Label(header_frame, 
                                 text=f"Balance: ${user_info['balance']:.2f}", 
                                 font=('Arial', 14, 'bold'), 
                                 background='#f0f8ff', foreground='#27ae60')
        balance_label.pack(side='right')
        
        # Logout button
        logout_btn = ttk.Button(header_frame, text="Logout", 
                               command=self.create_welcome_screen)
        logout_btn.pack(side='right', padx=10)
        
        # Tab control for different features
        tab_control = ttk.Notebook(self.root)
        
        # Account info tab
        account_tab = ttk.Frame(tab_control, style='TFrame')
        tab_control.add(account_tab, text='Account Info')
        
        # Transactions tab
        transactions_tab = ttk.Frame(tab_control, style='TFrame')
        tab_control.add(transactions_tab, text='Transactions')
        
        # Transfer tab
        transfer_tab = ttk.Frame(tab_control, style='TFrame')
        tab_control.add(transfer_tab, text='Transfer Funds')
        
        # Analytics tab
        analytics_tab = ttk.Frame(tab_control, style='TFrame')
        tab_control.add(analytics_tab, text='Account Analytics')
        
        tab_control.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Populate tabs
        self.populate_account_tab(account_tab)
        self.populate_transactions_tab(transactions_tab)
        self.populate_transfer_tab(transfer_tab)
        self.populate_analytics_tab(analytics_tab)
    
    def populate_account_tab(self, tab):
        """Populate the account information tab"""
        user_info = self.accounts[self.current_user]
        
        info_frame = ttk.LabelFrame(tab, text="Account Details", padding=20)
        info_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        details = [
            ("Account Number:", self.current_user),
            ("Account Holder:", user_info['name']),
            ("Email:", user_info['email']),
            ("Phone:", user_info['phone']),
            ("Account Type:", user_info['account_type']),
            ("Account Status:", user_info['status']),
            ("Member Since:", user_info['created_at'])
        ]
        
        for label, value in details:
            row_frame = ttk.Frame(info_frame, style='TFrame')
            row_frame.pack(fill='x', pady=5)
            
            label_widget = ttk.Label(row_frame, text=label, 
                                   font=('Arial', 12, 'bold'), 
                                   background='#f0f8ff', width=15)
            label_widget.pack(side='left')
            
            value_widget = ttk.Label(row_frame, text=value, 
                                   font=('Arial', 12), 
                                   background='#f0f8ff')
            value_widget.pack(side='left')
        
        # Balance display with special styling
        balance_frame = ttk.Frame(info_frame, style='TFrame')
        balance_frame.pack(fill='x', pady=20)
        
        balance_label = ttk.Label(balance_frame, text="Current Balance:", 
                                 font=('Arial', 14, 'bold'), 
                                 background='#f0f8ff')
        balance_label.pack(side='left')
        
        balance_value = ttk.Label(balance_frame, 
                                 text=f"${user_info['balance']:.2f}", 
                                 font=('Arial', 16, 'bold'), 
                                 background='#f0f8ff', foreground='#27ae60')
        balance_value.pack(side='left', padx=10)
    
    def populate_transactions_tab(self, tab):
        """Populate the transactions history tab"""
        # Header
        header_frame = ttk.Frame(tab, style='TFrame')
        header_frame.pack(fill='x', padx=20, pady=10)
        
        title_label = ttk.Label(header_frame, text="Transaction History", 
                               style='Header.TLabel')
        title_label.pack(side='left')
        
        # Add transaction button
        add_btn = ttk.Button(header_frame, text="Add Sample Transaction", 
                            command=self.add_sample_transaction)
        add_btn.pack(side='right')
        
        # Transactions list
        list_frame = ttk.Frame(tab, style='TFrame')
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create a treeview for transactions
        columns = ('Date', 'Type', 'Amount', 'Description', 'Balance')
        self.transaction_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.transaction_tree.heading(col, text=col)
            self.transaction_tree.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', 
                                 command=self.transaction_tree.yview)
        self.transaction_tree.configure(yscrollcommand=scrollbar.set)
        
        self.transaction_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Load transactions
        self.load_transactions()
    
    def add_sample_transaction(self):
        """Add sample transaction to demonstrate functionality"""
        # Tuple operations demonstration
        transaction_types = ('Deposit', 'Withdrawal', 'Transfer')
        selected_type = random.choice(transaction_types)
        
        if selected_type == 'Deposit':
            amount = random.randint(100, 1000)
            description = 'Sample Deposit'
        elif selected_type == 'Withdrawal':
            amount = -random.randint(10, 200)
            description = 'Sample Withdrawal'
        else:
            amount = -random.randint(50, 300)
            description = 'Sample Transfer'
        
        # Update balance
        current_balance = self.accounts[self.current_user]['balance']
        new_balance = current_balance + amount
        
        # Create transaction tuple
        transaction = (
            datetime.now().strftime('%Y-%m-%d'),
            selected_type,
            amount,
            description,
            new_balance
        )
        
        # Add to transactions list
        self.transactions[self.current_user].append(transaction)
        self.accounts[self.current_user]['balance'] = new_balance
        
        self.load_transactions()
        messagebox.showinfo("Sample Data", "Sample transaction added successfully!")
        self.create_dashboard()  # Refresh to show updated balance
    
    def load_transactions(self):
        """Load transactions into the treeview"""
        # Clear existing items
        for item in self.transaction_tree.get_children():
            self.transaction_tree.delete(item)
        
        # List comprehension to format transactions
        formatted_transactions = [
            (date, t_type, f"${amount:+.2f}", desc, f"${balance:.2f}")
            for date, t_type, amount, desc, balance in self.transactions.get(self.current_user, [])
        ]
        
        # Add transactions to treeview (reverse order - newest first)
        for transaction in reversed(formatted_transactions):
            self.transaction_tree.insert('', 'end', values=transaction)
    
    def populate_transfer_tab(self, tab):
        """Populate the fund transfer tab"""
        transfer_frame = ttk.LabelFrame(tab, text="Transfer Funds", padding=20)
        transfer_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Recipient account
        recip_label = ttk.Label(transfer_frame, text="Recipient Account Number:", 
                               font=('Arial', 12), background='#f0f8ff')
        recip_label.pack(pady=10)
        
        self.recipient_entry = ttk.Entry(transfer_frame, font=('Arial', 12), width=20)
        self.recipient_entry.pack(pady=5)
        
        # Amount
        amount_label = ttk.Label(transfer_frame, text="Amount:", 
                                font=('Arial', 12), background='#f0f8ff')
        amount_label.pack(pady=10)
        
        self.amount_entry = ttk.Entry(transfer_frame, font=('Arial', 12), width=20)
        self.amount_entry.pack(pady=5)
        
        # Description
        desc_label = ttk.Label(transfer_frame, text="Description:", 
                              font=('Arial', 12), background='#f0f8ff')
        desc_label.pack(pady=10)
        
        self.desc_entry = ttk.Entry(transfer_frame, font=('Arial', 12), width=20)
        self.desc_entry.pack(pady=5)
        
        # Transfer button
        transfer_btn = ttk.Button(transfer_frame, text="Transfer Funds", 
                                 command=self.process_transfer, width=20)
        transfer_btn.pack(pady=20)
        
        # Error label
        self.transfer_error = ttk.Label(transfer_frame, text="", 
                                       foreground='red', background='#f0f8ff')
        self.transfer_error.pack()
    
    def process_transfer(self):
        """Process a fund transfer"""
        recipient = self.recipient_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        description = self.desc_entry.get().strip()
        
        # Validation
        if not re.match(r'^\d{10}$', recipient):
            self.transfer_error.config(text="Recipient account must be 10 digits")
            return
        
        if recipient not in self.accounts:
            self.transfer_error.config(text="Recipient account not found")
            return
        
        if recipient == self.current_user:
            self.transfer_error.config(text="Cannot transfer to your own account")
            return
        
        if not re.match(r'^\d+(\.\d{1,2})?$', amount_str):
            self.transfer_error.config(text="Please enter a valid amount")
            return
        
        amount = float(amount_str)
        if amount <= 0:
            self.transfer_error.config(text="Amount must be positive")
            return
        
        # Use custom module for validation
        if not banking_module.validate_transaction(amount, self.accounts[self.current_user]['balance']):
            self.transfer_error.config(text="Insufficient funds")
            return
        
        # Process transfer
        self.accounts[self.current_user]['balance'] -= amount
        self.accounts[recipient]['balance'] += amount
        
        # Record transactions
        current_balance = self.accounts[self.current_user]['balance']
        recipient_balance = self.accounts[recipient]['balance']
        
        # Using tuple for transaction record
        sender_transaction = (
            datetime.now().strftime('%Y-%m-%d'),
            'Transfer',
            -amount,
            f"To {recipient}: {description}",
            current_balance
        )
        
        recipient_transaction = (
            datetime.now().strftime('%Y-%m-%d'),
            'Transfer',
            amount,
            f"From {self.current_user}: {description}",
            recipient_balance
        )
        
        # Add transactions to history
        self.transactions[self.current_user].append(sender_transaction)
        self.transactions[recipient].append(recipient_transaction)
        
        messagebox.showinfo("Transfer Successful", 
                           f"${amount:.2f} transferred successfully to account {recipient}")
        
        # Clear form
        self.recipient_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.transfer_error.config(text="")
        
        # Refresh dashboard to show updated balance
        self.create_dashboard()
    
    def populate_analytics_tab(self, tab):
        """Populate the analytics tab with various data operations"""
        analytics_frame = ttk.LabelFrame(tab, text="Account Analytics", padding=20)
        analytics_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Get transaction data
        transactions = self.transactions.get(self.current_user, [])
        
        if not transactions:
            no_data_label = ttk.Label(analytics_frame, text="No transaction data available", 
                                     font=('Arial', 14), background='#f0f8ff')
            no_data_label.pack(pady=50)
            return
        
        # Use custom module for analytics
        analytics_data = banking_module.analyze_transactions(transactions)
        
        # Demonstration of tuple operations
        transaction_dates = tuple(t[0] for t in transactions)  # Indexing
        recent_dates = transaction_dates[-5:]  # Slicing
        all_dates = transaction_dates + recent_dates  # Concatenation
        repeated_dates = recent_dates * 2  # Repetition
        
        # Membership test
        has_deposits = 'Deposit' in (t[1] for t in transactions)
        has_large_transactions = any(t[2] > 1000 for t in transactions)
        
        # Comparison
        deposit_count = len([t for t in transactions if t[1] == 'Deposit'])
        withdrawal_count = len([t for t in transactions if t[1] == 'Withdrawal'])
        more_deposits = deposit_count > withdrawal_count
        
        # Recursive function demonstration
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        
        # Display analytics
        analytics_text = f"""
        Account Analytics Summary:
        
        Total Transactions: {analytics_data['total_transactions']}
        Unique Transaction Types: {', '.join(analytics_data['transaction_types'])}
        
        Transaction Statistics:
        {', '.join([f'{k}: {v}' for k, v in analytics_data['type_stats'].items()])}
        
        Financial Summary:
        Total Deposits: ${analytics_data['total_deposits']:.2f}
        Total Withdrawals: ${analytics_data['total_withdrawals']:.2f}
        Net Flow: ${analytics_data['net_flow']:.2f}
        
        Additional Insights:
        Has Deposits: {'Yes' if has_deposits else 'No'}
        Has Large Transactions (>$1000): {'Yes' if has_large_transactions else 'No'}
        More Deposits Than Withdrawals: {'Yes' if more_deposits else 'No'}
        
        Recent Transaction Dates: {', '.join(recent_dates)}
        
        Fun Fact: Factorial of transaction count ({len(transactions)}) is {factorial(min(len(transactions), 10))}
        """
        
        # Display analytics
        analytics_label = ttk.Label(analytics_frame, text=analytics_text, 
                                   font=('Courier', 9), background='#f0f8ff', 
                                   justify='left')
        analytics_label.pack(fill='both', expand=True)
    
    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartBankr(root)
    root.mainloop()
