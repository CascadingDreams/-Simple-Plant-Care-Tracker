# 🌱 Plant Care Tracker

A simple Flask web application to help you track your houseplants and their watering schedules.

## Features

- Add and manage your plants
- Track watering schedules
- Visual indicators for plants that need water
- Responsive design with Bootstrap
- Simple JSON file storage

## Setup

### Why Use a Virtual Environment?
Virtual environments isolate your project's Python dependencies from the system-wide Python installation. This prevents:
- **Dependency conflicts** - Different projects can use different versions of the same package
- **System breakage** - Installing packages system-wide can break OS tools that rely on specific Python versions
- **Permission issues** - No need for sudo/admin rights to install packages
- **Reproducibility** - Ensures consistent environments across different machines

### Installation Steps

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python run.py
```

4. Open your browser to `http://localhost:5000`

### Troubleshooting

**Port 5000 already in use?**
If port 5000 is occupied, run on a different port:
```bash
APP_PORT=5001 python run.py
```
Then visit `http://localhost:5001`

**CSS not loading?**
This should be automatically fixed. The app is configured to serve static files from the `/static` directory.

## Usage

- **Add Plant**: Click "Add New Plant" to register a new plant with its watering schedule
- **Water Plant**: Click "Water Now" when you water a plant to update the last watered date
- **Visual Indicators**: Plants that need water will have a warning border and badge
- **Delete Plant**: Remove plants you no longer have

## Data Storage

Plant data is stored in SQLite database at `data/plants.db` or `instance/plants.db`.

## Customization

- Edit `static/css/style.css` to customize the appearance
- Modify `app/routes.py` to add new features like fertilizing schedules or plant photos
- Update `app/models.py` to change the database schema