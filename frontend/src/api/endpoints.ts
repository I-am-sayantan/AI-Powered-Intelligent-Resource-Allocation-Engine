import type {
  AlgorithmType,
  AllocationResult,
  Assignment,
  CompareResult,
  GenerateDataResponse,
  MetricsResponse,
  ModelType,
  PredictResponse,
  ServiceRequest,
  Technician,
  TrainResponse,
} from '../types';

import { apiClient } from './client';

export interface GenerateDataPayload {
  n_technicians?: number;
  n_requests?: number;
  n_assignments?: number;
  seed?: number;
}

export interface PredictPayload {
  technician_id?: string;
  request_id?: string;
  features?: Record<string, number>;
}

/** Typed wrappers around every backend endpoint. */
export const api = {
  generateData: async (payload: GenerateDataPayload = {}): Promise<GenerateDataResponse> =>
    (await apiClient.post<GenerateDataResponse>('/generate-data', payload)).data,

  getTechnicians: async (): Promise<Technician[]> =>
    (await apiClient.get<Technician[]>('/technicians')).data,

  getRequests: async (): Promise<ServiceRequest[]> =>
    (await apiClient.get<ServiceRequest[]>('/requests')).data,

  getAssignments: async (): Promise<Assignment[]> =>
    (await apiClient.get<Assignment[]>('/assignments')).data,

  getMetrics: async (): Promise<MetricsResponse> =>
    (await apiClient.get<MetricsResponse>('/metrics')).data,

  trainModel: async (modelType: ModelType): Promise<TrainResponse> =>
    (await apiClient.post<TrainResponse>('/train-model', { model_type: modelType })).data,

  predict: async (payload: PredictPayload = {}): Promise<PredictResponse> =>
    (await apiClient.post<PredictResponse>('/predict', payload)).data,

  allocate: async (algorithm: AlgorithmType): Promise<AllocationResult> =>
    (await apiClient.post<AllocationResult>('/allocate', { algorithm })).data,

  compare: async (): Promise<CompareResult> =>
    (await apiClient.post<CompareResult>('/compare', {})).data,
};
