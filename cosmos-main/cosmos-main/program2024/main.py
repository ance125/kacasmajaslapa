from website import create_app
from flask import send_file, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import os 

app = create_app()

@app.route('/jupiter_histogram')
def jupiter_histogram():
    df = pd.read_csv('jupitera_menesi.csv')

    plt.figure(figsize=(10, 6))
    df.plot(x='Moon Name', y='Diameter (km)', kind='bar', color='tan', legend=False)
    plt.xlabel('Moon Name', fontsize=10)
    plt.ylabel('Diameter (km)', fontsize=10)
    plt.title('Jupiter Moon Diameters', fontsize=12)
    plt.xticks(rotation=45, fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches="tight")
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/')
def home():
    return render_template('mars.html')  # Ensure mars.html exists

@app.route('/weather_chart')
def weather_chart():
    try:
        df = pd.read_csv('static/weather.csv', delimiter='\t')  # Adjust if needed
        df['date'] = pd.to_datetime(df['date'])

        plt.figure(figsize=(10, 5))
        plt.plot(df['date'], df['min_temp'], label='Min Temp', color='blue')
        plt.plot(df['date'], df['max_temp'], label='Max Temp', color='red')
        plt.plot(df['date'], df['average temperature'], label='Avg Temp', color='green')

        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Trends Over Time')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)

        img_io = io.BytesIO()
        plt.savefig(img_io, format='png', bbox_inches='tight')
        img_io.seek(0)
        plt.close()
        return send_file(img_io, mimetype='image/png')

    except FileNotFoundError:
        return "Error: weather.csv not found in static/ folder", 404

if __name__ == '__main__':
    app.run(debug=True)
