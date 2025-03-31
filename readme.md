# Personal Expense Tracker

A simple command-line Personal Expense Tracker built with Python and SQLite. This project allows users to manage their financial transactions by adding incomes and expenses, viewing their current balance, filtering transactions by date, and exporting data to a CSV file.

## Features
- Add income and expenses
- List all transactions
- View current balance
- Filter transactions by a specific period
- Export transactions to a CSV file

## Technologies Used
- Python
- SQLite3 (database)
- CSV (for data export)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```
2. Install dependencies (if required):
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- The application runs in the terminal and provides a menu with different options.
- Follow the on-screen prompts to add transactions, check balance, filter transactions, and export data.

## Project Structure
```
├── database.py       # Handles database connection and table creation
├── models.py         # Functions for transaction management and balance calculation
├── utils.py          # Utility functions (e.g., export to CSV)
├── interface.py      # Command-line menu interface
├── main.py           # Entry point of the application
├── requirements.txt  # (Optional) List of dependencies
└── README.md         # Project documentation
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is open-source and available under the MIT License.

