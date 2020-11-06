import matplotlib.pyplot as plt
import base64
from io import BytesIO


def fig_to_html(fig: plt.Figure) -> str:
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format="png")
    encoded = base64.b64encode(tmpfile.getvalue()).decode("utf-8")

    return f"<img src='data:image/png;base64,{encoded}'>"
