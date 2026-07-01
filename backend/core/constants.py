"""Project-wide constants: feature names, skills, and optimization constraints.

These values are the single source of truth shared across data generation,
feature engineering, model training, and the optimization engine.
"""

from __future__ import annotations

# --- Synthetic data sizing (see PRD) ---
DEFAULT_N_TECHNICIANS: int = 1_000
DEFAULT_N_ASSIGNMENTS: int = 10_000

# --- Skill catalog ---
SKILLS: list[str] = [
    "HVAC",
    "Electrical",
    "Plumbing",
    "Networking",
    "Appliance",
    "Security",
]

# --- The 13 engineered features (see PRD: Feature Engineering) ---
FEATURE_NAMES: list[str] = [
    "distance",
    "normalized_distance",
    "travel_time",
    "workload_ratio",
    "technician_utilization",
    "historical_completion_rate",
    "experience_score",
    "skill_score",
    "priority_weight",
    "sla_remaining_time",
    "rush_hour_flag",
    "weekend_flag",
    "holiday_flag",
]

# The binary training target produced by the data generator.
TARGET_NAME: str = "assignment_success"

# --- Optimization constraints (see PRD: Optimization) ---
HARD_CONSTRAINTS: list[str] = [
    "required_skill",        # technician must possess the requested skill
    "technician_available",  # technician must be available
    "max_daily_jobs",        # respect per-technician daily job cap
    "sla_feasibility",       # assignment must be able to meet the SLA
    "working_hours",         # assignment must fall within working hours
]

SOFT_CONSTRAINTS: list[str] = [
    "minimize_travel",       # prefer shorter travel distance
    "balance_workload",      # spread load evenly across technicians
    "historical_success",    # prefer historically successful pairings
    "customer_priority",     # weight high-priority requests
    "technician_preference", # honor technician preferences
]

# --- Operational defaults ---
DEFAULT_MAX_DAILY_JOBS: int = 8
WORKING_HOURS_START: int = 8   # 08:00
WORKING_HOURS_END: int = 18    # 18:00
AVG_SPEED_KMH: float = 40.0    # used to convert distance -> travel time
