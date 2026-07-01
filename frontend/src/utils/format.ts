import type { AlgorithmType, ModelType } from '../types';

export const formatPercent = (value: number, digits = 0): string =>
  `${(value * 100).toFixed(digits)}%`;

export const formatKm = (value: number): string => `${value.toFixed(1)} km`;

export const formatMs = (value: number): string => `${value.toFixed(1)} ms`;

export const formatNumber = (value: number): string => value.toLocaleString();

export const algorithmLabels: Record<AlgorithmType, string> = {
  greedy: 'Greedy',
  hungarian: 'Hungarian',
  ml: 'Machine Learning',
  dl: 'Deep Learning',
};

export const modelLabels: Record<ModelType, string> = {
  random_forest: 'Random Forest',
  xgboost: 'XGBoost',
  lightgbm: 'LightGBM',
  catboost: 'CatBoost',
  ffnn: 'Feed-Forward NN',
  tabnet: 'TabNet',
};
