# WinSpeed

WinSpeed is a lightweight Python application that monitors and displays real-time internet connection speeds directly from the Windows taskbar. It provides a convenient way to keep track of your network performance without interrupting your workflow.

## Features

- **Real-time Monitoring**: Continuously tests and updates download and upload speeds every minute.
- **Taskbar Integration**: Displays internet speed directly from the Windows taskbar.
- **Simple Interface**: Easy to use with minimal configuration.

## Installation

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.
2. **Install Dependencies**: Use `pip` to install required packages.
   ```bash
   pip install psutil speedtest-cli PyQt5
   ```
3. **Download the Script**: Save the `winspeed.py` script to your desired location.

## Usage

1. **Run the Application**: Execute the script using Python.
   ```bash
   python winspeed.py
   ```
2. **Access from Taskbar**: Once running, WinSpeed will appear in your system tray. Hover over the icon to see the current download and upload speeds.
3. **Exit**: Right-click the tray icon and select "Quit" to close the application.

## Notes

- **Network Access**: The application requires internet access to test speeds.
- **Icon**: Ensure you have a `network_icon.png` file in the same directory as the script for the tray icon.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
```

This setup will test and display real-time internet speeds from the Windows taskbar using Python and PyQt5. The script leverages `speedtest-cli` to measure the internet speed and `PyQt5` to display it in the system tray.