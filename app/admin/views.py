from flask import render_template
from app.admin import admin_bp

@admin_bp.route('/')
def admin_dashboard():
    # Admin dashboard logic 
    return {"HI":"Bro"}
#add all admin logic