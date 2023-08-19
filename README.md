# Image to PDF Converter

This Python application provides a simple GUI to drag and drop image files, generating a visual thumbnail for each, and allowing users to combine them all into a single PDF.

## Prerequisites

Ensure you have Python 3.x installed on your system. You can check your current Python version by running:
```bash
python --version
```

or

```bash
python3 --version
```

## Installation

1. **Clone this Repository**:
   If you're using git, you can clone this repository to your local machine.
   ```bash
   git clone [YOUR REPO LINK HERE]
   cd [YOUR REPO DIRECTORY]
   ```

   Alternatively, download the source code and navigate to the directory.

2. **Install Required Libraries**:
   This application depends on the `wxPython` and `Pillow` libraries. Install them using pip:
   
   ```bash
   pip install wxPython pillow
   ```

   or if you use `python3` explicitly:
   
   ```bash
   pip3 install wxPython pillow
   ```

## Usage

1. **Run the Program**:
   In the terminal, navigate to the directory containing the script and run:
   
   ```bash
   python path/to/your_script_name.py
   ```

   or if you use `python3` explicitly:

   ```bash
   python3 path/to/your_script_name.py
   ```

2. **Drag and Drop Images**:
   With the GUI window open, drag and drop images into the window one at a time. Thumbnails of the images will appear as they are added.

3. **Save as PDF**:
   Once you've added all desired images, click the "Save as PDF" button located at the bottom of the window. Choose the destination and save your combined PDF.

## Contributing

Contributions, bug reports, and fixes are welcome. Please open an issue or submit a pull request.
