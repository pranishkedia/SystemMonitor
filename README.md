# SystemMonitor


## Overview
This is a simple system monitoring tool written in Python. It collects and displays real-time information about CPU usage, memory usage, and disk usage on your computer. The tool uses the `psutil` library to gather system metrics, making it cross-platform and compatible with macOS, Windows, and Linux.

## Features
- Monitor CPU usage for each core.
- Display memory usage information, including total, available, used, and percentage of usage.
- Show disk usage information for each mounted partition.

## Requirements
- Python 3.x
- `psutil` library. Install it using the following command:

    ```pip install psutil```

5. The script will start displaying real-time system information, including CPU usage, memory usage, and disk usage.

## How it Works
The system monitoring tool is built with Python and utilizes the `psutil` library for system information gathering. The script runs in an infinite loop, collecting CPU, memory, and disk usage data every 5 seconds. It then prints the collected information in a user-friendly format in the terminal.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

## Disclaimer
This tool is intended for personal use and educational purposes only. Please be mindful of the system metrics you monitor and ensure you have the necessary permissions to access and display system information. The authors of this project are not responsible for any misuse or damage caused by the use of this tool.

## Acknowledgments
- Thanks to the developers of the `psutil` library for providing a powerful and easy-to-use tool for system monitoring.

## Contact
For any questions or feedback, please feel free to contact the project maintainer:
- Name: Pranish Kedia
- Email: pranishk12@gmail.com


