#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py

Demonstration script that uses the revised wbs_builder module
to produce colorized WBS diagrams without repeated labels.

Author: Brighton Sikarskie
Date: 2025-01-28
"""

import logging
import wbs_builder

# Configure application-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Ensure there is a console handler for the main script
if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def main():
    logger.info("Starting WBS diagram generation...")

    # Define Gruvbox theme colors for each level - using more distinct colors
    colors = {
        0: "#fbf1c7",  # Light0
        1: "#d3869b",  # Purple
        2: "#8ec07c",  # Green
        3: "#fe8019",  # Orange
        4: "#83a598",  # Blue
        5: "#b8bb26",  # Yellow
        6: "#fb4934",  # Red
        7: "#fabd2f"   # Bright Yellow
    }

    # Define the WBS structure with empty strings - numbers will be assigned automatically
    wbs_data = {
        "SelfiePod": [
            ("Market Analysis", [
                ("Materials Research", [
                    ("Battery Research", [
                        ("Battery Types", [
                            ("Lithium Ion", [
                                ("Cell Chemistry", [
                                    ("Cathode Materials", []),
                                    ("Anode Materials", []),
                                    ("Electrolyte Composition", [])
                                ]),
                                ("Form Factor", [
                                    ("Cylindrical", []),
                                    ("Prismatic", []),
                                    ("Pouch", [])
                                ])
                            ]),
                            ("LiFePO4", [
                                ("Safety Features", [
                                    ("Thermal Management", []),
                                    ("Overcharge Protection", []),
                                    ("Short Circuit Prevention", [])
                                ])
                            ])
                        ]),
                        ("Battery Capacity", []),
                        ("Battery Safety", []),
                        ("Battery Suppliers", [])
                    ]),
                    ("Plastic Research", [
                        ("Plastic Types", [
                            ("ABS Analysis", [
                                ("Impact Resistance", []),
                                ("Heat Resistance", []),
                                ("Cost Analysis", [])
                            ]),
                            ("Polycarbonate Study", [
                                ("Durability Tests", []),
                                ("UV Resistance", []),
                                ("Manufacturing Process", [])
                            ])
                        ])
                    ])
                ]),
                ("User Needs Analysis", [
                    ("Target Audience Research", [
                        ("Demographics", []),
                        ("Usage Patterns", []),
                        ("Purchase Behavior", [])
                    ]),
                    ("User Pain Points", [
                        ("Current Solutions", []),
                        ("Unmet Needs", []),
                        ("Feature Requests", [])
                    ])
                ])
            ]),
            ("Design", [
                ("Brainstorming", [
                    ("Initial Concepts", [
                        ("Design Sketches", []),
                        ("3D Models", []),
                        ("Prototype Ideas", [])
                    ])
                ]),
                ("Battery & Charging", [
                    ("Battery Selection", [
                        ("Capacity Requirements", []),
                        ("Size Constraints", []),
                        ("Temperature Management", [])
                    ]),
                    ("Charging Circuit", [
                        ("Circuit Layout", []),
                        ("Component Selection", []),
                        ("Safety Features", [])
                    ])
                ]),
                ("Electronics Design", [
                    ("Circuit Design", [
                        ("Power Management", [
                            ("Voltage Regulation", [
                                ("Buck Converter", [
                                    ("Component Selection", []),
                                    ("Efficiency Analysis", []),
                                    ("Thermal Design", [])
                                ]),
                                ("Battery Protection", [
                                    ("Overcurrent", []),
                                    ("Overvoltage", []),
                                    ("Temperature", [])
                                ])
                            ]),
                            ("Power Distribution", [
                                ("PCB Layout", [
                                    ("Component Placement", []),
                                    ("Trace Routing", []),
                                    ("Ground Plane", [])
                                ])
                            ])
                        ]),
                        ("Microcontroller Integration", [
                            ("Firmware Architecture", [
                                ("Power States", []),
                                ("Communication Protocol", []),
                                ("Error Handling", [])
                            ])
                        ])
                    ])
                ])
            ]),
            ("Build", [
                ("Component Sourcing", [
                    ("Battery Procurement", [
                        ("Supplier Selection", []),
                        ("Quality Verification", []),
                        ("Cost Negotiation", [])
                    ]),
                    ("Electronics Components", [
                        ("Component List", []),
                        ("Supplier Quotes", []),
                        ("Lead Time Analysis", [])
                    ])
                ]),
                ("Prototype Development", [
                    ("Initial Prototype", [
                        ("3D Printing", []),
                        ("Assembly", []),
                        ("Testing", [])
                    ]),
                    ("Final Prototype", [
                        ("Production Methods", []),
                        ("Quality Control", []),
                        ("Documentation", [])
                    ])
                ])
            ]),
            ("Testing", [
                ("Quality Assurance", [
                    ("Component Testing", [
                        ("Electrical Testing", [
                            ("Power System", [
                                ("Battery Performance", [
                                    ("Charge Cycles", []),
                                    ("Voltage Stability", []),
                                    ("Temperature Profile", [])
                                ]),
                                ("Circuit Validation", [
                                    ("Signal Integrity", []),
                                    ("EMI Testing", []),
                                    ("Power Efficiency", [])
                                ])
                            ]),
                            ("Control System", [
                                ("MCU Validation", [
                                    ("Clock Stability", []),
                                    ("Memory Tests", []),
                                    ("Peripheral Tests", [])
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            ("Marketing", [
                ("Digital Marketing", [
                    ("Social Media", [
                        ("Platform Strategy", [
                            ("Instagram Campaign", [
                                ("Content Creation", [
                                    ("Photo Shoots", []),
                                    ("Video Production", []),
                                    ("Story Templates", [])
                                ]),
                                ("Influencer Program", [
                                    ("Selection Criteria", []),
                                    ("Engagement Metrics", []),
                                    ("ROI Analysis", [])
                                ])
                            ]),
                            ("TikTok Strategy", [
                                ("Trend Analysis", []),
                                ("Content Calendar", []),
                                ("Performance Metrics", [])
                            ])
                        ])
                    ])
                ])
            ]),
            ("Production & Deployment", [
                ("Manufacturing Setup", [
                    ("Assembly Line Design", [
                        ("Automation Systems", [
                            ("Robot Integration", [
                                ("End Effector Design", [
                                    ("Gripper Mechanism", []),
                                    ("Sensor Integration", []),
                                    ("Control Software", [])
                                ]),
                                ("Motion Planning", [
                                    ("Path Optimization", []),
                                    ("Collision Avoidance", []),
                                    ("Speed Control", [])
                                ])
                            ]),
                            ("Vision System", [
                                ("Camera Setup", [
                                    ("Lighting Design", []),
                                    ("Image Processing", []),
                                    ("Quality Checks", [])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ]
    }

    wbs_builder.create_wbs_diagram(
        wbs_structure=wbs_data,
        output_filename="wbs_diagram",
        file_format="pdf",
        graph_direction="TB",
        colors=colors
    )

    logger.info("WBS diagram generation complete.")

if __name__ == "__main__":
    main()

