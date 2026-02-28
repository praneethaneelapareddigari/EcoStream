# EcoStream – Hardware-Aware Adaptive Video Analytics

## Problem
Conventional campus AI vision systems operate at constant peak inference loads regardless of activity, causing idle-compute energy waste.

## Solution
EcoStream implements Adaptive Frame-Rate (AFR):
- Sentry Mode (2 FPS)
- Active Mode (30 FPS)

Dynamic switching reduces unnecessary inference cycles.

## Modeled Compute Reduction
If 70% idle:
(0.7 × 2/30) + (0.3 × 1.0) ≈ 0.35

→ ~65% reduction in inference cycles.

## Tech Stack
- OpenCV
- ONNX Runtime
- INT8-ready architecture

## AMD Alignment
Designed to target AMD Ryzen AI NPU acceleration for improved TOPS/Watt efficiency.