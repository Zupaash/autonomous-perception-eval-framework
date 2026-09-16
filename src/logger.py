import os

def output_telemetry(results: dict, model_name: str):
    """Prints results cleanly and saves them to a designated model log file."""
    report = f"""
=====================================================
    PERCEPTION VALIDATION TELEMETRY: {model_name.upper()}     
=====================================================
Mean Latency            : {results['mean']:.2f} ms
Median Latency          : {results['median']:.2f} ms
P95 Reliability Bound   : {results['p95']:.2f} ms (Worst 5% Spikes)
P99 Reliability Bound   : {results['p99']:.2f} ms (Worst 1% Spikes)
System Throughput       : {results['fps']:.1f} FPS
Average CPU Profile     : {results['cpu']:.1f} %
=====================================================
"""
    # Print the report output to your terminal screen
    print(report)
    
    # Isolate the file prefix name (e.g., 'yolov8n' from 'yolov8n.pt')
    clean_name = model_name.split('.')[0]
    
    # Save the run metrics straight to your experiments folder
    os.makedirs("experiments", exist_ok=True)
    file_path = f"experiments/{clean_name}_report.md"
    
    with open(file_path, "w") as f:
        f.write(f"# Benchmarking Baseline: {model_name}\n```text\n{report}\n```")
    print(f"[*] Saved telemetry report to: {file_path}")
