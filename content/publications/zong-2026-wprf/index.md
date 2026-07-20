---
title: "Widest-Path Reachability Fields for Connectivity-Preserving Slender Structure Segmentation"
authors:
  - youcheng-zong
  - Runda Jia
  - Minxuan Hu
  - Weilan Su
  - Dakuo He
date: "2026-07-08T08:04:06Z"
publishDate: "2026-07-08T08:04:06Z"
publication_types: ["preprint"]
publication: "arXiv preprint arXiv:2607.07123"
publication_short: "arXiv"
abstract: >-
  Segmenting slender curvilinear structures such as retinal vessels, cracks, and roads demands topological correctness, as even a single-pixel discontinuity can fragment a continuous network and invalidate downstream analysis. Under standard binary-mask supervision, models optimized for pixel-level overlap frequently produce topologically broken predictions. We trace this to a fundamental mismatch: pixel-wise losses distribute gradients uniformly, yet connectivity hinges on a sparse set of bottleneck pixels. These pixels are vastly outnumbered by thick structures and background, rendering their aggregate gradient contribution negligible. We term this phenomenon topological gradient starvation (TGS). To address it, we propose Widest-Path Reachability Fields (WPRF), a differentiable Max-Min reachability objective that redirects gradient flow to connectivity bottlenecks. The module is plug-and-play, backbone-agnostic, and incurs no inference overhead. WPRF implements a differentiable Max-Min objective via dynamic programming on a domain-restricted graph, coupled with a bottleneck-aware observation term that balances gradient contributions across varying structures. Compared to prior topology-aware losses that rely on post-hoc skeletonization or homology computation, WPRF directly optimizes end-to-end reachability via differentiable Max-Min algebra, enabling gradient flow to concentrate on connectivity bottlenecks without auxiliary structures. We introduce OMVIS, a new oral microvessel segmentation dataset. Experiments across nine architectures and six datasets validate the bottleneck-focused gradient routing mechanism. WPRF improves 87% of experiments with fixed hyperparameters and achieves clDice gains of 7.2 percentage points on structurally fragile datasets.
summary: "A differentiable Max-Min reachability objective that redirects training gradients toward connectivity bottlenecks in slender-structure segmentation."
tags:
  - Slender Structure Segmentation
  - Connectivity Preservation
  - Topological Learning
featured: true
links:
  - type: custom
    url: https://arxiv.org/abs/2607.07123
    label: arXiv
    icon: academicons/arxiv
  - type: custom
    url: https://github.com/mituan-ai/WPRF_open
    label: Code
    icon: brands/github
image:
  filename: featured.webp
  caption: "Qualitative comparison on road and retinal-vessel segmentation."
  focal_point: "Center"
  preview_only: false
projects: []
slides: ""
---
