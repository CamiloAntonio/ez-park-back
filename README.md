# ezPark Backend

Flask API server for the ezPark parking reservation mobile app.

## 🏗️ Architecture

- **Framework**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL (Google Cloud SQL)
- **Deployment**: Docker + SSH to remote server
- **Environment**: Python 3.11

## 🗃️ Database Models

- **Garage**: Parking locations with pricing and availability
- **User**: User accounts for reservations
- **Reservation**: Booking records linking users to garages

## 🚀 Quick Start

### 1. Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your database credentials
# DATABASE_URL=postgresql://username:password@host:port/database

# Run locally (without Docker)
python app.py
```

### 2. Docker Development

```bash
# Start with Docker (includes PostgreSQL if configured)
make dev

# Or manually:
docker-compose up --build
```

## 🔧 Common Commands

### Database Management

# Test database connection

curl http://localhost:5000/test-db

# Get all garages

curl http://localhost:5000/garages

````

### Remote Server Deployment

```bash
# Deploy code to remote server
make deploy

# Start services on remote server
make ssh-up

# View logs from remote server
make ssh-logs

# Stop service on the remote server
make ssh-stop

# Connect to remote server
make connect
````

## 🌐 API Endpoints

| Method | Endpoint   | Description              |
| ------ | ---------- | ------------------------ |
| `GET`  | `/`        | Health check             |
| `GET`  | `/garages` | List all parking garages |
| `GET`  | `/test-db` | Test database connection |

## ⚙️ Environment Variables

Create a `.env` file with:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@host:port/database

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
```

## 🛠️ Troubleshooting

### Database Connection Issues

**Problem**: `psycopg2.OperationalError: connection to server failed`

**Solutions**:

1. Check database is running
2. Verify credentials in `.env`
3. For Google Cloud SQL: Check authorized networks
4. For high latency: Connection may timeout (Argentina ↔ Oregon)

### Docker Permission Issues

**Problem**: `PermissionError: [Errno 13] Permission denied`

**Solution**: Add user to docker group on remote server:

```bash
ssh -i ~/.ssh/ez-gcp -l username server_ip
sudo usermod -aG docker $USER
# Log out and back in
```

### Port Already in Use

**Problem**: `Port 5000 is already in use`

**Solution**: Kill the process or use different port:

```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9

# Or run on different port
python app.py  # Will use port 5000
```

## 📝 Development Notes

- Tables are created automatically by SQLAlchemy on first run
- Use `seed-garages` endpoint to populate sample data
- High latency connections (Argentina ↔ Oregon) may timeout
- For production: Use environment-specific `.env` files

## 🔄 Development Workflow

1. **Make changes** to Python code
2. **Test locally**: `python app.py`
3. **Deploy**: `make deploy`
4. **Start remote**: `make ssh-up`
5. **Check logs**: `make ssh-logs`

## 📚 Useful Commands

```bash
# Check what's running
docker ps

# Stop all containers
docker-compose down

# Rebuild after changes
docker-compose up --build

# View app logs
docker-compose logs flask-app

# Access container shell
docker-compose exec flask-app bash
```
