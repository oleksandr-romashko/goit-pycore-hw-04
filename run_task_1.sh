#!/bin/bash

# 1. Activate the virtual environment
source /path/to/your/venv/bin/activate

# 2. Set the PYTHONPATH (this is equivalent to adding extra paths in settings.json)
export PYTHONPATH=$(pwd)/src:$PYTHONPATH

# 3. Run the specific task's main.py (task_1 in this case)
python src/task_1/main.py