# Custom HID Library - Titan Two External Signaling
<p align="left">
  <img src="Icons/CHL_T2.png" alt="CHL Logo" width="96"/>
</p>

## Overview
This repository demonstrates how to send signals directly to a Titan Two device **from an external Python environment**, without relying on the Gtuner IDE’s embedded Python.

> **Disclaimer**: This project is intended **for educational purposes**. Use responsibly and abide by all applicable terms, conditions, and regulations for the Titan Two device.

## Features
- **Direct HID Signaling**: Bypass the aging Gtuner back-end and send HID signals straight from Python (or other language) to your Titan Two device.
- **Easy Integration**: The concept can be easily adapted to other languages (C, C++, C#, JavaScript, etc.).
- **Open-Source Collaboration**: Submit pull requests or fork this repo to help expand its capabilities – for instance, by loading GPC scripts and switching Titan Two slots without using the Gtuner IDE.

## Why This Matters
- The official Gtuner IDE is no longer being updated, and its embedded Python environment is becoming antiquated.
- The files and HID signal profile can be easily ported to other languages, including C, C++, C#, and JavaScript.
- By leveraging your own Python environment or other programming language, you can maintain modern libraries, frameworks, and debugging tools.
- We aim to discover a simple way to load GPC scripts and set active slots programmatically, further streamlining Titan Two usage.

## How to Help
We need assistance in refining the GPC push and Slot selection HID signal profiles.
- **GPC Push Signal Profile**
- **Slot Update Signal Profile**

## Getting Started
1. **Clone/Fork** this repository or download the code via ZIP.
2. Ensure your Titan Two device is connected to your system and that you have:
   - [Python 3.x](https://www.python.org/) installed (if you plan to use the sample scripts).
   - Upload the CHL.gpc to the Titan Two and load the slot using Gtuner (for now).
3. **Run the Python script** to establish direct HID communication with Titan Two. 
   - Example usage:
     ```bash
     python CHL.py
     ```
   - Adjust script parameters (e.g., device paths, button mappings) as desired.

## Contributing
1. **Fork** the repository.
2. Create a new feature branch (`git checkout -b feature/someFeature`).
3. Commit your changes (`git commit -m 'Add someFeature'`).
4. Push to the branch (`git push origin feature/someFeature`).
5. **Open a Pull Request** to have your changes reviewed and merged into the main branch.

We welcome push/pull requests that:
- Enhance device-slot management without relying on Gtuner.
- Add cross-language examples (C, C++, C#, JavaScript).
- Improve or optimize HID signaling routines.

## Future Goals
- **Automated GPC Management**: Load GPC scripts and set the active slot programmatically, without ever opening Gtuner.
- **Cross-Platform Support**: Expand tested device and OS compatibility (Linux, macOS, Windows).
- **Community-Driven Improvements**: Encourage collaboration to uncover new features and integrations.

## License
[MIT License](LICENSE)
