# ============================================================================
# STEP 2: Sequential Dependency Installation
# ============================================================================

import subprocess
import sys

def run_pip_install(packages, description):
    """Install packages with proper error handling"""
    print(f"\n🔄 Installing {description}...")
    for package in packages:
        try:
            print(f"   Installing: {package}")
            result = subprocess.run([sys.executable, "-m", "pip", "install", package], 
                                  capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                print(f"   ✅ {package} installed successfully")
            else:
                print(f"   ❌ Failed to install {package}")
                print(f"   Error: {result.stderr}")
        except subprocess.TimeoutExpired:
            print(f"   ⏰ Timeout installing {package}")
        except Exception as e:
            print(f"   ❌ Exception installing {package}: {e}")

# Your current versions:
# ✅ torch: 2.6.0 (newer than needed - compatible)
# ✅ transformers: 4.30.1 (slightly older - needs update)
# ✅ accelerate: 0.34.2 (newer - compatible)
# ✅ peft: 0.4.0 (perfect)
# ❌ bitsandbytes: Not installed
# ❌ trl: Not installed
# ✅ datasets: 2.16.1 (newer - compatible)

print("=== STEP 2: FIXING DEPENDENCIES ===")
print("Current status analysis:")
print("✅ PyTorch 2.6.0 - Good (newer version)")
print("⚠️  Transformers 4.30.1 - Needs update for Llama-3.1")
print("✅ Accelerate 0.34.2 - Good (newer version)")
print("✅ PEFT 0.4.0 - Perfect")
print("❌ BitsAndBytes - Missing")
print("❌ TRL - Missing")
print("✅ Datasets 2.16.1 - Good (newer version)")

# Step 2A: Install missing critical packages
print("\n" + "="*50)
print("STEP 2A: Installing missing packages")
print("="*50)

missing_packages = [
    "bitsandbytes>=0.41.0",  # Updated for compatibility with PyTorch 2.6
    "trl>=0.7.0"             # Updated for compatibility
]

run_pip_install(missing_packages, "missing critical packages")

# Step 2B: Update transformers for Llama-3.1 support
print("\n" + "="*50)
print("STEP 2B: Updating transformers for Llama-3.1")
print("="*50)

transformers_update = [
    "transformers>=4.43.0"  # Required for Llama-3.1
]

run_pip_install(transformers_update, "transformers update")

# Step 2C: Install additional helpful packages
print("\n" + "="*50)
print("STEP 2C: Installing additional packages")
print("="*50)

additional_packages = [
    "scipy",
    "tensorboard",
    "wandb",
    "sentencepiece",  # Often needed for tokenizers
    "protobuf"        # Often causes conflicts if not specified
]

run_pip_install(additional_packages, "additional packages")

print("\n" + "="*50)
print("INSTALLATION COMPLETE!")
print("="*50)
print("Please restart your kernel and run Step 3 verification!")