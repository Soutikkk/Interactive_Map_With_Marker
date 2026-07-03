# Interactive Map with Marker 🗺️

A simple, lightweight Python project that generates a dynamic, interactive web map with a custom marker using the **Folium** library. 
The map is centered on New Delhi, India, and includes an interactive marker that displays details upon user interaction.

## Features
- 📍 **Custom Marker:** Places a marker at specific geographic coordinates (New Delhi) with a popup tooltip/label.
- 🌐 **Interactive Interface:** Fully interactive map with zoom controls, panning, and multiple map layer capabilities (handled out-of-the-box by Leaflet.js under Folium).
- 💾 **Export to HTML:** Automatically compiles and exports the map into a standalone, portable `map.html` file that can be opened in any web browser.

---

## Technical Stack
- **Python 3.x**
- **Folium** (Python wrapper for Leaflet.js)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Soutikkk/Interactive_Map_With_Marker.git
cd Interactive_Map_With_Marker
```

### 2. Install Dependencies
Make sure you have Python installed, then install the required dependency using `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Usage

Run the Python script to generate the map:
```bash
python app.py
```

This will generate a file named `map.html` in your project folder. Double-click `map.html` or open it in your favorite web browser to view the interactive map.

---

## Code Breakdown (`app.py`)

Here is the quick breakdown of the core code in `app.py`:

```python
import folium

# Initialize and center the map on New Delhi (coordinates: [latitude, longitude])
m = folium.Map(location=[28.61, 77.23], zoom_start=5)

# Add a marker at New Delhi with a popup label
folium.Marker(
    [28.61, 77.23],
    popup="New Delhi"
).add_to(m)

# Export the generated map to an HTML file
m.save("map.html")
```

---

## License
This project is open-source and available under the [MIT License](LICENSE).
