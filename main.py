#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py

Main script for generating Work Breakdown Structure (WBS) and
Responsibility Assignment Matrix (RAM) diagrams from YAML configuration.

Author: Brighton Sikarskie
Date: 2025-01-29
"""

import logging
import sys
from pm_matrix_builder import create_wbs_and_ram

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    # Use command line argument if provided, otherwise use default
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else "wbs_structure.yaml"
    
    try:
        create_wbs_and_ram(yaml_file)
        logger.info("Successfully generated WBS and RAM diagrams")
        logger.info(f"- WBS diagram saved as: wbs_output.pdf")
        logger.info(f"- RAM diagram saved as: ram_output.pdf")
    except Exception as e:
        logger.error(f"Error generating diagrams: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

