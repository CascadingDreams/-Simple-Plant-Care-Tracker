#!/usr/bin/env python3
"""
Plant Care Tracker Application Entry Point

This script creates and runs the Flask application.
"""

import os
from app import create_app

# Create Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('APP_HOST', '0.0.0.0')
    port = int(os.getenv('APP_PORT', 5001))
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    
    # Run the application
    app.run(host=host, port=port, debug=debug)