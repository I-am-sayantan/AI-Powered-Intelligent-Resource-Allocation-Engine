/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useMemo, useState } from 'react';
import type { ReactNode } from 'react';

import type { AlgorithmType, ModelType } from '../types';

interface AppState {
  algorithm: AlgorithmType;
  setAlgorithm: (algorithm: AlgorithmType) => void;
  modelType: ModelType;
  setModelType: (modelType: ModelType) => void;
}

const AppContext = createContext<AppState | undefined>(undefined);

/** Provides the globally-selected allocation algorithm and model type. */
export function AppProvider({ children }: { children: ReactNode }) {
  const [algorithm, setAlgorithm] = useState<AlgorithmType>('ml');
  const [modelType, setModelType] = useState<ModelType>('xgboost');

  const value = useMemo<AppState>(
    () => ({ algorithm, setAlgorithm, modelType, setModelType }),
    [algorithm, modelType],
  );

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useAppStore(): AppState {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppStore must be used within an AppProvider');
  }
  return context;
}
