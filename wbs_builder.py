#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wbs_builder.py

Revised module for creating colorized Work Breakdown Structure (WBS) diagrams
using Graphviz, ensuring clusters are labeled once (avoiding repeated text).

Author: Brighton Sikarskie
Date: 2025-01-29
"""

import logging
import re
from graphviz import Digraph

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
if not logger.handlers:
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def _safe_cluster_name(label: str) -> str:
    """
    Convert a label into a safe subgraph name (no spaces, punctuation).
    Example: 'Project A (1.1)' -> 'cluster_Project_A__1_1_'
    """
    return "cluster_" + re.sub(r"[^a-zA-Z0-9_]", "_", label)

def _cluster_style_for(label: str) -> dict:
    """
    Returns style dict for a cluster (bounding box) depending on the label.
    """
    return {
        "style": "invis",  # Make cluster borders invisible
        "margin": "8"
    }

def _node_style_for(label: str, level: int = 0, colors: dict = None) -> dict:
    """
    Returns style dict for a node.
    level: 0 for root, 1 for first level, 2 for second level, 3+ for deeper levels
    colors: Optional dictionary mapping levels to colors
    """
    if colors is None:
        colors = {0: "#fbf1c7"}  # Default to Gruvbox light0

    # Adjust size based on level
    sizes = {
        0: ("0.5", "0.3"),  # (width, height) for root
        1: ("0.45", "0.3"),
        2: ("0.4", "0.25"),
        3: ("0.35", "0.25"),
        4: ("0.3", "0.2"),
        5: ("0.25", "0.2"),
        6: ("0.2", "0.15"),
        7: ("0.15", "0.15")
    }
    width, height = sizes.get(level, ("0.15", "0.15"))
    
    # Adjust font size based on level
    font_sizes = {
        0: "12",
        1: "11",
        2: "10",
        3: "9",
        4: "8",
        5: "8",
        6: "7",
        7: "7"
    }

    base_style = {
        "shape": "box",
        "style": "filled",
        "color": "#3c3836",  # Gruvbox dark0
        "fillcolor": colors.get(level % len(colors), "#fbf1c7"),
        "fontcolor": "#282828",  # Gruvbox dark
        "fontname": "Arial",
        "fontsize": font_sizes.get(level, "7"),
        "height": height,
        "width": width,
        "margin": "0.05",
        "penwidth": "1.0"
    }

    return base_style

def create_wbs_diagram(
    wbs_structure: dict,
    output_filename: str = "wbs_output",
    file_format: str = "pdf",
    graph_direction: str = "TB",
    colors: dict = None
) -> None:
    """
    Create and save a WBS diagram with proper styling and layout.
    """
    logger.info("Creating WBS diagram...")
    try:
        dot = Digraph(comment="Work Breakdown Structure")
        dot.attr(
            rankdir=graph_direction,
            splines="line",
            nodesep="0.2",      # Reduced for compactness
            ranksep="0.25",     # Reduced for compactness
            pad="0.2",
            concentrate="true",  # Help reduce edge crossings
            compound="true",
            newrank="true",
            bgcolor="#f9f5d7"   # Gruvbox light background
        )

        def add_nodes_and_edges(items, parent_node=None, level=0, parent_number=""):
            """
            Recursively add nodes and edges to the graph.
            """
            nodes = []
            
            if isinstance(items, dict):
                # Handle the root level
                for label, children in items.items():
                    node_id = re.sub(r"[^a-zA-Z0-9_]", "_", label)
                    node_style = _node_style_for(label, level, colors)
                    dot.node(node_id, label, **node_style)
                    add_nodes_and_edges(children, node_id, level + 1)
            else:
                # Handle list of tuples for other levels
                for idx, (label, children) in enumerate(items, 1):
                    # Generate node number based on level and position
                    if level == 1:
                        node_number = f"{idx}.0"
                    elif level > 1:
                        if parent_number:
                            if parent_number.endswith('.0'):
                                # Remove the .0 for cleaner numbering
                                parent_base = parent_number[:-2]
                                node_number = f"{parent_base}.{idx}"
                            else:
                                node_number = f"{parent_number}.{idx}"
                        else:
                            node_number = str(idx)
                    else:
                        node_number = ""

                    # Format the display label with the WBS number
                    if level > 0:  # Don't add number to root level
                        display_label = f"{label} ({node_number})"
                    else:
                        display_label = label
                    
                    # Create unique node ID
                    node_id = re.sub(r"[^a-zA-Z0-9_]", "_", f"{label}_{node_number}")
                    
                    # Add the node
                    node_style = _node_style_for(display_label, level, colors)
                    dot.node(node_id, display_label, **node_style)
                    nodes.append(node_id)
                    
                    if parent_node:
                        dot.edge(parent_node, node_id,
                               color="#3c3836",  # Gruvbox dark0
                               arrowsize="0.6",
                               penwidth="1.0")
                    
                    if children:
                        add_nodes_and_edges(children, node_id, level + 1, node_number)
            
            return nodes

        # Start with top-level items
        for top_label, top_structure in wbs_structure.items():
            top_node_id = re.sub(r"[^a-zA-Z0-9_]", "_", top_label)
            dot.node(top_node_id, top_label, **_node_style_for(top_label, 0, colors))
            add_nodes_and_edges(top_structure, top_node_id, 1)

        # Render the final diagram
        output_path = dot.render(filename=output_filename, format=file_format, cleanup=True)
        logger.info(f"WBS diagram saved to: {output_path}")

    except Exception as e:
        logger.error("Error while creating WBS diagram:", exc_info=True)
        raise

