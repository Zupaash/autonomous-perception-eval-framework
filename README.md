# Autonomous Perception Evaluation Framework

A research-focused validation framework designed to evaluate the trade-offs between perception capability and temporal performance in autonomous systems. Rather than focusing solely on static detection accuracy, this framework emphasizes **inference behavior**, **latency reliability (P₉₅/P₉₉ bounds)**, and **hardware resource utilization** under deployment-constrained environments.

---

## 🎯 Study Structure & Research Focus

Autonomous systems operate under strict temporal and physical constraints. While modern object detection networks achieve remarkable accuracy, their real-world suitability depends heavily on deterministic execution bounds and computational efficiency. 

### Primary Research Question
* How do temporal constraints influence the deployment feasibility of perception systems in autonomous robotic environments?

### Secondary Research Questions
* How do latency distributions vary across object detection architectures?
* To what extent do latency spikes (P₉₅ and P₉₉ bounds) impact the safety and reliability of perception pipelines?
* What computational trade-offs emerge between perception quality (model scale) and hardware utilization?

---

## 📂 Minimalist Architecture

The project is structured to eliminate software engineering bloat, isolating validation mechanics into three highly focused, decoupled modules within a single entry-point execution system:

```text
perception_eval/
├── docs/                  # Study background and documentation
├── experiments/           # Generated evaluation output and markdown logs
├── src/
│   ├── detector.py        # SafetyCriticalDetector wrapper for the network
│   ├── profiler.py        # PerformanceProfiler high-precision evaluation loops
│   └── logger.py          # Output formatting and telemetry file logger
└── run_eval.py            # Master automated multi-model batch runner
```

---

## 🛠️ Getting Started & Replication

### 1. Installation
Clone the repository and install the framework's lightweight tracking and perception dependencies:
```bash
pip install ultralytics psutil numpy
```

### 2. Executing the Evaluation Sweep
Run the master script to trigger the automated hardware cache warm-up, microsecond-resolution timing loops, and CPU telemetry collection across multiple model horizons:
```bash
python run_eval.py
```

---

## 📊 Baseline Telemetry Results (CPU Benchmark)

The following baseline metrics were collected across sequential 100-frame loops on an x86 host environment, using mock array video feeds to isolate processing latency from local disk I/O bottlenecks:

| Model Architecture | Mean Latency | Median Latency | $P_{95}$ Reliability Bound | $P_{99}$ Extreme Spike | System Throughput | Avg CPU Load |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **YOLOv8n** (Nano) | 83.76 ms | 82.36 ms | 138.81 ms | 186.57 ms | **11.9 FPS** | 94.9% |
| **YOLOv8s** (Small) | 191.50 ms | 183.39 ms | 216.68 ms | 242.27 ms | **5.2 FPS** | 89.5% |
| **YOLOv8m** (Medium) | 575.39 ms | 562.76 ms | 660.75 ms | 846.71 ms | **1.7 FPS** | 96.1% |

### Key Trade-Off Insights
1. **The Real-Time Boundary:** Standard robotic deployments typically demand a processing threshold of sub-33 ms ($\ge 30$ FPS). This unaccelerated CPU validation highlights a critical barrier—even the lightest configuration (YOLOv8n) is restricted to 11.9 FPS under full physical host strain ($94.9\%$).
2. **The Risk of Latency Jitter:** While YOLOv8n averages 83.76 ms, its **$P_{99}$ latency climbs to 186.57 ms**. For an autonomous drone or vehicle traveling at high speed, this 1% edge-case spike translates to a significant window of localized blindness, proving why tracking average latency alone is insufficient for safety-critical systems.
3. **Non-Linear Complexity Scaling:** Scaling from Nano to Medium induces an exponential latency bottleneck, dragging throughput down to an unusable 1.7 FPS. This emphasizes that model depth/width scaling requires hardware acceleration (GPU/TPU) or advanced edge compiler optimizations (Quantization/TensorRT) to achieve physical viability.

