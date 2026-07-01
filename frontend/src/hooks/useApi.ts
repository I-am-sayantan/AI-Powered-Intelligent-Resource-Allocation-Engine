import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

import type { GenerateDataPayload, PredictPayload } from '../api/endpoints';
import { api } from '../api/endpoints';
import type { AlgorithmType, ModelType } from '../types';

export const queryKeys = {
  technicians: ['technicians'] as const,
  requests: ['requests'] as const,
  assignments: ['assignments'] as const,
  metrics: ['metrics'] as const,
};

export function useTechnicians() {
  return useQuery({ queryKey: queryKeys.technicians, queryFn: api.getTechnicians });
}

export function useRequests() {
  return useQuery({ queryKey: queryKeys.requests, queryFn: api.getRequests });
}

export function useAssignments() {
  return useQuery({ queryKey: queryKeys.assignments, queryFn: api.getAssignments });
}

export function useMetrics() {
  return useQuery({ queryKey: queryKeys.metrics, queryFn: api.getMetrics });
}

export function useGenerateData() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (payload: GenerateDataPayload) => api.generateData(payload),
    onSuccess: () => queryClient.invalidateQueries(),
  });
}

export function useAllocate() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (algorithm: AlgorithmType) => api.allocate(algorithm),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.assignments });
      queryClient.invalidateQueries({ queryKey: queryKeys.metrics });
    },
  });
}

export function useCompare() {
  return useMutation({ mutationFn: () => api.compare() });
}

export function useTrainModel() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (modelType: ModelType) => api.trainModel(modelType),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: queryKeys.metrics }),
  });
}

export function usePredict() {
  return useMutation({ mutationFn: (payload: PredictPayload) => api.predict(payload) });
}
