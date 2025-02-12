#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
block_diagram_builder.py

Module for generating functional block diagrams using graphviz.

Author: Brighton Sikarskie
Date: 2024-02-10
"""

import graphviz
import yaml
import logging

logger = logging.getLogger(__name__)

def create_block_diagram(yaml_file, output_file="block_diagram"):
    """
    Create a functional block diagram from YAML configuration.
    
    Args:
        yaml_file (str): Path to YAML file containing block diagram configuration
        output_file (str): Name of the output file (without extension)
    """
    try:
        # Create a new directed graph
        dot = graphviz.Digraph(comment='Functional Block Diagram')
        dot.attr(rankdir='LR')  # Left to right layout
        
        # Load block diagram configuration from YAML
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
            
        # Set global graph attributes
        dot.attr('graph', 
                splines='ortho',    # Orthogonal lines
                nodesep='0.75',     # Space between nodes
                ranksep='0.75',     # Space between ranks
                pad='0.5',          # Padding around the graph
                bgcolor='lightblue:white')  # Gradient background
                
        # Add title
        dot.attr(label=config['title'] + '\n' + config['description'], 
                labelloc='t',
                fontsize='24',
                fontname='Times-Roman')

        # Create main unit subgraph
        with dot.subgraph(name='cluster_main') as main:
            main.attr(label='Main Unit', style='rounded', color='black', penwidth='2.0')
            
            # Power section
            with main.subgraph(name='cluster_power') as power:
                power.attr(label='Power Management', style='rounded', color='darkred')
                power.node('main_battery', config['blocks'][0]['name'],
                          shape='box', style='filled', fillcolor='#ff4444',
                          color='black', height='0.6', width='1.5')
                power.node('main_power_mgmt', config['blocks'][1]['name'],
                          shape='box', style='filled', fillcolor='#ff4444',
                          color='black', height='0.6', width='1.8')
                power.node('main_voltage_reg', config['blocks'][2]['name'],
                          shape='box', style='filled', fillcolor='#ff4444',
                          color='black', height='0.6', width='1.5')
            
            # Control section
            with main.subgraph(name='cluster_control') as control:
                control.attr(label='Control System', style='rounded', color='darkblue')
                control.node('main_mcu', config['blocks'][3]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.8', width='1.8')
                control.node('motor_driver', config['blocks'][4]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.6', width='1.5')
                control.node('motor', config['blocks'][5]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.6', width='1.5')
            
            # Sensors section
            with main.subgraph(name='cluster_sensors') as sensors:
                sensors.attr(label='Sensors', style='rounded', color='darkgreen')
                sensors.node('phone_mount', config['blocks'][6]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.6', width='1.5')
                sensors.node('angle_sensor', config['blocks'][7]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.6', width='1.5')
                sensors.node('main_status_led', config['blocks'][8]['name'],
                           shape='box', style='filled', fillcolor='#ff4444',
                           color='black', height='0.6', width='1.5')

        # Create remote unit subgraph
        with dot.subgraph(name='cluster_remote') as remote:
            remote.attr(label='Remote Unit', style='rounded', color='black', penwidth='2.0')
            
            # Remote power section
            with remote.subgraph(name='cluster_remote_power') as remote_power:
                remote_power.attr(label='Power Management', style='rounded', color='darkred')
                remote_power.node('remote_battery', config['blocks'][9]['name'],
                                shape='box', style='filled', fillcolor='#ff4444',
                                color='black', height='0.6', width='1.5')
                remote_power.node('remote_reg', config['blocks'][10]['name'],
                                shape='box', style='filled', fillcolor='#ff4444',
                                color='black', height='0.6', width='1.5')
            
            # Remote control section
            with remote.subgraph(name='cluster_remote_control') as remote_control:
                remote_control.attr(label='Control System', style='rounded', color='darkblue')
                remote_control.node('remote_mcu', config['blocks'][11]['name'],
                                  shape='box', style='filled', fillcolor='#ff4444',
                                  color='black', height='0.8', width='1.8')
                remote_control.node('control_buttons', config['blocks'][12]['name'],
                                  shape='box', style='filled', fillcolor='#ff4444',
                                  color='black', height='0.6', width='1.5')
                remote_control.node('remote_status_led', config['blocks'][13]['name'],
                                  shape='box', style='filled', fillcolor='#ff4444',
                                  color='black', height='0.6', width='1.5')

        # Add connections
        for connection in config.get('connections', []):
            if connection.get('style') == 'dashed':
                dot.edge(connection['from'], connection['to'],
                        xlabel=connection.get('label', ''),
                        fontsize='10',
                        penwidth='1.2',
                        style='dashed',
                        constraint='false')  # Allow crossing ranks for BLE
            else:
                dot.edge(connection['from'], connection['to'],
                        xlabel=connection.get('label', ''),
                        fontsize='10',
                        penwidth='1.2')

        # Save the diagram
        dot.render(output_file, format='pdf', cleanup=True)
        dot.render(output_file, format='png', cleanup=True)
        
        logger.info(f"Successfully generated block diagram: {output_file}")
        
    except Exception as e:
        logger.error(f"Error generating block diagram: {e}")
        raise 