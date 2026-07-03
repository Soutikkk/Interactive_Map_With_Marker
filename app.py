import folium

# Coordinates for New Delhi
location = [28.61, 77.23]

# Create a map centered on New Delhi
m = folium.Map(
    location=location,
    zoom_start=5
)

# Add a marker for New Delhi
folium.Marker(
    location=location,
    popup="New Delhi",
    tooltip="Click to view"
).add_to(m)

# Save the map as an HTML file
output_file = "map.html"
m.save(output_file)

print(f"Map successfully saved as '{output_file}'")

# Display the map (works in Jupyter Notebook)
m
