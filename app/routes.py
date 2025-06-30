from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.models import Plant

# Create blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Main plant listing page"""
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

@main.route('/add', methods=['GET', 'POST'])
def add_plant():
    """Add new plant form and handler"""
    if request.method == 'POST':
        try:
            last_watered = datetime.strptime(request.form['last_watered'], '%Y-%m-%d').date()
            new_plant = Plant(
                name=request.form['name'],
                species=request.form['species'],
                water_frequency=int(request.form['water_frequency']),
                last_watered=last_watered,
                notes=request.form['notes']
            )
            db.session.add(new_plant)
            db.session.commit()
            flash('Plant added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error adding plant. Please try again.', 'error')
        return redirect(url_for('main.index'))
    return render_template('add_plant.html')

@main.route('/water/<int:plant_id>')
def water_plant(plant_id):
    """Update plant's last watered date"""
    plant = Plant.query.get_or_404(plant_id)
    try:
        plant.last_watered = datetime.now().date()
        db.session.commit()
        flash(f'{plant.name} watered!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating plant. Please try again.', 'error')
    return redirect(url_for('main.index'))

@main.route('/delete/<int:plant_id>')
def delete_plant(plant_id):
    """Delete plant from collection"""
    plant = Plant.query.get_or_404(plant_id)
    try:
        plant_name = plant.name
        db.session.delete(plant)
        db.session.commit()
        flash(f'{plant_name} deleted!', 'info')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting plant. Please try again.', 'error')
    return redirect(url_for('main.index'))

@main.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Test database connection
        from sqlalchemy import text
        db.session.execute(text('SELECT 1'))
        return {'status': 'healthy', 'database': 'connected'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500

# Template filters
@main.app_template_filter('days_since')
def days_since_filter(date_obj):
    """Template filter to calculate days since date"""
    try:
        if isinstance(date_obj, str):
            date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()
        return (datetime.now().date() - date_obj).days
    except:
        return 0

@main.app_template_filter('needs_water')
def needs_water_filter(plant):
    """Template filter to check if plant needs water"""
    try:
        return plant.needs_water()
    except:
        return True