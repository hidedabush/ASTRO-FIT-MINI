"""
Push-up exercise module with specific technique requirements
"""
from typing import Dict, Any
from .base import ExerciseModule, ExerciseParameters


class PushupExercise(ExerciseModule):
    """
    Push-up exercise with elbow angle and body alignment requirements.
    """
    
    def __init__(self, parameters: ExerciseParameters = None):
        super().__init__("Push-up", parameters)
        self.target_elbow_angle_deg = 90
        self.angle_tolerance_deg = 20
    
    def get_technique_requirements(self) -> Dict[str, Any]:
        """Define push-up technique requirements."""
        return {
            "primary_joints": ["left_elbow", "right_elbow", "left_shoulder", "right_shoulder"],
            "target_elbow_angle_deg": self.target_elbow_angle_deg,
            "angle_tolerance_deg": self.angle_tolerance_deg,
            "target_tempo_sec": self.parameters.target_tempo_sec,
            "movement_pattern": "bilateral_pushup",
        }
    
    def validate_rep(self, motion_data: Dict[str, float]) -> bool:
        """Validate push-up repetition."""
        # Simplified validation - in reality would check elbow angles
        return True
    
    def get_target_intensity(self) -> float:
        """Get cardiovascular intensity for push-ups."""
        intensity_map = {
            "low": 0.3,
            "moderate": 0.5,
            "high": 0.7,
        }
        return intensity_map.get(self.parameters.intensity_level, 0.5)