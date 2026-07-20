---
title: "Open-Ended Scenario Reasoning for Specialist Model Adaptation"
authors:
  - youcheng-zong
  - Runda Jia
  - Ranmeng Lin
  - Mingxuan Ren
  - Dakuo He
date: "2026-07-07T11:29:45Z"
publishDate: "2026-07-07T11:29:45Z"
publication_types: ["preprint"]
publication: "arXiv preprint arXiv:2607.06625"
publication_short: "arXiv"
abstract: >-
  Process industries have accumulated validated specialist models, yet sensor drift, feedstock variation, and regime switching cause these models to degrade systematically in new scenarios. Collecting new labeled data and retraining is costly, while continuing with the original model incurs persistent bias. Existing adaptation methods require modifying model parameters with sufficient labeled data, making rapid response on deployed systems difficult. Using LLMs as direct predictors risks hallucinations and uncontrollable outputs. Such predictors also cannot incorporate unstructured scenario knowledge from the field. To address these limitations, this article proposes Reasoning-Driven Open Adaptation for Specialist Models (ROAM), a framework that uses LLM world knowledge and reasoning to adapt frozen specialist models to unseen scenarios without retraining. ROAM confines all corrections to a low-dimensional, semantically interpretable latent space. LLM-generated scenario judgments and online observations are fused under a unified probabilistic framework. A risk-constrained mechanism suppresses corrections under unreliable LLM evidence or abrupt scenario shifts and falls back to the original frozen model when evidence is insufficient. Experiments on a mineral thickening process and the public IndPenSim penicillin fermentation dataset show that ROAM reduces MAE by over 20% in major shift settings such as hidden shifts with only 839 additional parameters and under 0.02 ms per-step overhead. These results indicate that LLM reasoning can be turned into a conservative adaptation signal for industrial models already in service.
summary: "A risk-gated Bayesian adaptation framework that uses open-ended scenario evidence to correct frozen specialist models without retraining."
tags:
  - Specialist Model Adaptation
  - Bayesian Inference
  - Industrial AI
featured: true
links:
  - type: custom
    url: https://arxiv.org/abs/2607.06625
    label: arXiv
    icon: academicons/arxiv
  - type: custom
    url: https://github.com/mituan-ai/ROAM_open
    label: Code
    icon: brands/github
image:
  filename: featured.webp
  caption: "Comparison of parameter updating, LLM-as-predictor, and ROAM adaptation."
  focal_point: "Center"
  preview_only: false
projects: []
slides: ""
---
