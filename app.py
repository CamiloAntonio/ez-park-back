from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

# Database Models
class Garage(db.Model):
    __tablename__ = 'garages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    total_spots = db.Column(db.Integer, nullable=False)
    available_spots = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relationship with reservations
    reservations = db.relationship('Reservation', backref='garage', lazy=True)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relationship with reservations
    reservations = db.relationship('Reservation', backref='user', lazy=True)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    garage_id = db.Column(db.Integer, db.ForeignKey('garages.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, completed, cancelled
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# API Routes
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'message': 'ezPark API is running', 'status': 'healthy'})

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return jsonify({'message': 'Database connection successful'})
    except Exception as e:
        return jsonify({'error': f'Database connection failed: {str(e)}'}), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Local development server
    app.run(debug=True, host="0.0.0.0")
