# Pumped Storage Hydropower Energy Model App 💡

## Overview 📝

This GitHub repository contains code for a Streamlit application that calculates the available energy (in MWh) in a pumped storage hydroelectric reservoir system.

Streamlit app is here [Pumped Storage Hydropower - Energy Model](https://pumped-storage-energy-model.streamlit.app/).

## Features 🎯

- User-input for reservoir levels and volumes
- Pump and generator efficiency parameters
- Real-time calculations for net head, overall efficiency, and available energy

## How it Works 🛠️

1. The application starts by importing Streamlit.
2. A title and an image are displayed on the web page.
3. The user provides various inputs such as reservoir levels, volumes, and efficiency values through Streamlit widgets.
4. Upon clicking the 'Calculate' button, the app performs calculations for:
    - Net Head
    - Overall Efficiency
    - Available Energy (in MWh)

## Requirements 📋

- Streamlit
- Python 3.x

## Installation 📦

\`\`\`bash
pip install streamlit
\`\`\`

## Run 🚀

To run the application:

\`\`\`bash
streamlit run <filename>.py
\`\`\`

## Input/Output 🔄

- **Inputs**: 
  - Upper and lower reservoir levels (m)
  - Upper and lower reservoir volumes (m³)
  - Pump and generator efficiencies
  
- **Outputs**: 
  - Net head (m)
  - Overall efficiency
  - Available energy (MWh)

## Example Output 📊

- Available Energy: 123.4 MWh
- For every 1000 MWh of energy, you could charge 123 Tesla Model S cars.

## License 📄

MIT License

---

For technical details, please consult the source code.
