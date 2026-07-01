/**
 * TypeScript types mirroring the backend Pydantic schemas.
 *
 * Keep these in sync with `backend/schemas/*`. (A future improvement is to
 * auto-generate them from the backend OpenAPI schema.)
 */

export type AlgorithmType = 'greedy' | 'hungarian' | 'ml' | 'dl';

export type ModelType =
  | 'random_forest'
  | 'xgboost'
  | 'lightgbm'
  | 'catboost'
  | 'ffnn'
  | 'tabnet';

export type RequestStatus = 'pending' | 'assigned' | 'completed' | 'cancelled';

export interface GeoPoint {
  lat: number;
  lon: number;
}

export interface Technician {
  id: string;
  name: string;
  location: GeoPoint;
  skills: string[];
  experience_years: number;
  completion_rate: number;
  customer_rating: number;
  current_workload: number;
  max_daily_jobs: number;
  available: boolean;
  utilization: number;
}

export interface ServiceRequest {
  id: string;
  customer_name: string;
  location: GeoPoint;
  required_skill: string;
  priority: number;
  created_at: string;
  sla_deadline: string;
  estimated_duration_min: number;
  status: RequestStatus;
}

export interface FeatureContribution {
  feature: string;
  contribution: number;
}

export interface Assignment {
  id: string;
  technician_id: string;
  request_id: string;
  distance_km: number;
  travel_time_min: number;
  predicted_success: number;
  algorithm: AlgorithmType;
  score: number;
  assigned_at: string;
  explanation: FeatureContribution[];
}

export interface ConfusionMatrix {
  true_negative: number;
  false_positive: number;
  false_negative: number;
  true_positive: number;
}

export interface ModelMetrics {
  model_type: ModelType;
  accuracy: number;
  precision: number;
  recall: number;
  f1: number;
  roc_auc: number;
  confusion_matrix: ConfusionMatrix;
}

export interface FeatureImportance {
  feature: string;
  importance: number;
}

export interface KpiSummary {
  total_technicians: number;
  total_requests: number;
  total_assignments: number;
  avg_utilization: number;
  avg_travel_km: number;
  sla_met_pct: number;
  avg_predicted_success: number;
  customer_satisfaction: number;
}

export interface MetricsResponse {
  kpis: KpiSummary;
  model_metrics: ModelMetrics | null;
  feature_importance: FeatureImportance[];
}

export interface AllocationResult {
  algorithm: AlgorithmType;
  assignments: Assignment[];
  total_score: number;
  unassigned_request_ids: string[];
  kpis: KpiSummary;
  runtime_ms: number;
}

export interface AlgorithmComparisonRow {
  algorithm: AlgorithmType;
  total_score: number;
  assigned_count: number;
  avg_travel_km: number;
  avg_utilization: number;
  sla_met_pct: number;
  runtime_ms: number;
}

export interface CompareResult {
  rows: AlgorithmComparisonRow[];
  best_algorithm: AlgorithmType;
}

export interface TrainResponse {
  model_type: ModelType;
  n_samples: number;
  metrics: ModelMetrics;
  trained_at: string;
}

export interface PredictResponse {
  predicted_success: number;
  explanation: FeatureContribution[];
}

export interface GenerateDataResponse {
  n_technicians: number;
  n_requests: number;
  n_assignments: number;
  generated_at: string;
}
