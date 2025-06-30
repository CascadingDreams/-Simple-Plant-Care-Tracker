# 🌱 Plant Care Tracker

A clean and playful Flask web application to help you track your houseplants and their watering schedules with a modern, plant-themed design.

## Features

- 🌱 Add and manage your plants with custom images
- 💧 Track watering schedules with visual indicators
- 🎨 Clean, cute & playful design with fresh green theme
- 📱 Responsive design optimized for all devices
- 🖼️ Custom logo and branding support
- 💾 SQLite database storage
- ⚡ Fast and lightweight Flask backend

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

4. Open your browser to `http://localhost:5001` (or any available port)

### Troubleshooting

**Port already in use?**
If the default port is occupied, run on a different port:
```bash
APP_PORT=8080 python run.py
```
Then visit `http://localhost:8080`

**Common ports to try:** 5001, 8000, 8080, 3000

**CSS not loading?**
This should be automatically fixed. The app is configured to serve static files from the `/static` directory.

**Want to customize the theme?**
Edit `static/css/style.css` to modify colors, spacing, and visual elements. The current theme uses a fresh green color palette perfect for plant care.

## Usage

- **Add Plant**: Click "Add Plant" to register a new plant with its watering schedule
- **Water Plant**: Click "Water Now" when you water a plant to update the last watered date
- **Visual Indicators**: Plants that need water show orange borders and warning badges
- **Plant Images**: Each plant card displays your custom plant placeholder image
- **Clean Interface**: Enjoy the modern, green-themed design that's easy on the eyes
- **Delete Plant**: Remove plants you no longer have with the red delete button

## Data Storage

Plant data is stored in SQLite database at `instance/plants.db`. The database is automatically created when you first run the application.

### Database Schema
Each plant record includes:
- Name and species
- Watering frequency (days)
- Last watered date
- Optional notes
- Creation timestamp

## Customization

### Theme & Appearance
- **Colors**: Edit CSS variables in `static/css/style.css` to change the color scheme
- **Logo**: Replace `static/images/logo.png` with your own logo (recommended: 40px height)
- **Favicon**: Replace `static/images/favicon.ico` with your custom browser icon
- **Plant Images**: Replace `static/images/plant-placeholder.png` with your preferred plant image

### Features
- **Routes**: Modify `app/routes.py` to add new features like fertilizing schedules
- **Database**: Update `app/models.py` to change the database schema
- **Templates**: Edit HTML templates in `app/templates/` for layout changes

### Current Theme
The app uses a **Clean, Cute & Playful** theme with:
- Fresh green color palette (#4CAF50 primary)
- No animations for better performance and accessibility
- Rounded corners and soft shadows
- Modern card-based layout
- Custom branding support (logo, favicon, plant images)
- Responsive design for mobile and desktop
- Clean typography and intuitive interface