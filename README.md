# CSV Reader 📊

An automated CSV reader project that triggers a Python script via GitHub Actions whenever `deepak.csv` is committed.

## 🎯 Overview

This project automatically reads and displays CSV data in the console whenever changes are made to `deepak.csv` in the repository. It uses GitHub Actions to detect commits (via direct push or Pull Request) and runs a Python script to process the data.

## 📁 Project Structure

```
csv-reader/
├── deepak.csv                   # CSV data file (monitored for changes)
├── read_csv.py                  # Python script to read and display CSV data
├── .github/
│   └── workflows/
│       └── csv-reader.yml       # GitHub Actions workflow
└── README.md                    # This file
```

## ⚙️ How It Works

1. **Commit Changes**: When you commit changes to `deepak.csv` (either directly or via a Pull Request)
2. **Automatic Trigger**: GitHub Actions automatically detects the change
3. **Script Execution**: The workflow sets up Python and runs `read_csv.py`
4. **Console Output**: CSV data is displayed in the GitHub Actions console logs

## 🚀 Usage

### Updating deepak.csv

1. Edit `deepak.csv` with your data:
   ```bash
   # Add a new row
   echo "6,New Person,25,City,Role" >> deepak.csv
   ```

2. Commit and push the changes:
   ```bash
   git add deepak.csv
   git commit -m "Update deepak.csv"
   git push
   ```

3. The workflow will automatically trigger and display the CSV data

### Running Locally

You can also run the script locally to test:

```bash
python read_csv.py
```

## 📋 Requirements

- Python 3.11+ (automatically set up in GitHub Actions)
- No external dependencies required (uses standard library only)

## 🔄 Workflow Details

The GitHub Actions workflow (`csv-reader.yml`) is configured to:

- **Trigger on**: Push and Pull Request events
- **Filter**: Only when `deepak.csv` changes
- **Run on**: Ubuntu latest
- **Steps**:
  1. Checkout repository
  2. Set up Python 3.11
  3. Execute `read_csv.py`
  4. Display results in console

## 📊 Sample Data

The repository includes `deepak.csv` with sample employee data:
- id, name, age, city, role

## 🎨 Features

- ✅ Automatic execution on `deepak.csv` commits
- ✅ Formatted console output with tables
- ✅ Error handling
- ✅ Row count statistics
- ✅ Works with both push and pull requests
- ✅ Lightweight - no external dependencies

## 🔍 Viewing Results

After pushing changes:

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Select the latest workflow run
4. Click on "Read and Display CSV Data" job
5. Expand "Run CSV Reader Script" to see the CSV data output

## 🛠️ Customization

### Modify the Python Script

Edit `read_csv.py` to change how data is processed or displayed.

### Change Trigger Conditions

Edit `.github/workflows/csv-reader.yml` to modify:
- Which branches trigger the workflow
- Additional processing steps
- Notification settings

### Monitor Different Files

To monitor a different CSV file, update:
1. The `paths` section in `.github/workflows/csv-reader.yml`
2. The file path in `read_csv.py`

## 📝 Notes

- The workflow **only** triggers when `deepak.csv` is modified
- Changes to other files (like `README.md` or `read_csv.py`) won't trigger the workflow
- Console output is available in GitHub Actions logs

## 🤝 Contributing

1. Create a new branch
2. Modify `deepak.csv`
3. Create a Pull Request
4. The workflow will run automatically on the PR

## 📄 License

This project is open source and available for use.

---

**Made with ❤️ for automated CSV processing**
