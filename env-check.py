# ============================================================================
# STEP 1: Environment Check and Dependency Analysis
# ============================================================================

# Check current Python version and CUDA availability
import sys
import subprocess
import pkg_resources

print("=== ENVIRONMENT CHECK ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Check if we're in a virtual environment
import os
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("✅ Running in virtual environment")
else:
    print("⚠️  Not in virtual environment")

# Check CUDA availability
try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU count: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
except ImportError:
    print("❌ PyTorch not installed")

# Check current installed packages
print("\n=== CURRENTLY INSTALLED PACKAGES ===")
try:
    installed_packages = [d.project_name for d in pkg_resources.working_set]
    relevant_packages = ['torch', 'transformers', 'accelerate', 'peft', 'bitsandbytes', 'trl', 'datasets']
    
    for package in relevant_packages:
        try:
            version = pkg_resources.get_distribution(package).version
            print(f"✅ {package}: {version}")
        except pkg_resources.DistributionNotFound:
            print(f"❌ {package}: Not installed")
except Exception as e:
    print(f"Error checking packages: {e}")

print("\n=== SYSTEM INFO ===")
# Check system info
try:
    result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ NVIDIA GPU detected")
        print("GPU Memory Info:")
        lines = result.stdout.split('\n')
        for line in lines:
            if 'MiB' in line and ('/' in line):
                print(f"  {line.strip()}")
    else:
        print("❌ nvidia-smi failed")
except FileNotFoundError:
    print("❌ nvidia-smi not found")

print("\n" + "="*50)
print("Please run this first and share the output!")
print("="*50)