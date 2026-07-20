# AGENTS.md

本仓库是基于 HugoBlox Academic CV 模板、通过 GitHub Pages 发布的个人学术主页。维护时应将其视为内容与配置驱动的 Hugo 静态网站。

## 维护边界

- 优先使用 Hugo/HugoBlox 官方支持的 Markdown、YAML 和静态资源配置。
- 站点设置与导航位于 `config/_default/`，首页位于 `content/_index.md`，作者信息位于 `data/authors/`，论文和项目内容位于 `content/`，公开文件位于 `static/`。
- 不要手动编辑构建产物 `public/`，也不要直接修改 HugoBlox 模块、主题源码或已编译的 CSS/JavaScript。
- 只有官方配置无法实现目标时，才考虑 CSS、`layouts/` 覆盖、hook、构建脚本或依赖修改；实施前必须说明原因和影响，并征得用户同意。

## 内容要求

- 首页只展示真实、完整的内容；没有内容的栏目应从首页和导航栏隐藏，不使用占位文案。
- 个人简介和研究内容应保持简洁、准确、学术化，避免宣传口吻、产品化措辞和明显的 AI 写作痕迹。
- 论文元数据与 BibTeX 分别维护在 `content/publications/*/index.md` 和对应目录的 `cite.bib` 中。

## CV 与验证

每次 git 提交前同步最新 CV：

```bash
rsync -av /home/zongyoucheng/Code/0LaTeX/0简历/out/CV.pdf static/cv.pdf
```

修改后按影响范围运行 `pnpm run build` 和 `git diff --check`；不要通过修改 `public/` 修复构建结果。
