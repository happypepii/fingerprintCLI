"""
Simple Plugin Analyzer CLI
A minimal tool to analyze and compare ZIP/JAR files
"""

import click
import json
import zipfile
from pathlib import Path


@click.group()
def cli():
    """Analyze and compare plugin files (ZIP/JAR)"""
    pass


@cli.command()
@click.argument('plugin_file', type=click.Path(exists=True))
@click.option('-o', '--output', required=True, help='Output JSON file')
def analyze(plugin_file, output):
    """Analyze a plugin file and save structure to JSON"""
    
    # Read ZIP entries
    with zipfile.ZipFile(plugin_file, 'r') as zf:
        entries = zf.namelist()
    
    # Create output data
    data = {
        "name": Path(plugin_file).name,
        "total_files": len(entries),
        "files": sorted(entries)
    }
    
    # Save to JSON
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo(f"✓ Analyzed {len(entries)} files → {output}")


@cli.command()
@click.argument('file1', type=click.Path(exists=True))
@click.argument('file2', type=click.Path(exists=True))
def compare(file1, file2):
    """Compare two analysis JSON files"""
    
    # Load both files
    with open(file1) as f:
        data1 = json.load(f)
    with open(file2) as f:
        data2 = json.load(f)
    
    # Compare
    set1 = set(data1['files'])
    set2 = set(data2['files'])
    
    common = set1 & set2
    only1 = set1 - set2
    only2 = set2 - set1
    
    # Show results
    similarity = len(common) / max(len(set1), len(set2)) * 100
    
    click.echo(f"\n{'='*50}")
    click.echo(f"Plugin 1: {data1['name']}")
    click.echo(f"Plugin 2: {data2['name']}")
    click.echo(f"{'='*50}")
    click.echo(f"Similarity: {similarity:.1f}%")
    click.echo(f"Common files: {len(common)}")
    click.echo(f"Only in 1: {len(only1)}")
    click.echo(f"Only in 2: {len(only2)}")


if __name__ == '__main__':
    cli()