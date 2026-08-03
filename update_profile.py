import os

def build_profile():
    COLORS = {
        'bg': '#050816',
        'primary': '#7C3AED',
        'secondary': '#2563EB',
        'accent': '#38BDF8',
        'text': '#F8FAFC',
        'muted': '#94A3B8',
        'card_bg': 'rgba(255,255,255,0.03)',
        'card_border': 'rgba(255,255,255,0.08)',
    }

    def create_svg(filename, content, width, height):
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&amp;display=swap');
      * {{ font-family: 'Inter', -apple-system, sans-serif; }}
      .bg {{ fill: {COLORS['bg']}; }}
      .card {{ fill: {COLORS['card_bg']}; stroke: {COLORS['card_border']}; stroke-width: 1px; rx: 16px; }}
      .text-title {{ font-size: 32px; font-weight: 800; fill: {COLORS['text']}; }}
      .text-h2 {{ font-size: 24px; font-weight: 700; fill: {COLORS['text']}; }}
      .text-p {{ font-size: 15px; font-weight: 400; fill: {COLORS['muted']}; line-height: 1.5; }}
      .text-sm {{ font-size: 13px; font-weight: 400; fill: {COLORS['muted']}; }}
      .highlight {{ fill: {COLORS['accent']}; font-weight: 600; }}
      .badge {{ fill: rgba(56, 189, 248, 0.1); stroke: rgba(56, 189, 248, 0.3); stroke-width: 1px; rx: 6px; }}
      .badge-text {{ font-size: 12px; font-weight: 600; fill: {COLORS['accent']}; }}
    </style>
  </defs>
  {content}
</svg>'''
        with open(f'assets/{filename}', 'w', encoding='utf-8') as f:
            f.write(svg)

    about_content = '''
  <rect class="bg" width="100%" height="100%"/>
  <rect class="card" x="20" y="20" width="760" height="280"/>
  <text class="text-h2" x="60" y="75">Engineer first. Researcher by discipline.</text>
  <text class="text-p" x="60" y="120">I'm <tspan fill="#F8FAFC" font-weight="600">D. Devanandu</tspan>, an AI &amp; Machine Learning Engineer from India, working at the intersection</text>
  <text class="text-p" x="60" y="145">of scientific research and production-grade software engineering. I don't build CRUD apps</text>
  <text class="text-p" x="60" y="170">— I build systems that reason, retrieve, simulate, and optimize.</text>
  
  <text class="text-p" x="60" y="210">My work spans <tspan fill="#F8FAFC" font-weight="600">Scientific Machine Learning</tspan>, autonomous agents, and LLM infrastructure,</text>
  <text class="text-p" x="60" y="235">always held to the same engineering bar: clean architecture and async-first design.</text>
  <text class="text-p" x="60" y="260">Currently preparing for a Master's in Artificial Intelligence in Germany.</text>
'''
    create_svg('about.svg', about_content, 800, 320)

    # Experience & Education SVG
    exp_content = '''
  <rect class="bg" width="100%" height="100%"/>
  <rect class="card" x="20" y="20" width="370" height="300"/>
  <text class="text-h2" x="40" y="60" font-size="20">Experience</text>
  <g transform="translate(40, 90)">
    <circle cx="0" cy="5" r="4" fill="#2563EB"/>
    <text class="text-sm" x="15" y="10" fill="#38BDF8" font-family="monospace">2025 - Present</text>
    <text class="text-p" x="15" y="30" fill="#F8FAFC" font-weight="600">Independent AI Engineer</text>
    
    <circle cx="0" cy="75" r="4" fill="#2563EB"/>
    <text class="text-sm" x="15" y="80" fill="#38BDF8" font-family="monospace">2024 - 2025</text>
    <text class="text-p" x="15" y="100" fill="#F8FAFC" font-weight="600">Applied ML Projects</text>
    
    <circle cx="0" cy="145" r="4" fill="#2563EB"/>
    <text class="text-sm" x="15" y="150" fill="#38BDF8" font-family="monospace">2023 - 2024</text>
    <text class="text-p" x="15" y="170" fill="#F8FAFC" font-weight="600">Backend Engineering</text>
  </g>

  <rect class="card" x="410" y="20" width="370" height="300"/>
  <text class="text-h2" x="430" y="60" font-size="20">Education</text>
  <g transform="translate(430, 90)">
    <circle cx="0" cy="5" r="4" fill="#7C3AED"/>
    <text class="text-sm" x="15" y="10" fill="#38BDF8" font-family="monospace">Planned</text>
    <text class="text-p" x="15" y="30" fill="#F8FAFC" font-weight="600">M.Sc. Artificial Intelligence</text>
    <text class="text-p" x="15" y="55" font-size="14">Germany</text>
    
    <circle cx="0" cy="105" r="4" fill="#7C3AED"/>
    <text class="text-sm" x="15" y="110" fill="#38BDF8" font-family="monospace">In Progress</text>
    <text class="text-p" x="15" y="130" fill="#F8FAFC" font-weight="600">B.Tech / B.Sc.</text>
    <text class="text-p" x="15" y="155" font-size="14">AI &amp; Machine Learning</text>
  </g>
