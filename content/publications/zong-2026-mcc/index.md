---
title: "LLM-Guided Measurement Credibility Correction for Trustworthy Industrial Process Inference"
authors:
  - youcheng-zong
  - Runda Jia
  - Dakuo He
date: "2026-07-07T10:21:55Z"
publishDate: "2026-07-07T10:21:55Z"
publication_types: ["preprint"]
publication: "arXiv preprint arXiv:2607.06111"
publication_short: "arXiv"
abstract: >-
  Industrial prediction and soft sensing depend on credible input measurements. In field deployment, a predictor may receive biased, delayed, stale, or derived measurements that still look plausible. Prediction can then fail before the forecasting backbone becomes the main limitation, because the input window no longer represents the real process. Sensor reconstruction, data reconciliation, and fault-tolerant soft sensing reduce this risk, but they often rely on numerical correlation, alarms, fault labels, or explicit process equations. These assumptions are not always available. A correlated variable can also be an unsafe reference when variables share instruments, derived formulas, soft-sensing chains, or control actions. The key issue is to decide before prediction which external measurements can credibly support the current measurement. To address this issue, this article proposes LLM-Guided Measurement Credibility Correction (MCC). MCC converts measurement meanings in process documents into measurement semantics usable by numerical models. It builds independent process references from semantically qualified external measurements and corrects local measurement conflicts before prediction. The predictor therefore receives a more credible input window. Across multiple complex industrial forecasting and soft-sensing tasks, +MCC achieves average relative MAE reductions of 30.7% on real-test protocols and 80.3% on controlled-corruption protocols. It adds only 0.5--2.0k online parameters, with the slowest +MCC inference time at 0.089 ms/step. These results show that measurement semantics can turn process documents into lightweight pre-inference credibility correction and improve prediction accuracy.
summary: "A pre-inference correction framework that uses measurement semantics to build independent references for locally inconsistent industrial signals."
tags:
  - Measurement Credibility
  - Industrial Forecasting
  - Soft Sensing
featured: true
links:
  - type: custom
    url: https://arxiv.org/abs/2607.06111
    label: arXiv
    icon: academicons/arxiv
image:
  filename: featured.webp
  caption: "Offline semantic construction, observer calibration, and online measurement correction."
  focal_point: "Center"
  preview_only: false
projects: []
slides: ""
---
