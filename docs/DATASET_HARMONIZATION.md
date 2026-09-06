# Dataset Harmonization Protocol

To ensure valid cross-dataset generalization for the W-NETR and NLMS evaluation, all four datasets (ADFECGDB, FECGSYNDB, NInFEA, PCDB) are strictly harmonized to a common physiological structure before feeding into the PyTorch dataloaders.

## 1. Sampling Rate
- **Target Rate**: 1000 Hz.
- **Resampling Method**: Polyphase filtering (e.g. `scipy.signal.resample_poly`) to prevent aliasing.
- **Why**: ADFECGDB, NInFEA, and PCDB are native 1000 Hz. FECGSYNDB is native 250 Hz and must be upsampled to match the dimensionality required by the fixed-length W-NETR patch embeddings.

## 2. Signal Polarity and Naming
- All maternal reference channels are mapped to index `0`.
- All abdominal mixtures are mapped to indices `1` through `N`.
- Any reversed polarity channels (e.g. due to electrode placement differences in NInFEA) are manually inverted if documented in the dataset.

## 3. Windowing Strategy
- **Window Length**: 2.0 seconds (2000 samples at 1000 Hz).
- **Overlap**: None for test set. 50% overlap permitted for training set augmentation.
- **Transients**: The first and last 2.0 seconds of every recording are dropped to prevent edge filter transients.

## 4. Normalization and Scaling
- **Amplitude Scaling**: All signals are scaled to millivolts (mV) before any deep learning normalization.
- **Normalization Strategy**: Z-score normalization `(x - mu) / sigma`.
- **CRITICAL**: `mu` and `sigma` are calculated strictly per-channel, **using only the training split**. These exact statistics are saved and applied deterministically to the validation and test sets.

## 5. Missing Values and Signal Quality
- Segments with `NaN` values or flatlines exceeding 0.1 seconds are dropped entirely.
- No imputation is performed on the locked test sets.
