import kfp
import kfp.compiler


@kfp.dsl.component
def training(epochs: int, n_layers):
    ...
    return kfp.dsl.ContainerOp(
        name="Trianing",
        image="docker.io/cgarciae/test-pipeline:latest",
        command=[
            "python",
            "-m",
            "training.main",
            "--epochs",
            f"{epochs}",
            "--n-layers",
            f"{n_layers}",
        ],
        file_outputs={
            "mlpipeline-metrics": "/mlpipeline-metrics.json",
            "mlpipeline-ui-metadata": "/mlpipeline-ui-metadata.json",
        },
        output_artifact_paths={
            "mlpipeline-metrics": "/mlpipeline-metrics.json",
            "mlpipeline-ui-metadata": "/mlpipeline-ui-metadata.json",
        },
    )


@kfp.dsl.pipeline(name="test-pipeline", description="....")
def pipeline(epochs: int = 10, n_layers: int = 6):
    training_step = training(
        epochs=epochs,
        n_layers=n_layers,
    )


kfp.compiler.Compiler().compile(pipeline, "pipeline.yml")
