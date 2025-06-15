import csv
from datetime import datetime

def stock_portfolio_tracker():
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 135.20,
        "MSFT": 420.30,
        "AMZN": 145.80,
        "META": 315.45,
        "NVDA": 875.25,
        "NFLX": 485.60,
        "UBER": 62.40,
        "SPOT": 198.30
    }
    
    portfolio = {}
    total_investment = 0
    
    print("📈 Stock Portfolio Tracker")
    print("=" * 40)
    print("Available Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    print("=" * 40)
    
    while True:
        print("\n1. Add Stock to Portfolio")
        print("2. View Portfolio")
        print("3. Calculate Total Investment")
        print("4. Save Portfolio to File")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            add_stock_to_portfolio(stock_prices, portfolio)
        
        elif choice == "2":
            view_portfolio(portfolio, stock_prices)
        
        elif choice == "3":
            total_investment = calculate_total_investment(portfolio, stock_prices)
            print(f"\n💰 Total Portfolio Value: ${total_investment:.2f}")
        
        elif choice == "4":
            save_portfolio_to_file(portfolio, stock_prices)
        
        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker! 👋")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-5.")

def add_stock_to_portfolio(stock_prices, portfolio):
    """Add a stock to the portfolio"""
    stock_symbol = input("\nEnter stock symbol (e.g., AAPL): ").upper().strip()
    
    if stock_symbol not in stock_prices:
        print(f"❌ Stock '{stock_symbol}' not found in our database.")
        return
    
    try:
        quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            return
        
        if stock_symbol in portfolio:
            portfolio[stock_symbol] += quantity
            print(f"✅ Added {quantity} more shares of {stock_symbol}")
        else:
            portfolio[stock_symbol] = quantity
            print(f"✅ Added {quantity} shares of {stock_symbol} to portfolio")
            
    except ValueError:
        print("❌ Please enter a valid number for quantity!")

def view_portfolio(portfolio, stock_prices):
    """Display the current portfolio"""
    if not portfolio:
        print("\n📭 Your portfolio is empty!")
        return
    
    print("\n📊 Your Portfolio:")
    print("-" * 60)
    print(f"{'Stock':<8} {'Quantity':<10} {'Price':<12} {'Total Value':<15}")
    print("-" * 60)
    
    total_value = 0
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        stock_value = quantity * price
        total_value += stock_value
        
        print(f"{stock:<8} {quantity:<10} ${price:<11.2f} ${stock_value:<14.2f}")
    
    print("-" * 60)
    print(f"{'Total Portfolio Value:':<42} ${total_value:.2f}")

def calculate_total_investment(portfolio, stock_prices):
    """Calculate total investment value"""
    total = 0
    for stock, quantity in portfolio.items():
        total += quantity * stock_prices[stock]
    return total

def save_portfolio_to_file(portfolio, stock_prices):
    """Save portfolio to both TXT and CSV files"""
    if not portfolio:
        print("\n📭 Portfolio is empty! Nothing to save.")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to TXT file
    txt_filename = f"portfolio_{timestamp}.txt"
    with open(txt_filename, 'w') as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        total_value = 0
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            stock_value = quantity * price
            total_value += stock_value
            
            file.write(f"Stock: {stock}\n")
            file.write(f"Quantity: {quantity} shares\n")
            file.write(f"Price per share: ${price:.2f}\n")
            file.write(f"Total value: ${stock_value:.2f}\n")
            file.write("-" * 30 + "\n")
        
        file.write(f"\nTOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
    
    # Save to CSV file
    csv_filename = f"portfolio_{timestamp}.csv"
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
        
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            stock_value = quantity * price
            writer.writerow([stock, quantity, f"${price:.2f}", f"${stock_value:.2f}"])
    
    print(f"✅ Portfolio saved to:")
    print(f"   📄 {txt_filename}")
    print(f"   📊 {csv_filename}")

if __name__ == "__main__":
    stock_portfolio_tracker()