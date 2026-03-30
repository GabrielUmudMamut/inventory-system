# 📦 Inventory Manager

A terminal-based inventory tracking system for any business that sells products. Record daily stock, track what sells and what's wasted, calculate averages over time, and get AI-generated business insights — all from the command line, with a web dashboard to visualise the data.

---

## What It Does

This system lets you log how many units of each product you **made/stocked**, how many you **sold**, and tracks the **profit and waste** automatically based on your cost and selling prices. Over time, you can analyse trends and get advice on what to produce more or less of.

---

## File Overview

| File | Purpose |
|---|---|
| `main.py` | Entry point. Runs the main menu. |
| `getdata.py` | Records a new day's inventory data. Saves prices so you don't have to re-enter them. |
| `report.py` | View the saved record for any specific week/day. |
| `average.py` | Calculates averages across a range of days and saves a report. |
| `visualizer.py` | Prints a colour-coded sell-through bar chart in the terminal. |
| `insight.py` | Sends your average data to a Gemini AI model and gets business advice back. |
| `test.py` | Quick utility to verify the manifest file is valid. |
| `index.html` | Web dashboard. Open in a browser to see charts and daily records. |
| `_env` | Template for your environment variables (e.g. API key). |

---

## How to Run

### 1. Install dependencies

```bash
pip install google-generativeai
```

### 2. Set your Gemini API key

Either export it in your terminal:

```bash
export GEMINI_API_KEY="your_key_here"
```

Or rename `_env` to `.env` and fill in your key (requires `python-dotenv` if you want auto-loading).

### 3. Start the program

```bash
python main.py
```

---

## Menu Options

```
1. Record Daily Inventory   → Log a new day's products, quantities, costs, and prices
2. View a Specific Day      → Print a formatted report for any past day
3. Crunch the Averages      → Analyse a date range and compute per-item averages
4. Get AI Business Insights → Ask an AI consultant to review your averages
5. Exit
```

---

## Data Storage

All data is saved as JSON files in a `data/` folder that is created automatically.

| File | What's in it |
|---|---|
| `data/w{week}d{day}.json` | One file per day recorded (e.g. `w1d3.json` = Week 1, Day 3) |
| `data/prices.json` | Price memory — reused automatically on future entries |
| `data/manifest.json` | Index of all recorded days (used by the web dashboard) |
| `data/average_report.json` | Output of the Average Calculator |
| `data/insight_report.json` | Output of the AI Insight tool |

---

## Web Dashboard

Open `index.html` in your browser (from the same directory as the `data/` folder) to see:

- **AI Consultant Insights** — alerts for high-waste items and praise for top sellers
- **Production vs. Sales chart** — visual bar chart comparing stock vs. sold per item
- **Net Profit chart** — profit breakdown per product
- **Global Averages table** — average made, sold, profit, and waste loss
- **Past Records grid** — cards for every day you've logged

> The dashboard reads directly from the JSON files in `data/`, so just refresh it after running any Python tool.

---

## Notes

- **Week and day numbers** are whatever you define them to be — there's no fixed calendar. Week 1 Day 1 is just your starting point.
- **Price memory** means you only need to enter costs and prices once per product. You'll be prompted if you want to update them.
- The system works for **any type of product** — not just food. Anything with a cost price, a sell price, and a quantity works.
