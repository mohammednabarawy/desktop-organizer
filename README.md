# PyQt5 File Organizer

This is a simple file scanner application built with PyQt5. The application allows you to browse and manage files on your desktop, providing features such as file deletion, list refreshing, and folder browsing.

## Features

- **Delete Selected Files:** Select files from the list and delete them. Deleted files are moved to the system's trash/recycle bin.
- **Refresh List:** Refresh the list of files on your desktop.
- **Browse for Folder:** Browse and view files in a selected folder.

## Installation

1. Make sure you have Python 3 installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt

   ```

4. Usage

Run the application using the following command:

```
python main.py

```

The application window will appear, allowing you to interact with your files.

## File Types and Colors

The application colorizes files in the list based on their file types. Customize the colors in the `set_item_color` method in the `main.py` file.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.
