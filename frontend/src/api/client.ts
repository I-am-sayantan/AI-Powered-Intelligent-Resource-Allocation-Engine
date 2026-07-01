import axios from 'axios';

/** Base URL of the FastAPI backend (override with VITE_API_BASE_URL). */
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000';

/** Shared Axios instance for all API calls. */
export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});
