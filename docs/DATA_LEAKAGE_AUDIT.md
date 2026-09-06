# Data Leakage Audit & Prevention Policy

To ensure maximum scientific rigor, this project enforces strict zero-leakage policies across all machine learning and classical signal processing pipelines.

## 1. Subject-Wise Splitting Guarantee
Absolutely no random window-level splitting is permitted. If window-level splitting is used, segments from the same patient will appear in both the training and test sets, artificially inflating correlation and suppressing RMSE.
- **Enforcement**: Splits are defined explicitly at the recording/subject level in `data/splits/`.

## 2. Locked Test Set Definition
The test subjects (e.g. `r10` for ADFECGDB, `sub09-10` for FECGSYNDB) are mathematically locked.
- **Enforcement**: The test set is only evaluated during the final `evaluate_ai.py` pass. It is strictly excluded from:
  - Architecture search.
  - Hyperparameter tuning.
  - Early stopping triggers (validation set is used instead).
  - Threshold selection for peak detection.

## 3. Augmentation Boundaries
- Data augmentation (amplitude scaling, noise injection) is restricted exclusively to the `TRAIN` splits. 
- Validation and Test sets are evaluated on raw, unaugmented physiological signals to reflect true clinical conditions.

## 4. Normalization Statistics
- Any mean (`mu`) and standard deviation (`sigma`) calculated for Z-score normalization must be derived entirely from the training set array.
- Code asserting `x_test = (x_test - mean(x_all)) / std(x_all)` is strictly forbidden and actively audited by the CI/CD pipeline.
