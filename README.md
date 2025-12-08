ASTRO-FIT MINI 🚀
A NASA-aligned virtual exercise coaching system prototype

ASTRO-FIT MINI is a modular, device-agnostic exercise monitoring platform designed for space fitness applications. The system integrates biomedical sensors, real-time technique evaluation, machine learning-based physiological state estimation, and a "Mars Gym" visualization interface.

🎯 Features
Modular Sensor Architecture: Easy integration of new sensors (HR, IMU, etc.)
Exercise Module System: Plug-and-play exercise definitions with technique requirements
Real-time Technique Evaluation: Analyzes movement quality using joint angles and motion data
ML-Powered Fatigue Detection: Random Forest classifier for physiological state estimation
SQLite Database Logging: Complete session history with sensor streams and evaluations
Mars Gym UI: PyQt6 interface with Mars-themed visualization
Mock Data Generation: Synthetic datasets for testing and ML training
📁 Project Structure
astro-fit-mini/
├── config/                  # Configuration files
│   ├── settings.py          # Global settings
│   └── database_schema.sql  # Database schema
├── src/
│   ├── sensors/             # Sensor modules
│   │   ├── base.py          # SensorModule base class
│   │   ├── heart_rate.py    # Mock HR sensor
│   │   ├── motion.py        # Mock IMU sensor
│   │   └── data_generator.py
│   ├── exercises/           # Exercise modules
│   │   ├── base.py          # ExerciseModule base class
│   │   └── squat.py         # Squat implementation
│   ├── evaluation/          # Technique evaluation
│   │   └── technique.py     # TechniqueEvaluator
│   ├── ml/                  # Machine learning
│   │   ├── physiological.py # ML model
│   │   └── training.py      # Training pipeline
│   ├── database/            # Database management
│   │   └── manager.py       # DatabaseManager
│   ├── ui/                  # User interface
│   │   └── mars_gym_qt.py   # PyQt6 UI
│   └── core/                # Core orchestration
│       └── session.py       # ExerciseSession coordinator
├── data/                    # Data storage
│   ├── synthetic/           # Generated training data
│   ├── models/              # Trained ML models
│   └── sessions.db          # SQLite database
├── requirements.txt
└── main.py                  # Application entry point
🚀 Quick Start
Installation
bash
# Clone repository
git clone <repository-url>
cd astro-fit-mini

# Install dependencies
pip install -r requirements.txt
Running the System
bash
# Launch ASTRO-FIT MINI
python main.py
On first run, the system will:

Initialize SQLite database
Create default user profile
Train ML model (if not exists)
Launch Mars Gym UI
Using the Interface
Start Session: Click "Start Session" to begin monitoring
Complete Reps: Click "Complete Rep" after each repetition
Stop Session: Click "Stop Session" to end and save data
🧪 Training the ML Model
The physiological state estimator can be trained standalone:

bash
python src/ml/training.py
This generates synthetic data and trains a Random Forest classifier to detect fatigue levels:

Fresh: Low HR, high motion intensity
Moderate: Elevated HR, moderate intensity
Fatigued: High HR, low motion intensity
🔧 Adding New Components
Adding a New Sensor
python
from src.sensors.base import SensorModule

class CustomSensor(SensorModule):
    def start(self):
        # Initialize sensor
        return True
    
    def stop(self):
        # Cleanup
        return True
    
    def read(self):
        # Return sensor data
        return {
            "timestamp": time.time(),
            "data": self.get_reading()
        }
Adding a New Exercise
python
from src.exercises.base import ExerciseModule

class PushupExercise(ExerciseModule):
    def get_technique_requirements(self):
        return {
            "primary_joints": ["left_elbow", "right_elbow"],
            "target_depth_deg": 90,
            # ... other requirements
        }
    
    def validate_rep(self, motion_data):
        # Validate rep quality
        return True
📊 Database Schema
The SQLite database includes:

users: User profiles
sessions: Exercise sessions
heart_rate_data: HR sensor stream
motion_data: Joint angle stream
technique_evaluations: Per-rep technique scores
physiological_states: ML predictions
Query example:

python
from src.database.manager import DatabaseManager
db = DatabaseManager("data/sessions.db")

# Get user's recent sessions
sessions = db.get_user_sessions(user_id=1, limit=5)
🤖 ML Model Architecture
Feature Set:

Average heart rate (30-second window)
Heart rate variability (std dev)
Motion intensity (joint angle variance)
Session progress (0-1)
Model: Random Forest Classifier

100 estimators
Max depth: 10
Balanced class weights
Training: 200 synthetic sessions, 80/20 train/test split

🎨 UI Customization
Modify Mars theme in src/ui/mars_gym_qt.py:

python
def _apply_mars_theme(self):
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(40, 20, 20))
    # Customize colors...
📝 Configuration
Edit config/settings.py for:

Sensor sampling rates
Exercise parameters
ML hyperparameters
Database settings
UI refresh rates
🧪 Testing
bash
# Run unit tests
pytest tests/

# Test specific module
pytest tests/test_sensors.py
📈 Future Enhancements
 Real sensor integration (Bluetooth HR monitors)
 Computer vision joint tracking (MediaPipe)
 Advanced ML models (LSTM for temporal patterns)
 Web-based UI (Flask/React)
 Multi-user support with authentication
 Exercise recommendations based on history
 Export data to NASA formats
📚 Documentation
Key Classes
SensorModule: Abstract base for all sensors
ExerciseModule: Abstract base for exercise definitions
TechniqueEvaluator: Movement quality analysis
PhysiologicalMLModel: Fatigue classification
DatabaseManager: SQLite operations
ExerciseSession: Main orchestration coordinator
Data Flow
Sensors → ExerciseSession → TechniqueEvaluator → Database
                ↓                    ↓
         PhysiologicalML ←────────────┘
                ↓
            Mars Gym UI
🤝 Contributing
This is a prototype system. Contributions welcome:

Fork repository
Create feature branch
Add tests
Submit pull request
📄 License
MIT License - see LICENSE file

👥 Authors
Built for NASA-aligned space fitness applications

🙏 Acknowledgments
NASA Human Research Program
Anthropic Claude for architectural guidance
Open-source ML and Qt communities
Ready for liftoff! 🚀

