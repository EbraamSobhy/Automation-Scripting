from pathlib import Path

ROOT = Path("VitePress")
DOCS = ROOT / "docs"
VP = DOCS / ".vitepress"
THEME = VP / "theme"

files = {
    ROOT / "package.json": """{
  "private": true,
  "devDependencies": {
    "vitepress": "^2.0.0-alpha.15"
  },
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  }
}
""",

    DOCS / "index.md": """# Welcome

This is the home page of **My Docs** 🚀
""",

    DOCS / "guide.md": """# Guide

## Getting Started

This is the guide page.
""",

    VP / "config.js": """export default {
  title: "My Docs",
  description: "VitePress documentation",
  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Guide", link: "/guide" }
    ]
  }
}
""",

    THEME / "custom.css": """:root {
  --vp-c-bg: #000000;
  --vp-c-bg-alt: #000000;
  --vp-c-bg-soft: #000000;
}

html.dark,
.VPContent {
  background-color: #000000;
}

/* Code blocks */
.vp-code-group,
div[class*='language-'] {
  border: 1px solid #ffffff;
  border-radius: 8px;
  background-color: #000000;
}

/* Inline code */
code {
  border: 1px solid #ffffff;
  padding: 2px 6px;
  border-radius: 4px;
}

/* Navbar */
.VPNav {
  border-bottom: 1px solid #ffffff;
}
""",

    THEME / "index.js": """import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default DefaultTheme
"""
}

# Create files
for path, content in files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"✔ Created {path}")

print("\nVitePress documentation scaffolded successfully!")
print("👉 Run:")
print("   cd my-docs")
print("   npm install")
print("   npm run docs:dev")