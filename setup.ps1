# Step 1: Create a virtual environment if not already created
if (-Not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
} else {
    Write-Host "Virtual environment already exists."
}

# Step 2: Activate the virtual environment
Write-Host "Activating the virtual environment..."
& .\.venv\Scripts\Activate.ps1

# Step 3: Install required packages from requirements.txt (if it exists)
if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt found."
}

# Step 4: Set the PYTHONPATH
Write-Host "Setting PYTHONPATH..."
$env:PYTHONPATH = ".\src" + ";" + $env:PYTHONPATH

# Optional: Inform the user about the environment setup
Write-Host "Virtual environment set up and PYTHONPATH configured."