# Inventory System
A Python-based inventory tracking and financial analysis tool designed to bridge the gap between daily operations and business insights. 

## 🚀 Features
- Automated Data Processing: Processes daily JSON logs to calculate stock levels and turnover.
- Financial Analytics: Calculates average costs, revenue, and profit/loss margins.
- Business Insights: Generates logic-driven reports to identify trends and stock issues.
- Dual Interface: 
    * Terminal: Quick charts and reports using visualizer.py.
    * Web Dashboard: Interactive HTML/JavaScript frontend powered by Chart.js.

## 📂 Project Structure
- main.py: The central hub for the dashboard and system operations.
- getdata.py: Handles input logic and price memory management.
- average.py: Performs financial mathematics and data crunching.
- insight.py: Generates business logic reports and status updates.
- visualizer.py: Renders terminal-based charts and summaries.
- index.html: The web frontend for visual data representation.

## 🛠️ Installation & Setup
1. Clone the repository:
   git clone https://github.com/GabrielUmudMamut/inventory-system.git
   cd inventory-system

2. Dependencies:
   This project requires Python 3.x. 

3. Data Format:
   The system expects daily logs in the format w{week}d{day}.json.

## 📈 Usage
To process data and update reports:
python main.py

Simply open index.html in any browser to view visual analytics.

## 📝 License
MIT License