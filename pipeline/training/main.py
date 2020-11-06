import json
import os
from pathlib import Path

import numpy as np
import typer
from matplotlib import pyplot as plt
from tensorflow.python.lib.io import file_io

from . import utils

ROOT = Path(os.environ.get("ROOT", "/"))


def main(epochs: int = typer.Option(...), n_layers: int = 6):
    print(f"Epochs: {epochs}")
    print(f"Number of layers: {n_layers}")

    x = np.linspace(-5, 5)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x, y)

    metadata = {
        "outputs": [
            {
                "type": "web-app",
                "storage": "inline",
                "source": utils.fig_to_html(fig),
            },
        ]
    }

    with file_io.FileIO(str(ROOT / "mlpipeline-ui-metadata.json"), "w") as f:
        json.dump(metadata, f)


if __name__ == "__main__":
    typer.run(main)
