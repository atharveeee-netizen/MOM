import gdown
import os

import os
os.environ["XDG_CACHE_HOME"] = os.path.abspath(".cache")
os.makedirs(".cache", exist_ok=True)
print("Downloading W-NETR pre-trained models...")
os.makedirs("W-NETR-for-FECG-extraction/models", exist_ok=True)

# Simulation dataset model
sim_url = 'https://drive.google.com/uc?id=1NljEmZJaBb4hT3sLJ_HFAJDJhEt4HoJv'
sim_output = 'W-NETR-for-FECG-extraction/models/50_simulation.pkl'
print(f"Downloading {sim_output}...")
gdown.download(sim_url, sim_output, quiet=False, use_cookies=False)

# Real dataset model
real_url = 'https://drive.google.com/uc?id=1wUzuZcAJmcaXPsYv-rgApjhke8mCuVZh'
real_output = 'W-NETR-for-FECG-extraction/models/50_real.pkl'
print(f"Downloading {real_output}...")
gdown.download(real_url, real_output, quiet=False, use_cookies=False)

print("Models downloaded successfully!")
