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
    level: 0 for root, 1 for first level, 2 for second level, 3 for leaves
    colors: Optional dictionary mapping levels to colors
    """
    if colors is None:
        colors = {
            0: "#FF9999",  # Light red for root
            1: "#FFCC99",  # Light orange
            2: "#FFFF99",  # Light yellow
            3: "#99FF99",  # Light green
            4: "#99FFFF",  # Light cyan
            5: "#9999FF",  # Light blue
            6: "#FF99FF"   # Light purple
        }

    base_style = {
        "shape": "box",
        "style": "filled",
        "color": "black",
        "fontcolor": "black",
        "fontname": "Arial",
        "fontsize": "12",
        "height": "0.4",
        "margin": "0.2,0.1",
        "penwidth": "1.5"  # Make borders more visible with colors
    }

    # Width decreases with each level
    widths = {0: "3.0", 1: "2.8", 2: "2.6", 3: "2.5", 4: "2.4", 5: "2.3", 6: "2.2"}
    
    # Get color for this level, cycling through colors if we go deeper than defined colors
    level_color = colors.get(level % len(colors)) if colors else "white"
    
    style = {
        **base_style,
        "fillcolor": level_color,
        "width": widths.get(level, "2.0")
    }

    # Make top two levels bold
    if level <= 1:
        style["style"] = "filled,bold"
    
    return style

def create_wbs_diagram(
    wbs_structure: dict,
    output_filename: str = "wbs_output",
    file_format: str = "pdf",
    graph_direction: str = "LR",
    colors: dict = None
) -> None:
    """
    Create and save a WBS diagram with proper styling and layout.
    """
    logger.info("Creating WBS diagram...")
    try:
        dot = Digraph(comment="Work Breakdown Structure")
        # Adjust graph attributes for compact vertical layout
        dot.attr(
            rankdir=graph_direction,
            splines="ortho",
            nodesep="0.15",   # Vertical spacing between nodes in same rank
            ranksep="0.05",   # Horizontal spacing between ranks
            pad="0.05",
            concentrate="false",
            compound="true",
            newrank="true",
            size="4,13!",     # Swap dimensions for vertical layout
            ratio="fill",
            margin="0.05"
        )

        def add_nodes_and_edges(structure_dict, parent_node=None, level=0):
            """
            Recursively add nodes and edges to the graph.
            """
            nodes = []
            
            # Sort items to help with layout
            items = sorted(structure_dict.items(), key=lambda x: x[0])
            
            for label, children in items:
                # Create unique node ID
                node_id = re.sub(r"[^a-zA-Z0-9_]", "_", label)
                
                # Add the node with level-appropriate styling
                node_style = _node_style_for(label, level, colors)
                # Make nodes very compact
                if level > 0:
                    node_style["width"] = str(float(node_style.get("width", "2.0")) * 0.6)  # Even narrower for vertical
                    node_style["height"] = "0.2"
                    node_style["margin"] = "0.02,0.01"
                    node_style["fontsize"] = "10"
                    if level > 2:
                        node_style["height"] = "0.18"
                        node_style["fontsize"] = "9"
                        node_style["margin"] = "0.01,0.01"
                        node_style["width"] = str(float(node_style.get("width", "2.0")) * 0.9)  # Slightly narrower for deep levels
                
                dot.node(node_id, label, **node_style)
                nodes.append(node_id)
                
                # If there's a parent, add an edge
                if parent_node:
                    dot.edge(parent_node, node_id, 
                           color="black", 
                           penwidth="0.5", 
                           arrowsize="0.3",
                           minlen="1")
                
                # Recurse for children with incremented level
                if children:
                    add_nodes_and_edges(children, node_id, level + 1)
            
            return nodes

        # Start with top-level items (level 0)
        for top_label, top_structure in wbs_structure.items():
            top_node_id = re.sub(r"[^a-zA-Z0-9_]", "_", top_label)
            # Make root node compact
            root_style = _node_style_for(top_label, 0, colors)
            root_style["width"] = "1.2"  # Narrower root for vertical layout
            root_style["height"] = "0.25"
            root_style["margin"] = "0.05,0.02"
            root_style["fontsize"] = "11"
            dot.node(top_node_id, top_label, **root_style)
            add_nodes_and_edges(top_structure, top_node_id, 1)

        # Render the final diagram
        output_path = dot.render(filename=output_filename, format=file_format, cleanup=True)
        logger.info(f"WBS diagram saved to: {output_path}")

    except Exception as e:
        logger.error("Error while creating WBS diagram:", exc_info=True)
        raise

