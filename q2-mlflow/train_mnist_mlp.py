import mlflow
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mnist-mlp-q2")

print("Loading MNIST (this can take a minute the first time)...")
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
y = y.astype(int)

X, _, y, _ = train_test_split(
    X, y, train_size=10000, stratify=y, random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

N_EPOCHS = 15
CLASSES = np.unique(y_train)

learning_rates = [0.1, 0.01, 0.001]
batch_sizes = [32, 128]

for lr in learning_rates:
    for bs in batch_sizes:

        run_name = f"mlp-lr{lr}-bs{bs}"

        with mlflow.start_run(run_name=run_name):

            mlflow.log_param("model_type", "MLPClassifier")
            mlflow.log_param("dataset", "MNIST")
            mlflow.log_param("learning_rate_init", lr)
            mlflow.log_param("batch_size", bs)
            mlflow.log_param("hidden_layer_sizes", "(100,)")
            mlflow.log_param("n_epochs", N_EPOCHS)

            model = MLPClassifier(
                hidden_layer_sizes=(100,),
                learning_rate_init=lr,
                batch_size=bs,
                max_iter=1,
                warm_start=True,
                random_state=42,
            )

            for epoch in range(N_EPOCHS):
                model.partial_fit(
                    X_train,
                    y_train,
                    classes=CLASSES
                )

                train_loss = model.loss_
                val_accuracy = model.score(X_val, y_val)

                mlflow.log_metric(
                    "train_loss",
                    train_loss,
                    step=epoch
                )

                mlflow.log_metric(
                    "val_accuracy",
                    val_accuracy,
                    step=epoch
                )

            final_train_acc = model.score(X_train, y_train)

            mlflow.log_metric(
                "final_train_accuracy",
                final_train_acc
            )

            mlflow.log_metric(
                "final_val_accuracy",
                val_accuracy
            )

            print(
                f"{run_name}: final val_accuracy = {val_accuracy:.4f}"
            )

print("\nAll 6 runs complete. Open http://localhost:5000 to compare them.")