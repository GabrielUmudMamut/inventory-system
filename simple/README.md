# 🍱 School Canteen Tracker

A simple Python program that helps a school canteen track daily food sales, see what's being wasted, and make smarter decisions about how much to cook.
---

## 🤔 What Problem Does It Solve?

The school canteen sometimes makes **too much food** (waste) or **too little food** (long queues, unhappy students). This program lets canteen staff log what was prepared and sold each day, then see exactly where the waste is happening.

---

## ▶️ How To Run It

Make sure Python is installed, then open a terminal in the same folder as the file and run:

```bash
python canteen.py
```

No pip installs needed — only uses built-in Python libraries (`json` and `os`).

---

## 🧭 Menu Options

When you run the program you'll see this menu:

```
1 - Add 1 item
2 - View summary of all items
3 - Top 3 wasted items
4 - Delete old save files
5 - Save
6 - Quit
```

**1 — Add 1 item**
Type a food name, how many were prepared, and how many were sold. The program calculates leftovers automatically and saves right away. It also won't let you enter an impossible number (like selling more than you prepared).

**2 — View summary**
Prints a table of every item you've logged with its prepared, sold, and leftover counts — plus the total waste at the bottom.

**3 — Top 3 wasted**
Sorts all your items by leftovers and shows the worst 3 offenders. Useful for spotting patterns like "we always make too many samosas."

**4 — Delete save file**
Wipes `canteen_data.json` completely. Useful for starting a fresh day.

**5 — Save**
Manually saves all current data to the file.

**6 — Quit**
Exits the program. Make sure to save first with option 5 if you haven't already.

---

## 💾 How Data is Saved

All data is stored in a file called `canteen_data.json` in the same folder. It's created automatically the first time you save. Each food item is stored as a record like this:

```json
{
  "name": "samosa",
  "prepared": 50,
  "sold": 35,
  "leftover": 15
}
```

All the records sit together in a list inside that file. When you start the program it loads the file automatically — so your data is always there from the last session.

---

## 💡 How The Code Works

The program is split into small functions, each doing one job:

| Function | What it does |
|----------|-------------|
| `load_data()` | Reads `canteen_data.json` at startup and returns the saved list |
| `save_data()` | Writes the current list back to the file |
| `del_data()` | Deletes the save file entirely |
| `add_item()` | Asks for item details, validates the input, builds a dictionary, appends it to the list |
| `view_summary()` | Loops through the list and prints each item + running total of waste |
| `top_wasted()` | Sorts by leftover count and prints the top 3 |
| `clear_screen()` | Clears the terminal so it doesn't look messy on startup |
| `main()` | Runs the menu loop and calls the right function based on what you pick |

### Input validation
The program checks every number you type. It won't accept letters, negative numbers, or a sold count higher than the prepared count. If you type something wrong it just asks again instead of crashing.

### The save file
Uses Python's built-in `json` module to convert the list of dictionaries into a readable text file and back. Nothing fancy — open the file in any text editor and you can read it directly.

---

## 🗂️ Files

| File | Purpose |
|------|---------|
| `canteen.py` | The whole program — run this |
| `canteen_data.json` | Auto-generated when you save; stores all your data |

---

----------|-----------------|
| While loop menu | `main()` |
| Dictionaries + list of dicts | Each item stored as a dict inside the `data` list |
| File saving / loading | `save_data()` and `load_data()` using JSON |
| Input validation | `try/except` + range checks in `add_item()` |
| Useful output | Summary table, top 3 wasted items |
| Functions (2+) | 8 functions total |

---

## 🌍 Real-World Impact

Less food waste means less money thrown away and less environmental impact. By seeing which items are consistently over-prepared, the canteen can adjust quantities over time and run more efficiently.

---

Made by Gabriel