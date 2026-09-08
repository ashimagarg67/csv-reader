# CSV Reader 📊

An automated CSV reader project that triggers Python scripts via GitHub Actions whenever CSV files are committed.

## 🎯 Overview

This project automatically reads and displays CSV data in the console whenever changes are made to CSV files in the repository. It uses GitHub Actions to detect commits (via direct push or Pull Request) and runs a Python script to process the data.

## 📁 Project Structure

```
csv-reader/
├── csv/                          # Directory containing CSV files
│   └── sample_data.csv          # Sample CSV data file
├── read_csv.py                  # Python script to read and display CSV data
├── .github/
│   └── workflows/
│       └── csv-reader.yml       # GitHub Actions workflow
└── README.md                    # This file
```

## ⚙️ How It Works

1. **Commit CSV Changes**: When you commit changes to any file in the `csv/` folder (either directly or via a Pull Request)
2. **Automatic Trigger**: GitHub Actions automatically detects the change
3. **Script Execution**: The workflow sets up Python and runs `read_csv.py`
4. **Console Output**: CSV data is displayed in the GitHub Actions console logs

## 🚀 Usage

### Adding New CSV Files

1. Add your CSV file to the `csv/` directory:
   ```bash
   cp your_data.csv csv/
   ```

2. Commit and push the changes:
   ```bash
   git add csv/your_data.csv
   git commit -m "Add new CSV data file"
   git push
   ```

3. The workflow will automatically trigger and display the CSV data

### Running Locally

You can also run the script locally:

```bash
python read_csv.py
```

## 📋 Requirements

- Python 3.11+ (automatically set up in GitHub Actions)
- No external dependencies required (uses standard library only)

## 🔄 Workflow Details

The GitHub Actions workflow (`csv-reader.yml`) is configured to:

- **Trigger on**: Push and Pull Request events
- **Filter**: Only when files in `csv/` directory change
- **Run on**: Ubuntu latest
- **Steps**:
  1. Checkout repository
  2. Set up Python 3.11
  3. Execute `read_csv.py`
  4. Display results in console

## 📊 Sample Data

The repository includes `sample_data.csv` with employee data for testing purposes.

## 🎨 Features

- ✅ Automatic execution on CSV file commits
- ✅ Formatted console output with tables
- ✅ Reads multiple CSV files
- ✅ Error handling
- ✅ Row count statistics
- ✅ Works with both push and pull requests

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

## 📝 Notes

- The workflow only triggers when CSV files are modified, not on other file changes
- All CSV files in the `csv/` directory will be processed
- Console output is available in GitHub Actions logs

## 🤝 Contributing

1. Create a new branch
2. Add or modify CSV files in the `csv/` directory
3. Create a Pull Request
4. The workflow will run automatically on the PR

## 📄 License

This project is open source and available for use.

---

**Made with ❤️ for automated CSV processing**
