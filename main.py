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

    # Define rainbow-like colors for each level
    colors = {
        0: "#FF9999",  # Light red for root
        1: "#FFCC99",  # Light orange
        2: "#FFFF99",  # Light yellow
        3: "#99FF99",  # Light green
        4: "#99FFFF",  # Light cyan
        5: "#9999FF",  # Light blue
        6: "#FF99FF"   # Light purple
    }

    # Define the nested dictionary for the WBS
    wbs_data = {
        "SelfiePod": {
            "Market Analysis (1.1)": {
                "Materials Research (1.1.1)": {
                    "Battery Research (1.1.1.1)": {
                        "Battery Types (1.1.1.1.1)": {},
                        "Battery Capacity (1.1.1.1.2)": {},
                        "Battery Safety (1.1.1.1.3)": {},
                        "Battery Suppliers (1.1.1.1.4)": {}
                    },
                    "Plastic Research (1.1.1.2)": {
                        "Plastic Types (1.1.1.2.1)": {},
                        "Durability Tests (1.1.1.2.2)": {},
                        "Cost Analysis (1.1.1.2.3)": {}
                    },
                    "Aluminum Research (1.1.1.3)": {
                        "Alloy Types (1.1.1.3.1)": {},
                        "Weight Analysis (1.1.1.3.2)": {},
                        "Corrosion Resistance (1.1.1.3.3)": {}
                    }
                },
                "User Needs Analysis (1.1.2)": {
                    "Target Audience Research (1.1.2.1)": {
                        "Demographics (1.1.2.1.1)": {},
                        "Usage Patterns (1.1.2.1.2)": {},
                        "Purchase Behavior (1.1.2.1.3)": {}
                    },
                    "User Pain Points (1.1.2.2)": {
                        "Current Solutions (1.1.2.2.1)": {},
                        "Unmet Needs (1.1.2.2.2)": {},
                        "Feature Requests (1.1.2.2.3)": {}
                    }
                }
            },
            "Design (1.2)": {
                "Brainstorming (1.2.1)": {
                    "Initial Concepts (1.2.1.1)": {
                        "Design Sketches (1.2.1.1.1)": {},
                        "3D Models (1.2.1.1.2)": {},
                        "Prototype Ideas (1.2.1.1.3)": {}
                    }
                },
                "Battery & Charging (1.2.2)": {
                    "Battery Selection (1.2.2.1)": {
                        "Capacity Requirements (1.2.2.1.1)": {},
                        "Size Constraints (1.2.2.1.2)": {},
                        "Temperature Management (1.2.2.1.3)": {}
                    },
                    "Charging Circuit (1.2.2.2)": {
                        "Circuit Layout (1.2.2.2.1)": {},
                        "Component Selection (1.2.2.2.2)": {},
                        "Safety Features (1.2.2.2.3)": {}
                    }
                },
                "Electronics Design (1.2.5)": {
                    "Circuit Design (1.2.5.1)": {
                        "Schematic Design (1.2.5.1.1)": {},
                        "PCB Layout (1.2.5.1.2)": {},
                        "Component Selection (1.2.5.1.3)": {}
                    },
                    "Bluetooth Integration (1.2.5.2)": {
                        "Module Selection (1.2.5.2.1)": {},
                        "Antenna Design (1.2.5.2.2)": {},
                        "Power Optimization (1.2.5.2.3)": {}
                    }
                }
            },
            "Build (1.3)": {
                "Component Sourcing (1.3.1)": {
                    "Battery Procurement (1.3.1.1)": {
                        "Supplier Selection (1.3.1.1.1)": {},
                        "Quality Verification (1.3.1.1.2)": {},
                        "Cost Negotiation (1.3.1.1.3)": {}
                    },
                    "Electronics Components (1.3.1.2)": {
                        "Component List (1.3.1.2.1)": {},
                        "Supplier Quotes (1.3.1.2.2)": {},
                        "Lead Time Analysis (1.3.1.2.3)": {}
                    }
                },
                "Prototype Development (1.3.3)": {
                    "Initial Prototype (1.3.3.1)": {
                        "3D Printing (1.3.3.1.1)": {},
                        "Assembly (1.3.3.1.2)": {},
                        "Testing (1.3.3.1.3)": {}
                    },
                    "Final Prototype (1.3.3.2)": {
                        "Production Methods (1.3.3.2.1)": {},
                        "Quality Control (1.3.3.2.2)": {},
                        "Documentation (1.3.3.2.3)": {}
                    }
                }
            },
            "Testing (1.4)": {
                "Quality Assurance (1.4.1)": {
                    "Component Testing (1.4.1.1)": {
                        "Electrical Testing (1.4.1.1.1)": {},
                        "Mechanical Testing (1.4.1.1.2)": {},
                        "Safety Testing (1.4.1.1.3)": {}
                    }
                },
                "Durability Testing (1.4.2)": {
                    "Drop Testing (1.4.2.1)": {
                        "Height Tests (1.4.2.1.1)": {},
                        "Impact Analysis (1.4.2.1.2)": {},
                        "Failure Points (1.4.2.1.3)": {}
                    },
                    "Environmental Testing (1.4.2.2)": {
                        "Temperature Range (1.4.2.2.1)": {},
                        "Water Resistance (1.4.2.2.2)": {},
                        "UV Exposure (1.4.2.2.3)": {}
                    }
                }
            },
            "Marketing (1.5)": {
                "Digital Marketing (1.5.2)": {
                    "Social Media (1.5.2.1)": {
                        "Content Calendar (1.5.2.1.1)": {},
                        "Influencer Strategy (1.5.2.1.2)": {},
                        "Ad Campaigns (1.5.2.1.3)": {}
                    },
                    "E-commerce (1.5.2.2)": {
                        "Amazon Setup (1.5.2.2.1)": {},
                        "Website Design (1.5.2.2.2)": {},
                        "Payment Integration (1.5.2.2.3)": {}
                    }
                },
                "Customer Support (1.5.4)": {
                    "Support System (1.5.4.1)": {
                        "Ticketing System (1.5.4.1.1)": {},
                        "Knowledge Base (1.5.4.1.2)": {},
                        "Support Team (1.5.4.1.3)": {}
                    }
                }
            },
            "Production & Deployment (1.6)": {
                "Manufacturing Setup (1.6.1)": {
                    "Assembly Line Design (1.6.1.1)": {
                        "Layout Planning (1.6.1.1.1)": {},
                        "Equipment Selection (1.6.1.1.2)": {},
                        "Workflow Optimization (1.6.1.1.3)": {}
                    },
                    "Quality Control System (1.6.1.2)": {
                        "Inspection Points (1.6.1.2.1)": {},
                        "Testing Stations (1.6.1.2.2)": {},
                        "Documentation System (1.6.1.2.3)": {}
                    },
                    "Supply Chain Setup (1.6.1.3)": {
                        "Supplier Management (1.6.1.3.1)": {},
                        "Inventory Control (1.6.1.3.2)": {},
                        "Logistics Planning (1.6.1.3.3)": {}
                    }
                },
                "Production Planning (1.6.2)": {
                    "Capacity Planning (1.6.2.1)": {
                        "Equipment Capacity (1.6.2.1.1)": {},
                        "Labor Requirements (1.6.2.1.2)": {},
                        "Production Targets (1.6.2.1.3)": {}
                    },
                    "Process Documentation (1.6.2.2)": {
                        "Work Instructions (1.6.2.2.1)": {},
                        "Quality Standards (1.6.2.2.2)": {},
                        "Safety Procedures (1.6.2.2.3)": {}
                    }
                },
                "Deployment (1.6.3)": {
                    "Distribution Network (1.6.3.1)": {
                        "Warehousing (1.6.3.1.1)": {},
                        "Shipping Partners (1.6.3.1.2)": {},
                        "Inventory Management (1.6.3.1.3)": {}
                    },
                    "Retail Integration (1.6.3.2)": {
                        "Store Setup (1.6.3.2.1)": {},
                        "Staff Training (1.6.3.2.2)": {},
                        "POS Integration (1.6.3.2.3)": {}
                    },
                    "Post-Launch Support (1.6.3.3)": {
                        "Technical Support (1.6.3.3.1)": {},
                        "Warranty Service (1.6.3.3.2)": {},
                        "Customer Feedback (1.6.3.3.3)": {}
                    }
                }
            }
        }
    }

    wbs_builder.create_wbs_diagram(
        wbs_structure=wbs_data,
        output_filename="wbs_diagram",
        file_format="pdf",
        graph_direction="LR",
        colors=colors
    )

    logger.info("WBS diagram generation complete.")

if __name__ == "__main__":
    main()

