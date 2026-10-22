---
title: "LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting"
authors:
  - youcheng-zong
  - Runda Jia
  - Mingxuan Ren
  - Dakuo He
date: "2026-10-22T00:00:00+08:00"
publishDate: "2026-07-07T10:39:45Z"
publication_types: ["article-journal"]
publication: "IEEE Transactions on Industrial Informatics (Accepted)"
publication_short: "IEEE TII (Accepted)"
abstract: >-
  Process industries rely on time-series forecasting and soft sensing to estimate quality variables that are hard to measure online. Labeled data are scarce, operating regimes change frequently, and retraining models or rebuilding alignment pipelines for each scenario is costly. Such settings often provide variable tables and process documents that record variable names, units, physical meanings, and process roles. However, standard time-series backbones usually treat inputs as anonymous numerical columns. Existing text-enhanced methods also rarely make the semantic-logical relations between input variables and the prediction target available to the model within each numerical window. To address this problem, this article proposes Task-Semantic Field Factorization (TSF), a large language model (LLM)-guided framework. TSF builds a task-semantic field from task protocols and variable documents before training and uses the LLM only for offline semantic construction. Online training and inference remain with conventional time-series backbones. During training and inference, the current numerical window activates variable semantics, so semantic information participates in each prediction and supports adaptation to different prediction targets and operating shifts. On multiple complex industrial forecasting and soft-sensing tasks, TSF reduces MAE by 6.4% on average in improved settings, with the largest reduction reaching 25.5%. It adds only about 1.8--3.0k parameters, with less than 0.008 ms/step of additional online inference overhead. These results show that TSF turns existing process documents into measurable forecasting gains across backbones and semantic generators while remaining lightweight for deployment.
summary: "An offline LLM-guided input factorization that lets each numerical window activate task-aware variable semantics before a standard forecasting backbone."
tags:
  - Industrial Time Series
  - Variable Semantics
  - Soft Sensing
featured: true
links:
  - type: custom
    url: https://arxiv.org/abs/2607.06623
    label: arXiv
    icon: academicons/arxiv
image:
  filename: featured.webp
  caption: "Comparison of numerical, text-augmented, and task-semantic forecasting paradigms."
  focal_point: "Center"
  preview_only: false
projects: []
slides: ""
---
