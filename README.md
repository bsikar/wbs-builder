# WBS Builder

A Python tool for generating Work Breakdown Structure (WBS) and Responsibility Assignment Matrix (RAM) diagrams from YAML configuration files.

## Features

- Generate visual Work Breakdown Structure (WBS) diagrams
- Create detailed Responsibility Assignment Matrix (RAM) diagrams
- Export project data to Excel format
- Support for multiple output formats (PDF, PNG)
- Color-coded visualization of responsibilities and hierarchy levels
- Automatic calculation of project totals and statistics

## Prerequisites

- Python 3.6 or higher
- Graphviz (must be installed on your system)
- Required Python packages (install via pip):
  - pyyaml
  - graphviz
  - pandas
  - openpyxl

## Installation

1. Install Graphviz on your system:
   - **macOS**: `brew install graphviz`
   - **Linux**: `sudo apt-get install graphviz`
   - **Windows**: Download from [Graphviz Downloads](https://graphviz.org/download/)

2. Clone this repository:
   ```bash
   git clone https://github.com/bsikar/wbs-builder.git
   cd wbs-builder
   ```

3. Install Python dependencies:
   ```bash
   pip install pyyaml graphviz pandas openpyxl
   ```

## Usage

1. Create or modify your WBS structure in a YAML file (see `wbs_structure.yaml` for example format)

2. Run the tool:
   ```bash
   python main.py [path_to_yaml_file]
   ```
   If no YAML file is specified, it defaults to `wbs_structure.yaml`

3. The tool will generate:
   - WBS diagram (PDF and PNG)
   - RAM diagram (PDF and PNG)
   - Excel files with project data
   
## YAML File Structure

The YAML file should follow this structure:

```yaml
project:
  name: "Project Name"
  Phase Name:
    Activity Name:
      Task Name:
        Subtask Name:
          responsibilities:
            project_manager: "L/P/R/I"
            hardware: "L/P/R/I"
            software: "L/P/R/I"
            testing: "L/P/R/I"
            sponsor: "L/P/R/I"
            other: "L/P/R/I"
          duration: number_of_days
          labor: person_hours
```

### Responsibility Types
- L = Lead: Primary responsibility
- P = Participant: Active involvement
- R = Reviewer: Reviews and provides feedback
- I = Input: Provides input or consulted
- (empty) = No involvement

## Output Files

- `wbs_output.pdf/png`: Visual Work Breakdown Structure diagram
- `ram_output.pdf/png`: Responsibility Assignment Matrix diagram
- `project_data_wbs.xlsx`: WBS data in Excel format
- `project_data_ram.xlsx`: RAM data in Excel format

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request