# Advent of Code 2024 - Python Solutions

Solutions for [Advent of Code 2024](https://adventofcode.com/2024) implemented in Python.

## Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

## Project Structure

```markdown
advent-py-24/
├── src/
│   ├── solutions/      # Daily solutions
│   │   └── day_01.py
│   └── utils/         # Common utilities
├── tests/
│   └── solutions/     # Solution tests
└── inputs/           # Daily puzzle inputs
```

## Development

* Solutions are organized by day in ```src/solutions/```
* Each day has its corresponding test file in ```tests/solutions/```
* Input files should be placed in ```inputs/```
* Run tests with ```pytest```
* Code formatting: ```black .```
* Type checking: ```mypy .```
* Linting: ```ruff .```

## Running Solutions

```bash
# Run specific day
python -m src.solutions.day_01

# Run tests for specific day
pytest tests/solutions/test_day_01.py
```

## License

Copyright 2024

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
