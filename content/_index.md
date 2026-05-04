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
        My recent work includes LLM-driven human-AI collaborative decision
        support for metallurgical processes, adaptive temperature trend
        prediction in ladle preheating, random-forest-based pressure prediction
        for manufacturing, blast furnace iron-tapping state recognition, and
        data-driven analysis of continuous casting and metallurgical processes.
      button:
        text: "CV"
        url: "uploads/resume.pdf"
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
    As: "section-f89358aa"
  - block: "collection"
    content:
      title: "Featured Publications"
      filters:
        folders:
          - "publications"
        featured_only: true
    design:
      view: "article-grid"
      columns: 2
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
    design:
      view: "citation"
    ce: "section-2dca0dee"
    As: "section-1a3c413c"
  - block: "collection"
    content:
      title: "Projects"
      text: "Project details will be added after the project list is confirmed."
      filters:
        folders:
          - "projects"
    design:
      view: "article-grid"
      columns: 3
    ce: "section-projects"
    id: "projects"
    As: "section-38490b7a"
  - block: "collection"
    content:
      title: "Blog"
      subtitle: ""
      text: "Blog posts will be added later."
      page_type: "blog"
      count: 6
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: "desc"
    design:
      view: "card"
      spacing:
        padding:
          - 0
          - 0
          - 0
          - 0
    ce: "section-news"
    id: "news"
    As: "section-9908f258"
---
