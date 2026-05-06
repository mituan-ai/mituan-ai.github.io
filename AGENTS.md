# AGENTS.md

本仓库是一个基于 HugoBlox Academic CV 模板的个人学术主页，并通过 GitHub Pages 发布。维护本项目时，应把它当作“内容与配置驱动”的 Hugo 静态网站，而不是普通应用代码库，也不是必须依赖可视化 CMS 的项目。

## 核心原则

优先修改 Hugo/HugoBlox 官方推荐的内容层和配置层。只有当目标功能无法通过 Markdown、YAML、`static/` 静态资源或官方配置项完成时，才考虑修改模板、partial、hook、CSS 或构建逻辑。

如果确实必须修改更底层的代码，应做到最小侵入，并说明为什么常规内容/配置入口无法满足需求。

## 优先修改位置

常见修改应优先落在以下位置：

- 导航栏菜单：`config/_default/menus.yaml`
- 站点标题、基础 Hugo 设置：`config/_default/hugo.yaml`
- HugoBlox 参数、品牌、页面行为：`config/_default/params.yaml`
- 语言配置：`config/_default/languages.yaml`
- 首页区块、顺序和展示内容：`content/_index.md`
- 作者和个人主页信息：`data/authors/*.yaml`
- 论文条目：`content/publications/*/index.md`
- 论文 BibTeX：对应论文目录下的 `cite.bib`
- 可公开下载的 PDF、CV 等静态文件：`static/uploads/`
- 少量项目专属样式微调：`assets/css/custom.css`

不要为了修改网站源内容而手动编辑 `public/`。`public/` 是 Hugo 构建后的输出目录，不是源文件目录。如果希望网站上出现 `/uploads/name.pdf`，应把源文件放到 `static/uploads/name.pdf`，然后重新构建。

## 默认避免修改

除非有明确、必要的理由，默认不要修改以下内容：

- HugoBlox 模块或主题源码
- `public/` 下的生成文件
- 已编译或压缩后的 CSS/JavaScript
- 自定义 `layouts/` 覆盖文件
- 构建脚本和依赖清单
- 可视化 CMS 或编辑器插件配置

如果看到 Ownable、Decap、Netlify CMS、Quarto CMS 等相关内容，不要默认认为它们是网站运行时依赖。应先确认它们是否只是编辑器便利工具，再决定是否保留或修改。

## CV 和静态文件规则

公开 CV 的标准源文件位置是：

`static/uploads/CV.pdf`

导航栏里的 CV 链接应直接指向：

`/uploads/CV.pdf`

不要直接维护 `public/uploads/CV.pdf`。该文件应由 Hugo 在构建时从 `static/uploads/CV.pdf` 自动复制生成。

## 首页内容规则

不要在首页展示空的占位区块。如果 Blog、Projects、Events 或类似栏目暂时没有真实内容，应从首页和导航栏隐藏，而不是展示 “coming later” 或模板占位文案。

个人简介和研究方向应使用简洁、标准的学术表达，避免宣传口吻、产品化措辞和明显 AI 味的空泛表述。

## 修改前判断顺序

处理任何修改请求时，优先按以下顺序判断：

1. 能否只改 `content/`、`data/`、`config/` 或 `static/`？
2. 是否存在 HugoBlox 官方推荐的 YAML/Markdown 配置方式？
3. 是否可以通过 `assets/css/custom.css` 做低风险样式微调？
4. 是否真的需要新增或覆盖 `layouts/`？
5. 是否真的需要修改构建脚本、依赖或主题底层代码？

只有前面的方式都不适合时，才进入后面的、更底层的修改方式。

## 验证方式

修改网站后，优先运行：

```bash
pnpm run build
```

如果本地 `public/` 中可能残留旧页面，导致检查时误判，应运行：

```bash
hugo --minify --cleanDestinationDir && pnpm run pagefind
```

完成前应检查 git 状态，确认真正需要提交的是源文件，而不是无意义的构建产物。
