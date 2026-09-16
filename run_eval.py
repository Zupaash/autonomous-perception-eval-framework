from src.profiler import PerformanceProfiler
from src.logger import output_telemetry

def main():
    print("=" * 60)
    print("  STARTING AUTOMATED MULTI-MODEL PERCEPTION EVALUATION  ")
    print("=" * 60)
    
    # Define a clean list of candidate architectures you want to evaluate
    candidate_models = ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"]
    
    print(f"[*] Launching batch evaluation loops for: {candidate_models}")
    
    for model_name in candidate_models:
        print(f"\n[>>>] BEGINNING ACTIVE EVALUATION FOR: {model_name} [<<<]")
        
        # 1. Initialize profiler for this model (using 100 sample frames)
        runner = PerformanceProfiler(model_weight=model_name, frames=100)
        
        # 2. Run the measurement evaluation loops
        telemetry_data = runner.measure_pipeline()
        
        # 3. Output metrics to console and save distinct markdown logs
        output_telemetry(telemetry_data, model_name)
        
    print("\n" + "=" * 60)
    print("  ALL BENCHMARKS COMPLETE. CHECK YOUR /experiments FOLDER!  ")
    print("=" * 60)

if __name__ == "__main__":
    main()
