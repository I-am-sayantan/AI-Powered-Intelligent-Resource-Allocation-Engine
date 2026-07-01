import ConfusionMatrix from '../charts/ConfusionMatrix';
import MetricsChart from '../charts/MetricsChart';
import Button from '../components/common/Button';
import Card from '../components/common/Card';
import Spinner from '../components/common/Spinner';
import { useMetrics, useTrainModel } from '../hooks/useApi';
import { useAppStore } from '../store/appStore';
import type { ModelType } from '../types';
import { formatNumber, modelLabels } from '../utils/format';

const models: ModelType[] = ['random_forest', 'xgboost', 'lightgbm', 'catboost', 'ffnn', 'tabnet'];

export default function ModelsPage() {
  const { modelType, setModelType } = useAppStore();
  const train = useTrainModel();
  const metrics = useMetrics();

  const modelMetrics = train.data?.metrics ?? metrics.data?.model_metrics ?? null;

  return (
    <div className="space-y-6">
      <Card title="Train Model" subtitle="Train a classifier to predict assignment success">
        <div className="flex flex-wrap items-center gap-2">
          {models.map((option) => (
            <Button
              key={option}
              variant={option === modelType ? 'primary' : 'secondary'}
              onClick={() => setModelType(option)}
            >
              {modelLabels[option]}
            </Button>
          ))}
          <Button onClick={() => train.mutate(modelType)} disabled={train.isPending}>
            {train.isPending ? 'Training…' : 'Train'}
          </Button>
        </div>
        {train.data && (
          <p className="mt-3 text-sm text-slate-500">
            Trained {modelLabels[train.data.model_type]} on {formatNumber(train.data.n_samples)}{' '}
            samples.
          </p>
        )}
      </Card>

      <div className="grid gap-6 lg:grid-cols-2">
        <Card title="Classification Metrics" subtitle="Accuracy, precision, recall, F1, ROC-AUC">
          {modelMetrics ? <MetricsChart metrics={modelMetrics} /> : <Spinner />}
        </Card>
        <Card title="Confusion Matrix">
          {modelMetrics ? <ConfusionMatrix matrix={modelMetrics.confusion_matrix} /> : <Spinner />}
        </Card>
      </div>
    </div>
  );
}
