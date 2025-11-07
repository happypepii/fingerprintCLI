# FingerprintCLI

A simple CLI tool for analyzing and comparing plugin artifacts (ZIP/JAR files).

## Installation

```bash
poetry install
```

## Usage

```bash
# 1. Analyze first plugin
poetry run fingerprintcli analyze plugin1.jar -o output1.json

# 2. Analyze second plugin
poetry run fingerprintcli analyze plugin2.jar -o output2.json

# 3. Compare the two outputs
poetry run fingerprintcli compare output1.json output2.json
```