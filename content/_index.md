---
title: ""
summary: ""
date: "2026-05-04"
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "youcheng-zong"
      text: |
        I am a PhD student in Control Science and Engineering at Northeastern
        University, China. My research focuses on large language models for
        complex industrial processes, industrial time-series modeling, and
        process industry intelligence.
      headings:
        about: "About"
        education: "Education"
        interests: "Research Interests"
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: "md"
      avatar:
        size: "large"
        shape: "circle"
    ce: "section-a8a3a0ad"
    id: "biography"
    As: "section-7668f1bc"
  - block: "markdown"
    content:
      title: "Research"
      subtitle: ""
      text: |-
        I work on data-driven and LLM-assisted intelligence for complex
        industrial processes, with a particular focus on metallurgy, process
        decision support, adaptive prediction, and industrial time-series
        modeling.
    design:
      columns: "1"
    ce: "section-7fbe6595"
    id: "research"
    As: "section-f89358aa"
  - block: "collection"
    content:
      title: "Selected Publications"
      filters:
        folders:
          - "publications"
        featured_only: true
    design:
      view: "article-grid"
      columns: 3
    ce: "section-papers"
    id: "papers"
    As: "section-5847d5ef"
  - block: "collection"
    content:
      title: "Publications"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: false
      count: 5
      sort_by: "Date"
      archive:
        enable: true
      order: "desc"
    design:
      view: "citation"
      fill_image: true
    ce: "section-2dca0dee"
    id: "publications"
    As: "section-1a3c413c"
---
