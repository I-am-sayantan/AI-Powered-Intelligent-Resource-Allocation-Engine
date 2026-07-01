import FeatureImportanceChart from '../charts/FeatureImportanceChart';
import Button from '../components/common/Button';
import Card from '../components/common/Card';
import Spinner from '../components/common/Spinner';
import ExplanationPanel from '../components/explain/ExplanationPanel';
import { useMetrics, usePredict } from '../hooks/useApi';

export default function ExplainabilityPage() {
  const metrics = useMetrics();
  const predict = usePredict();
  const explanation = predict.data;

  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <Card
        title="Global Feature Importance"
        subtitle="Across the 13 engineered features"
      >
        {metrics.data ? (
          <FeatureImportanceChart items={metrics.data.feature_importance} />
        ) : (
          <Spinner />
        )}
      </Card>

      <Card
        title="Assignment Explanation"
        subtitle="SHAP-style local contributions"
        actions={
          <Button variant="secondary" onClick={() => predict.mutate({})} disabled={predict.isPending}>
            {predict.isPending ? 'Explaining…' : 'Explain sample'}
          </Button>
        }
      >
        {explanation ? (
          <ExplanationPanel
            score={explanation.predicted_success}
            contributions={explanation.explanation}
          />
        ) : (
          <p className="text-sm text-slate-400">
            Click &ldquo;Explain sample&rdquo; to generate an explanation.
          </p>
        )}
      </Card>
    </div>
  );
}
