# Folder Organization
The project is organized as follows:
- `src/`: all executable code lives here
    - `main.py`: main file; parses CLI arguments, orchestrates workflow
    - `utils.py`: reusable helper functions (e.g. file handling, hashing, etc.)
    - `config_loader.py`: reads .yaml settings into workspace
- `data/input`: contains input data files
- `data/output`: contains generated files, reports
- `tests/`: any relevant tests scripts for validation
- `logs/`: automatic logging output
- `config/`: contains configurable parameters

# How to run
`./run.sh`: Executes the main python script

## Options
`-t` - Executes the tests only (not the main file)
`-c` - Cleans any created files
`-v` - Verbose Logging
