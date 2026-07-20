---
title: ""
summary: "Research on LLMs for industrial systems, time-series modeling, and structure-aware visual analysis."
date: "2026-07-19"
type: "landing"
sections:
  - block: "resume-biography-3"
    id: "biography"
    content:
      username: "youcheng-zong"
      text: |-
        I am a PhD candidate in Control Science and Engineering at Northeastern
        University, China. I develop LLM-based methods for industrial
        forecasting, measurement correction, model adaptation, and decision
        support. I also study structure-aware visual analysis for medical
        imaging.
      headings:
        about: "About"
    design:
      name:
        size: "sm"
      avatar:
        size: "medium"
        shape: "circle"
      biography:
        style: "max-width: 46rem;"
      spacing:
        padding: ["0", "0"]

  - block: "resume-experience"
    id: "education"
    content:
      username: "youcheng-zong"
    design:
      date_format: "Jan 2006"
      is_education_first: true

  - block: "stats"
    id: "metrics"
    content:
      items:
        - statistic: "14"
          description: "Publications and preprints"
        - statistic: "110"
          description: "Google Scholar citations"
        - statistic: "5"
          description: "h-index"
        - statistic: "3"
          description: "i10-index"
    design:
      layout: "minimal"
      numbers_gradient: false
      spacing:
        padding: ["0", "0"]
      background:
        color: "color-mix(in srgb, var(--hb-color-background) 97%, var(--hb-color-foreground) 3%)"

  - block: "features"
    id: "research"
    content:
      title: "Research"
      text: "My work connects LLMs, numerical time series, and visual structure under real process constraints."
      items:
        - name: "LLMs for industrial systems"
          description: "Retrieval, tool use, and constrained reasoning for industrial analysis and decision support."
          icon: "hero/cpu-chip"
        - name: "Semantic industrial forecasting"
          description: "Forecasting and soft sensing that connect numerical windows with variable meaning and process context."
          icon: "hero/chart-bar-square"
        - name: "Structure-aware visual analysis"
          description: "Connectivity-preserving segmentation and multimodal analysis for clinical and industrial images."
          icon: "hero/squares-plus"
    design:
      layout: "grid"

  - block: "collection"
    id: "publications"
    content:
      title: "Publications"
      text: "Recent work across industrial intelligence, time-series modeling, and visual analysis."
      filters:
        folders:
          - "publications"
        featured_only: true
      count: 6
      sort_by: "Date"
      order: "desc"
      archive:
        enable: true
        link: "/publications/"
        text: "View all publications"
    design:
      view: "article-grid"
      columns: 3
      fill_image: true
      show_read_time: false
      background:
        color: "color-mix(in srgb, var(--hb-color-background) 94%, var(--hb-color-foreground) 6%)"

  - block: "portfolio"
    id: "projects"
    content:
      title: "Projects"
      count: 4
      filters:
        folders:
          - "projects"
      archive:
        enable: false
    design:
      columns: 2
      status_badge:
        enable: true
      fallback_icon: "hero/beaker"

---
