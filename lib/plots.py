"""Reusable plotting utilities for music visualization."""

from typing import Callable, Optional
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from ipywidgets import FloatSlider

# Chart styling constants
DEFAULT_LINE_COLOR = '#2E86AB'
DEFAULT_LINE_WIDTH = 1.5
DEFAULT_FIGURE_SIZE = (10, 4)
DEFAULT_GRID_ALPHA = 0.3


def create_line_chart(
    x: np.ndarray,
    y: np.ndarray,
    xlabel: str,
    ylabel: str,
    title: str,
    ylim: Optional[tuple[float, float]] = None,
    show_zero_line: bool = True,
    color: str = DEFAULT_LINE_COLOR,
    figsize: tuple[int, int] = DEFAULT_FIGURE_SIZE,
) -> tuple[Figure, Axes]:
    """
    Create a styled 2D line chart.
    
    Args:
        x: X-axis data
        y: Y-axis data
        xlabel: Label for X-axis
        ylabel: Label for Y-axis
        title: Chart title
        ylim: Optional (min, max) tuple for Y-axis limits
        show_zero_line: Whether to show a horizontal line at y=0
        color: Line color
        figsize: Figure size as (width, height)
    
    Returns:
        Tuple of (Figure, Axes) for further customization if needed
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, y, color=color, linewidth=DEFAULT_LINE_WIDTH)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    if ylim:
        ax.set_ylim(ylim)
    
    ax.grid(True, alpha=DEFAULT_GRID_ALPHA)
    
    if show_zero_line:
        ax.axhline(y=0, color='black', linewidth=0.5)
    
    plt.tight_layout()
    return fig, ax


def create_interactive_plot(
    plot_fn: Callable[..., None],
    sliders: list[FloatSlider],
    slider_names: list[str],
) -> None:
    """
    Create an interactive plot with sliders that updates without flashing.
    
    Args:
        plot_fn: Function that takes slider values and plots to the output widget
        sliders: List of FloatSlider widgets
        slider_names: List of parameter names corresponding to each slider
    """
    from ipywidgets import interact
    
    # Close any existing figures from previous runs
    plt.close('all')
    
    # Set continuous_update=False to only update on slider release (reduces flicker)
    for slider in sliders:
        slider.continuous_update = False
    
    def wrapped_plot_fn(**kwargs):
        plt.close('all')
        plot_fn(**kwargs)
        plt.show()
    
    # Build kwargs dict mapping slider names to slider widgets
    interact_kwargs = {name: slider for name, slider in zip(slider_names, sliders)}
    interact(wrapped_plot_fn, **interact_kwargs)