'''
    create_svg('exp_edu.svg', exp_content, 800, 340)

    # Focus
    focus_items = [
        ("AGENTS", "Autonomous AI Agents"), ("PINN", "Physics-Informed NNs"),
        ("SCI-ML", "Scientific Machine Learning"), ("RL", "Reinforcement Learning"),
        ("RAG", "Retrieval-Augmented Gen"), ("LLM", "Large Language Models"),
        ("BACKEND", "Backend Architecture"), ("DIST", "Distributed AI Systems")
    ]
    focus_content = '<rect class="bg" width="100%" height="100%"/>\n'
    for i, (tag, item) in enumerate(focus_items):
        x = 20 + (i % 4) * 190
        y = 20 + (i // 4) * 90
        focus_content += f'<rect class="card" x="{x}" y="{y}" width="180" height="75"/>\n'
        focus_content += f'<text class="text-sm" x="{x+90}" y="{y+30}" text-anchor="middle" font-family="monospace" fill="#38BDF8" font-size="11">{tag}</text>\n'
        focus_content += f'<text class="text-p" x="{x+90}" y="{y+55}" text-anchor="middle" font-weight="600" fill="#F8FAFC" font-size="13">{item}</text>\n'
    create_svg('focus.svg', focus_content, 800, 220)

    # Philosophy
    phil_items = ["Clean Architecture", "Scalability", "Security", "Testing", "CI/CD", "Docker", "Observability", "Prod Readiness"]
    phil_content = '<rect class="bg" width="100%" height="100%"/>\n'
    for i, item in enumerate(phil_items):
        x = 20 + (i % 4) * 190
        y = 20 + (i // 4) * 60
        phil_content += f'<rect class="card" x="{x}" y="{y}" width="180" height="45"/>\n'
        phil_content += f'<text class="text-sm" x="{x+90}" y="{y+28}" text-anchor="middle" font-weight="600" fill="#38BDF8" font-size="13">{item}</text>\n'
    create_svg('philosophy.svg', phil_content, 800, 160)

    # Projects
    projects = [
        {"title": "Benefits & Bureaucracy Navigator", "desc": "Flagship enterprise-grade AI platform using autonomous agents.", "arch": "LLM, RAG, Async FastAPI", "tech": "Python, Docker, Postgres", "status": "Active"},
        {"title": "DreamScape AI", "desc": "Cinematic AI storytelling platform generating multimedia narratives.", "arch": "Celery Orchestration", "tech": "FastAPI, Gemini, Supabase", "status": "Live"},
        {"title": "ResearchMind AI", "desc": "RAG-powered research assistant for deep PDF understanding.", "arch": "Semantic Search, Vector DB", "tech": "LangChain, Gemini", "status": "Live"},
        {"title": "TrafficMind AI", "desc": "Smart-city platform optimizing traffic using PINNs & Deep RL.", "arch": "PINNs, Deep RL, SUMO", "tech": "Python, Reinforcement Learning", "status": "Research"}
    ]
    for i, p in enumerate(projects):
        p_content = f'''
  <rect class="bg" width="100%" height="100%"/>
  <rect class="card" x="10" y="10" width="370" height="220" style="transition: all 0.3s ease;"/>
  <text class="text-h2" x="30" y="50" font-size="18">{p['title']}</text>
  <text class="text-p" x="30" y="80" font-size="13.5">{p['desc']}</text>
  
  <text class="text-sm" x="30" y="130" fill="#7C3AED" font-weight="600">Architecture</text>
  <text class="text-sm" x="130" y="130">{p['arch']}</text>
  
  <text class="text-sm" x="30" y="160" fill="#7C3AED" font-weight="600">Tech Stack</text>
  <text class="text-sm" x="130" y="160">{p['tech']}</text>
  
  <text class="text-sm" x="30" y="190" fill="#7C3AED" font-weight="600">Status</text>
  <text class="text-sm" x="130" y="190">{p['status']}</text>
  
  <g transform="translate(340, 42)">
     <circle cx="0" cy="0" r="14" fill="rgba(255,255,255,0.05)"/>
     <path d="M-3,-4 L3,0 L-3,4" fill="none" stroke="#38BDF8" stroke-width="2"/>
  </g>
  '''
        create_svg(f'project_{i+1}.svg', p_content, 390, 240)

    # Button SVG for "View Interactive Profile"
    btn_content = '''
  <rect width="100%" height="100%" fill="#050816"/>
  <rect x="200" y="20" width="400" height="60" rx="30" fill="url(#btnGrad)" stroke="#38BDF8" stroke-width="1.5" style="filter: drop-shadow(0px 4px 12px rgba(56, 189, 248, 0.4));"/>
  <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#2563EB" stop-opacity="0.8"/>
  </linearGradient>
  <text x="400" y="56" text-anchor="middle" font-size="15" font-weight="700" fill="#F8FAFC" font-family="-apple-system, sans-serif" letter-spacing="1.5px">VIEW INTERACTIVE PORTFOLIO ↗</text>
