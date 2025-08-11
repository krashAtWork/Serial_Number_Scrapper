# Serial Number Scrapper 🔍

A Python script that searches through all files in a directory for a specific **serial number pattern** using Regular Expressions and outputs the results in a Pandas DataFrame.

---

## 📜 How It Works
1. **Set a regex pattern** in the script:
   ```python
   rp = r'N\D{3}-\d{5}'
