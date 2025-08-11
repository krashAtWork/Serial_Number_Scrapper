# Serial Number Scrapper 🔍

A Python script that searches through all files in a given directory for a specific **serial number pattern** using Regular Expressions and displays results in a Pandas DataFrame.

---

## 📜 How It Works
1. **Set the regex pattern** in the script:
   ```python
   rp = r'N\D{3}-\d{5}'
   ```
   This pattern matches serial numbers like `Nter-15496`.

2. **Scan a directory**:
   - The script checks every file inside `./SerialNumberScrapper/My_Big_Directory`.
   - For each file, it searches for the given regex pattern.

3. **Output results**:
   - Displays a table with:
     - File Name
     - Matched Serial Number
   - Prints the total number of matches found.
   - Shows how long the search took.

---

## 🛠 Requirements
- Python 3.x
- pandas

Install dependencies:
```bash
pip install pandas
```

---

## ▶️ Running the Script
1. Place the files to be searched in:
   ```
   ./SerialNumberScrapper/My_Big_Directory/
   ```
2. Edit the `rp` variable in the script if you want a different regex pattern.
3. Run:
   ```bash
   python main.py
   ```

---

## 📝 Example Output
```
       FILE:      Serial NO.
0  file1.txt   Nter-15496
1  file2.txt   Ncod-29876

Count : 2 found
Search duration: 1 seconds
```

---

## 📄 Customizing
- Change the regex pattern in `rp` to match your target format.
- Adjust the `path` variable to point to your directory.

---

## 🚀 Future Improvements
- Accept regex from user input.
- Add case-insensitive search.
- Export results to CSV or Excel.

---

## 📄 License
Open-source. You are free to modify and share.
