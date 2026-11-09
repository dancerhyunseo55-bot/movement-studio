
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

st.set_page_config(
    page_title="Movement Studio",
    page_icon="🎨",
    layout="centered"
)

st.title("Movement Studio")
st.write("Create abstract art inspired by dance and movement.")

palette = st.selectbox(
    "Color Palette",
    ["Pastel", "Vivid", "Monochrome"]
)

movement = st.slider(
    "Movement Intensity", 1, 10, 5
)

shapes = st.slider(
    "Number of Shapes", 3, 25, 12
)

seed = st.number_input(
    "Design Number", min_value=0, value=42
)

colors = {
    "Pastel": ["#E8B4BC", "#B8C9E8", "#C4DFCC", "#EED6A7"],
    "Vivid": ["#EF476F", "#06D6A0", "#118AB2", "#FFD166"],
    "Monochrome": ["#222222", "#555555", "#888888", "#BBBBBB"]
}

def make_art():
    rng = np.random.default_rng(seed)

    fig, ax = plt.subplots(figsize=(6, 8))
    fig.patch.set_facecolor("#FAF8F4")
    ax.set_facecolor("#FAF8F4")

    t = np.linspace(0, 2 * np.pi, 300)

    for i in range(shapes):
        x = rng.uniform(0.1, 0.9)
        y = rng.uniform(0.1, 0.9)
        radius = rng.uniform(0.04, 0.16)

        wobble = movement * 0.025
        wave = radius * (
            1 + wobble * np.sin(5 * t + i)
        )

        px = x + wave * np.cos(t)
        py = y + wave * np.sin(t)

        color = colors[palette][
            i % len(colors[palette])
        ]

        ax.fill(
            px, py,
            color=color,
            alpha=0.65,
            edgecolor="white",
            linewidth=1.5
        )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    return fig

fig = make_art()
st.pyplot(fig)

buffer = BytesIO()
fig.savefig(
    buffer,
    format="png",
    dpi=200,
    bbox_inches="tight"
)

st.download_button(
    "Download Your Artwork",
    data=buffer.getvalue(),
    file_name="movement_studio.png",
    mime="image/png"
)

plt.close(fig)
