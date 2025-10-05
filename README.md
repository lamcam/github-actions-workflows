# Demo Python Script Workflow

## Description
Example Python script run via **GitHub Actions**, taking input from **environment variables** and **arguments**, writing output to `output.txt`, and uploading it as an artifact.

## Script
`script.py` accepts two inputs:
- `MY_VARIABLE`
- `MY_STRING`

Prints the result to console and `output.txt`.

## Workflow
- Triggered on push to `master`, tags `v*.*.*`, or manually.
- Sets up Python 3.11, runs the script, writes results to **GitHub Actions summary** and uploads **artifact**.
