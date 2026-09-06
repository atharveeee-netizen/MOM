import matplotlib.pyplot as plt
import numpy as np

# Set publication style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, axes = plt.subplots(1, 3, figsize=(14, 4.2), dpi=300)

colors = ['#10B981', '#F59E0B'] # Emerald green (NLMS winner) vs Amber (W-NETR)

# 1. Extraction Error (RMSE in mV) - Lower is better
methods = ['32-tap NLMS\n(Deterministic)', '1D W-NETR\n(Deep Learning)']
rmse_vals = [0.1005, 0.43398]
bars1 = axes[0].bar(methods, rmse_vals, color=colors, width=0.55, edgecolor='#333', linewidth=1.2)
axes[0].set_ylabel('RMSE (mV) [Lower is Better]', fontsize=11, fontweight='bold', color='#1E293B')
axes[0].set_title('Extraction Accuracy (Held-out r10)', fontsize=12, fontweight='bold', pad=12, color='#0F172A')
axes[0].set_ylim(0, 0.52)
for bar in bars1:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2.0, yval + 0.015, f'{yval:.4f} mV', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#0F172A')
axes[0].text(0.5, 0.85, 'NLMS: 4.3x Lower Error', transform=axes[0].transAxes, ha='center', fontsize=9.5, fontweight='semibold', color='#047857', bbox=dict(boxstyle='round,pad=0.4', facecolor='#ECFDF5', edgecolor='#10B981'))

# 2. Computational Complexity (Parameter Count) - Lower is better
param_vals = [32, 1241729]
bars2 = axes[1].bar(methods, [np.log10(p) for p in param_vals], color=colors, width=0.55, edgecolor='#333', linewidth=1.2)
axes[1].set_ylabel('Parameters (log10 scale)', fontsize=11, fontweight='bold', color='#1E293B')
axes[1].set_title('Model Complexity & Weights', fontsize=12, fontweight='bold', pad=12, color='#0F172A')
axes[1].set_ylim(0, 7)
axes[1].text(bars2[0].get_x() + bars2[0].get_width()/2.0, bars2[0].get_height() + 0.2, '32 taps\n(~128 B)', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#0F172A')
axes[1].text(bars2[1].get_x() + bars2[1].get_width()/2.0, bars2[1].get_height() + 0.2, '1.24M weights\n(~4.9 MB)', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#0F172A')
axes[1].text(0.5, 0.85, '38,800x Fewer Parameters', transform=axes[1].transAxes, ha='center', fontsize=9.5, fontweight='semibold', color='#047857', bbox=dict(boxstyle='round,pad=0.4', facecolor='#ECFDF5', edgecolor='#10B981'))

# 3. Edge Feasibility & Execution Latency
latency_vals = [1.8, 420.0]
bars3 = axes[2].bar(methods, [1.8, 150.0], color=colors, width=0.55, edgecolor='#333', linewidth=1.2)
axes[2].set_ylabel('Inference Time (ms / window)', fontsize=11, fontweight='bold', color='#1E293B')
axes[2].set_title('Edge MCU Feasibility', fontsize=12, fontweight='bold', pad=12, color='#0F172A')
axes[2].set_ylim(0, 180)
axes[2].text(bars3[0].get_x() + bars3[0].get_width()/2.0, 1.8 + 6, '1.8 ms\n(Cortex-M4F)', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#047857')
axes[2].text(bars3[1].get_x() + bars3[1].get_width()/2.0, 150.0 + 6, '>420 ms (Desktop)\nInfeasible on MCU', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#B45309')
axes[2].text(0.5, 0.85, 'Real-Time Edge Streaming', transform=axes[2].transAxes, ha='center', fontsize=9.5, fontweight='semibold', color='#047857', bbox=dict(boxstyle='round,pad=0.4', facecolor='#ECFDF5', edgecolor='#10B981'))

for ax in axes:
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.suptitle('Classical Adaptive DSP (32-tap NLMS) vs. Deep Learning (1D W-NETR) Benchmark Evaluation', fontsize=14, fontweight='bold', y=1.03, color='#0F172A')
plt.tight_layout()
plt.savefig('docs/media/nlms_vs_wnetr_benchmark.png', dpi=300, bbox_inches='tight')
print('Generated docs/media/nlms_vs_wnetr_benchmark.png successfully')
