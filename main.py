#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py

Main script for generating Work Breakdown Structure (WBS),
Responsibility Assignment Matrix (RAM), and Block Diagrams from YAML configuration.

Author: Brighton Sikarskie
Date: 2024-02-10
"""

import logging
import sys
import argparse
from pm_matrix_builder import create_wbs_and_ram
from block_diagram_builder import create_block_diagram

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Generate project management diagrams.')
    parser.add_argument('--wbs', action='store_true', help='Generate WBS diagram')
    parser.add_argument('--ram', action='store_true', help='Generate RAM diagram')
    parser.add_argument('--block', action='store_true', help='Generate block diagram')
    parser.add_argument('--wbs-yaml', default='wbs_structure.yaml', help='WBS YAML file (default: wbs_structure.yaml)')
    parser.add_argument('--block-yaml', default='block_diagram.yaml', help='Block diagram YAML file (default: block_diagram.yaml)')
    
    args = parser.parse_args()
    
    # If no specific diagrams are requested, generate all
    if not (args.wbs or args.ram or args.block):
        args.wbs = args.ram = args.block = True
    
    try:
        if args.wbs or args.ram:
            create_wbs_and_ram(args.wbs_yaml)
            logger.info("Successfully generated WBS and RAM diagrams")
            logger.info(f"- WBS diagram saved as: wbs_output.pdf")
            logger.info(f"- RAM diagram saved as: ram_output.pdf")
        
        if args.block:
            create_block_diagram(args.block_yaml)
            logger.info("Successfully generated block diagram")
            logger.info(f"- Block diagram saved as: block_diagram.pdf")
            
    except Exception as e:
        logger.error(f"Error generating diagrams: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