'''
    create_svg('interactive_btn.svg', btn_content, 800, 100)

    # Readme Update
    readme_content = '''<div align="center">
  <img src="assets/hero.svg" width="100%" alt="Devadn11206 - AI Engineer & Researcher" />
</div>

<div align="center">
  <a href="https://devadn11206.github.io/Devadn11206/">
    <img src="assets/interactive_btn.svg" width="100%" alt="View Interactive Portfolio" />
  </a>
</div>

<div align="center">
  <img src="assets/about.svg" width="100%" alt="About Me" />
</div>

<div align="center">
  <h2 align="center">Current Focus</h2>
  <img src="assets/focus.svg" width="100%" alt="Current Focus" />
</div>

<div align="center">
  <h2 align="center">Engineering Philosophy</h2>
  <img src="assets/philosophy.svg" width="100%" alt="Engineering Philosophy" />
</div>

<h2 align="center">Featured Projects</h2>
<div align="center">
  <a href="https://github.com/Devadn11206/Benefits-Bureaucracy-Navigator"><img src="assets/project_1.svg" width="49%" /></a>
  <a href="https://github.com/Devadn11206/DreamScape-AI"><img src="assets/project_2.svg" width="49%" /></a>
  <br>
  <a href="https://github.com/Devadn11206/ResearchMind-AI"><img src="assets/project_3.svg" width="49%" /></a>
  <a href="https://github.com/Devadn11206/TrafficMind-AI"><img src="assets/project_4.svg" width="49%" /></a>
</div>

<div align="center">
  <img src="assets/exp_edu.svg" width="100%" alt="Experience and Education" />
</div>

<div align="center">
  <img src="assets/architecture.svg" width="100%" alt="Architecture" />
</div>

<div align="center">
  <img src="assets/tech_stack.svg" width="100%" alt="Tech Stack" />
</div>

<h2 align="center">Analytics & Activity</h2>
<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Devadn11206&theme=radical&show_icons=true&hide_border=true&bg_color=050816&title_color=7C3AED&text_color=94A3B8&icon_color=38BDF8" width="49%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Devadn11206&theme=radical&hide_border=true&background=050816&ring=7C3AED&fire=38BDF8&currStreakLabel=94A3B8" width="49%" />
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake.svg">
  </picture>
</div>

<div align="center">
  <a href="https://linkedin.com/in/Devadn11206"><img src="assets/contact_linkedin.svg" width="24%" /></a>
  <a href="mailto:contact@example.com"><img src="assets/contact_email.svg" width="24%" /></a>
  <a href="https://github.com/Devadn11206"><img src="assets/contact_portfolio.svg" width="24%" /></a>
  <a href="https://scholar.google.com/"><img src="assets/contact_scholar.svg" width="24%" /></a>
</div>
'''
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == '__main__':
    build_profile()
