import { Navigate, Route, Routes } from 'react-router-dom';

import Layout from './components/layout/Layout';
import AllocationPage from './pages/AllocationPage';
import ComparisonPage from './pages/ComparisonPage';
import DashboardPage from './pages/DashboardPage';
import ExplainabilityPage from './pages/ExplainabilityPage';
import ModelsPage from './pages/ModelsPage';
import { AppProvider } from './store/appStore';

export default function App() {
  return (
    <AppProvider>
      <Layout>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/allocation" element={<AllocationPage />} />
          <Route path="/models" element={<ModelsPage />} />
          <Route path="/comparison" element={<ComparisonPage />} />
          <Route path="/explainability" element={<ExplainabilityPage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </AppProvider>
  );
}
