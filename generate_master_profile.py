import os

def generate_svgs():
    os.makedirs('assets', exist_ok=True)

    COLORS = {
        'bg': '#050816',
        'bg_sec': '#0B1120',
        'primary': '#7C3AED',
        'secondary': '#2563EB',
        'highlight': '#22D3EE',
        'success': '#10B981',
        'warning': '#F59E0B',
        'text': '#F8FAFC',
        'text_sec': '#CBD5E1',
        'text_mut': '#94A3B8',
        'card': 'rgba(255,255,255,0.03)',
        'card_border': 'rgba(255,255,255,0.08)',
    }

    DEFS = f"""
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&amp;family=Inter:wght@300;400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap');
      * {{ box-sizing: border-box; }}
      .font-display {{ font-family: 'Space Grotesk', sans-serif; }}
      .font-body {{ font-family: 'Inter', sans-serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      
      @keyframes float1 {{ 0% {{ transform: translate(0, 0); }} 50% {{ transform: translate(20px, -20px); }} 100% {{ transform: translate(0, 0); }} }}
      @keyframes float2 {{ 0% {{ transform: translate(0, 0); }} 50% {{ transform: translate(-20px, 20px); }} 100% {{ transform: translate(0, 0); }} }}
      @keyframes float3 {{ 0% {{ transform: translate(0, 0) scale(1); }} 50% {{ transform: translate(15px, 15px) scale(1.05); }} 100% {{ transform: translate(0, 0) scale(1); }} }}
      
      .aurora-1 {{ animation: float1 15s ease-in-out infinite; }}
      .aurora-2 {{ animation: float2 20s ease-in-out infinite; }}
      .aurora-3 {{ animation: float3 25s ease-in-out infinite; }}
      
      .glass-card {{ fill: {COLORS['card']}; stroke: {COLORS['card_border']}; stroke-width: 1px; rx: 16px; }}
      .pill {{ fill: rgba(124, 58, 237, 0.1); stroke: rgba(124, 58, 237, 0.3); stroke-width: 1px; rx: 100px; }}
      .pill-text {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; fill: {COLORS['highlight']}; font-weight: 500; }}
      
      .h1 {{ font-family: 'Space Grotesk', sans-serif; font-size: 64px; font-weight: 700; fill: url(#textGrad); letter-spacing: -1px; }}
      .h2 {{ font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 600; fill: {COLORS['text']}; }}
      .h3 {{ font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 600; fill: {COLORS['text']}; }}
      .p {{ font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 400; fill: {COLORS['text_sec']}; line-height: 1.6; }}
      .p-mut {{ font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 400; fill: {COLORS['text_mut']}; }}
      .mono-sm {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: {COLORS['text_mut']}; letter-spacing: 1px; }}
      
      .node {{ fill: rgba(34, 211, 238, 0.8); }}
      .edge {{ stroke: rgba(124, 58, 237, 0.2); stroke-width: 1px; }}
    </style>
    
    <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(124, 58, 237, 0.05)" stroke-width="1"/>
    </pattern>

    <radialGradient id="aurora1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{COLORS['primary']}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{COLORS['bg']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="aurora2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{COLORS['secondary']}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{COLORS['bg']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="aurora3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{COLORS['highlight']}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{COLORS['bg']}" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#CBD5E1"/>
    </linearGradient>
    
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLORS['primary']}"/>
      <stop offset="100%" stop-color="{COLORS['highlight']}"/>
    </linearGradient>
  </defs>
"""

    def create_svg(filename, content, width=1000, height=400):
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
{DEFS}
  <!-- Background -->
  <rect width="100%" height="100%" fill="{COLORS['bg']}"/>
  <rect width="100%" height="100%" fill="url(#grid)"/>
  
  <!-- Auroras -->
  <circle cx="10%" cy="20%" r="400" fill="url(#aurora1)" class="aurora-1" />
  <circle cx="90%" cy="80%" r="500" fill="url(#aurora2)" class="aurora-2" />
  <circle cx="50%" cy="50%" r="300" fill="url(#aurora3)" class="aurora-3" />

  {content}
</svg>'''
        with open(f'assets/{filename}', 'w', encoding='utf-8') as f:
            f.write(svg)

    # 1. HERO
    hero_nodes = ""
    import random
    random.seed(42)
    pts = [(random.randint(0, 1000), random.randint(0, 500)) for _ in range(40)]
    for p1 in pts:
        for p2 in pts:
            if (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 < 15000:
                hero_nodes += f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" class="edge"/>\n'
    for p in pts:
        hero_nodes += f'<circle cx="{p[0]}" cy="{p[1]}" r="2" class="node"/>\n'

    hero_content = f"""
  {hero_nodes}
  <g transform="translate(500, 220)" text-anchor="middle">
    <rect x="-170" y="-140" width="340" height="28" class="pill"/>
    <text x="0" y="-121" class="pill-text">AI RESEARCH &amp; PRODUCTION ENGINEERING</text>
    
    <text x="0" y="-40" class="h1">D. DEVA NANDU</text>
    <text x="0" y="10" class="font-display" font-size="22" font-weight="500" fill="{COLORS['highlight']}" letter-spacing="2px">ARTIFICIAL INTELLIGENCE ENGINEER</text>
    <text x="0" y="50" class="p" fill="{COLORS['text_sec']}">Building Intelligent Systems Through Research and Engineering</text>
    
    <g transform="translate(-160, 100)">
      <rect x="0" y="0" width="140" height="44" rx="22" fill="url(#primaryGrad)"/>
      <text x="70" y="26" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="#fff">View Projects →</text>
    </g>
    <g transform="translate(20, 100)">
      <rect x="0" y="0" width="140" height="44" rx="22" fill="{COLORS['card']}" stroke="{COLORS['card_border']}"/>
      <text x="70" y="26" text-anchor="middle" font-family="Inter" font-size="14" font-weight="600" fill="{COLORS['text']}">Research</text>
    </g>
  </g>
"""
    create_svg('premium_hero.svg', hero_content, 1000, 500)

    # 2. ABOUT & MISSION
    about_content = f"""
  <rect x="40" y="40" width="920" height="320" class="glass-card"/>
  
  <g transform="translate(90, 100)">
    <text x="0" y="0" class="mono-sm" fill="{COLORS['highlight']}">01 // MISSION</text>
    <text x="0" y="45" class="h2">Engineer first. Researcher by discipline.</text>
    
    <text x="0" y="90" class="p">I build intelligent software that combines research, engineering, and scalable</text>
    <text x="0" y="115" class="p">system design. I am not interested in building generic CRUD applications.</text>
    <text x="0" y="140" class="p">I focus on solving real-world problems using <tspan fill="{COLORS['text']}" font-weight="600">Scientific Machine Learning,</tspan></text>
    <text x="0" y="165" class="p"><tspan fill="{COLORS['text']}" font-weight="600">Autonomous Agents</tspan>, and <tspan fill="{COLORS['text']}" font-weight="600">Large Language Models.</tspan></text>
    
    <text x="0" y="210" class="p-mut">Preparing for M.Sc. in Artificial Intelligence in Germany.</text>
  </g>
  
  <g transform="translate(650, 100)">
    <rect x="0" y="15" width="220" height="1" fill="{COLORS['card_border']}"/>
    <text x="0" y="40" class="mono-sm" fill="{COLORS['text_sec']}">FOCUS AREAS</text>
    <text x="0" y="70" class="p-mut">• Deep Reinforcement Learning</text>
    <text x="0" y="100" class="p-mut">• Physics-Informed NNs</text>
    <text x="0" y="130" class="p-mut">• AI Agents &amp; RAG</text>
    <text x="0" y="160" class="p-mut">• Distributed AI Systems</text>
    <text x="0" y="190" class="p-mut">• Backend &amp; FastAPI</text>
  </g>
"""
    create_svg('premium_about.svg', about_content, 1000, 400)

    # 3. FEATURED PROJECTS
    def draw_score(label, score, y):
        w = score * 1.5
        return f'''
        <text x="0" y="{y}" class="mono-sm" font-size="10">{label}</text>
        <rect x="120" y="{y-8}" width="150" height="4" rx="2" fill="{COLORS['card_border']}"/>
        <rect x="120" y="{y-8}" width="{w}" height="4" rx="2" fill="url(#primaryGrad)"/>
        <text x="285" y="{y}" class="mono-sm" font-size="10" fill="{COLORS['highlight']}">{score}/100</text>
        '''

    proj_content = f"""
  <text x="40" y="60" class="mono-sm" fill="{COLORS['highlight']}">02 // ENGINEERING SHOWCASE</text>
  <text x="40" y="105" class="h2">Featured Projects</text>
  
  <!-- Project 1: BBN -->
  <rect x="40" y="140" width="920" height="340" class="glass-card"/>
  <g transform="translate(80, 190)">
    <rect x="0" y="-15" width="220" height="24" class="pill"/>
    <text x="110" y="1" class="pill-text" text-anchor="middle">FLAGSHIP — KNOWLEDGE BASE PHASE</text>
    
    <text x="0" y="50" class="h2">Benefits &amp; Bureaucracy Navigator</text>
    <text x="0" y="90" class="p">An enterprise-grade AI platform designed to simplify public services,</text>
    <text x="0" y="115" class="p">benefits, documentation, and bureaucracy using autonomous AI agents.</text>
    
    <text x="0" y="160" class="mono-sm" fill="{COLORS['primary']}">TECH STACK</text>
    <text x="0" y="185" class="p-mut">FastAPI, Python, Async SQLAlchemy, Alembic, Docker, PostgreSQL, Pydantic</text>
    
    <text x="0" y="225" class="mono-sm" fill="{COLORS['primary']}">ARCHITECTURE</text>
    <text x="0" y="250" class="p-mut">Repository Pattern • Dependency Injection • Clean Architecture • SOLID</text>
  </g>
  <g transform="translate(600, 180)">
    <text x="0" y="0" class="font-display" font-size="16" font-weight="600" fill="{COLORS['text']}">Engineering Quality Matrix</text>
    {draw_score("Architecture", 95, 30)}
    {draw_score("Scalability", 95, 55)}
    {draw_score("Maintainability", 95, 80)}
    {draw_score("Testing", 95, 105)}
    {draw_score("Documentation", 100, 130)}
    {draw_score("AI Readiness", 95, 155)}
    {draw_score("Production", 85, 180)}
  </g>

  <!-- Project 2 & 3: Side by side -->
  <rect x="40" y="510" width="450" height="280" class="glass-card"/>
  <g transform="translate(70, 560)">
    <text x="0" y="0" class="mono-sm" fill="{COLORS['highlight']}">GENERATIVE AI</text>
    <text x="0" y="35" class="h3">DreamScape AI</text>
    <text x="0" y="65" class="p" font-size="14">Cinematic AI storytelling platform generating</text>
    <text x="0" y="85" class="p" font-size="14">narratives, images, and text-to-speech.</text>
    <rect x="0" y="110" width="390" height="1" fill="{COLORS['card_border']}"/>
    <text x="0" y="140" class="mono-sm">STACK</text>
    <text x="0" y="165" class="p-mut" font-size="13">FastAPI, Gemini, Celery, Redis, Supabase, Docker</text>
    <text x="0" y="200" class="mono-sm">ORCHESTRATION</text>
    <text x="0" y="225" class="p-mut" font-size="13">Async Task Queues for long-running generation</text>
  </g>

  <rect x="510" y="510" width="450" height="280" class="glass-card"/>
  <g transform="translate(540, 560)">
    <text x="0" y="0" class="mono-sm" fill="{COLORS['highlight']}">RETRIEVAL &amp; NLP</text>
    <text x="0" y="35" class="h3">ResearchMind AI</text>
    <text x="0" y="65" class="p" font-size="14">AI-powered research assistant built using</text>
    <text x="0" y="85" class="p" font-size="14">Retrieval-Augmented Generation over PDFs.</text>
    <rect x="0" y="110" width="390" height="1" fill="{COLORS['card_border']}"/>
    <text x="0" y="140" class="mono-sm">STACK</text>
    <text x="0" y="165" class="p-mut" font-size="13">LangChain, Vector DB, Semantic Embeddings</text>
    <text x="0" y="200" class="mono-sm">ARCHITECTURE</text>
    <text x="0" y="225" class="p-mut" font-size="13">Chunked indexing, semantic search, grounded Q&amp;A</text>
  </g>
  
  <!-- Project 4: TrafficMind -->
  <rect x="40" y="820" width="920" height="200" class="glass-card"/>
  <g transform="translate(80, 870)">
    <text x="0" y="0" class="mono-sm" fill="{COLORS['highlight']}">SCIENTIFIC MACHINE LEARNING &amp; RL</text>
    <text x="0" y="35" class="h3">TrafficMind AI — Smart City Platform</text>
    <text x="0" y="65" class="p" font-size="14">Predicting traffic flow and optimizing signal control by combining Deep Reinforcement</text>
    <text x="0" y="85" class="p" font-size="14">Learning, Physics-Informed Neural Networks, and SUMO Traffic Simulation.</text>
    
    <rect x="0" y="125" width="84" height="24" class="pill"/>
    <text x="42" y="141" class="pill-text" text-anchor="middle">Deep RL</text>
    <rect x="94" y="125" width="70" height="24" class="pill"/>
    <text x="129" y="141" class="pill-text" text-anchor="middle">PINNs</text>
    <rect x="174" y="125" width="60" height="24" class="pill"/>
    <text x="204" y="141" class="pill-text" text-anchor="middle">SUMO</text>
    <rect x="244" y="125" width="190" height="24" class="pill"/>
    <text x="339" y="141" class="pill-text" text-anchor="middle">Ant Colony Optimization</text>
  </g>
"""
    create_svg('premium_projects.svg', proj_content, 1000, 1060)

    # 4. SKILLS & PHILOSOPHY
    skills_content = f"""
  <text x="40" y="60" class="mono-sm" fill="{COLORS['highlight']}">03 // CAPABILITIES &amp; PRINCIPLES</text>
  <text x="40" y="105" class="h2">Technology &amp; Philosophy</text>
  
  <rect x="40" y="140" width="450" height="400" class="glass-card"/>
  <g transform="translate(80, 190)">
    <text x="0" y="0" class="h3">Engineering Principles</text>
    <text x="0" y="30" class="p-mut">Standards I apply to every system I build.</text>
    
    <g transform="translate(0, 60)">
      <path d="M 0 10 L 15 25 L 0 40" fill="none" stroke="{COLORS['primary']}" stroke-width="2"/>
      <text x="30" y="22" class="p" fill="{COLORS['text']}" font-weight="600">Clean Architecture &amp; SOLID</text>
      <text x="30" y="42" class="p-mut" font-size="13">Domain logic isolated from infrastructure.</text>
      
      <path d="M 0 80 L 15 95 L 0 110" fill="none" stroke="{COLORS['highlight']}" stroke-width="2"/>
      <text x="30" y="92" class="p" fill="{COLORS['text']}" font-weight="600">Scalability &amp; Maintainability</text>
      <text x="30" y="112" class="p-mut" font-size="13">Async-first design, built for future developers.</text>
      
      <path d="M 0 150 L 15 165 L 0 180" fill="none" stroke="{COLORS['success']}" stroke-width="2"/>
      <text x="30" y="162" class="p" fill="{COLORS['text']}" font-weight="600">Testing &amp; CI/CD</text>
      <text x="30" y="182" class="p-mut" font-size="13">Automated pipelines and rigorous test coverage.</text>
      
      <path d="M 0 220 L 15 235 L 0 250" fill="none" stroke="{COLORS['secondary']}" stroke-width="2"/>
      <text x="30" y="232" class="p" fill="{COLORS['text']}" font-weight="600">Observability &amp; Docker</text>
      <text x="30" y="252" class="p-mut" font-size="13">Reproducible environments with structured logging.</text>
    </g>
  </g>

  <rect x="510" y="140" width="450" height="400" class="glass-card"/>
  <g transform="translate(550, 190)">
    <text x="0" y="0" class="h3">Technology Stack</text>
    <text x="0" y="30" class="p-mut">Tools I use in research and production.</text>
    
    <g transform="translate(0, 60)">
      <text x="0" y="15" class="mono-sm" fill="{COLORS['primary']}">AI / ML</text>
      <text x="0" y="40" class="p">PyTorch, TensorFlow, Scikit-learn, LangChain</text>
      <text x="0" y="60" class="p">Transformers, OpenCV, NumPy, Pandas</text>
      <rect x="0" y="80" width="370" height="1" fill="{COLORS['card_border']}"/>
      
      <text x="0" y="115" class="mono-sm" fill="{COLORS['primary']}">BACKEND</text>
      <text x="0" y="140" class="p">FastAPI, Python, SQLAlchemy, Alembic</text>
      <text x="0" y="160" class="p">Redis, Celery</text>
      <rect x="0" y="180" width="370" height="1" fill="{COLORS['card_border']}"/>
      
      <text x="0" y="215" class="mono-sm" fill="{COLORS['primary']}">INFRA &amp; DATA</text>
      <text x="0" y="240" class="p">Docker, GitHub Actions, CI/CD, AWS</text>
      <text x="0" y="260" class="p">PostgreSQL, SQLite, Vector Databases</text>
    </g>
  </g>
"""
    create_svg('premium_skills.svg', skills_content, 1000, 600)

    # 5. CONTACT & FOOTER
    footer_content = f"""
  <rect x="40" y="40" width="920" height="240" class="glass-card"/>
  <g transform="translate(500, 120)" text-anchor="middle">
    <text x="0" y="-10" class="h2">Let's build intelligent systems.</text>
    <text x="0" y="25" class="p-mut">Open to research collaborations, AI engineering roles, and open source.</text>
    
    <g transform="translate(-160, 60)">
      <rect x="0" y="0" width="320" height="1" fill="{COLORS['card_border']}"/>
      <text x="0" y="40" class="mono-sm" fill="{COLORS['text']}">github.com/Devadn11206</text>
      <text x="320" y="40" class="mono-sm" text-anchor="end" fill="{COLORS['highlight']}">[ LINKEDIN ] [ RESUME ]</text>
    </g>
  </g>
"""
    create_svg('premium_footer.svg', footer_content, 1000, 320)

    # Generate README.md
    readme = f"""<div align="center">
  <img src="assets/premium_hero.svg" width="100%" alt="Hero" />
</div>

<div align="center">
  <a href="https://devadn11206.github.io/Devadn11206/">
    <img src="assets/interactive_btn.svg" width="100%" alt="View Interactive Portfolio" />
  </a>
</div>

<div align="center">
  <img src="assets/premium_about.svg" width="100%" alt="About & Mission" />
</div>

<div align="center">
  <img src="assets/premium_projects.svg" width="100%" alt="Featured Projects" />
</div>

<div align="center">
  <img src="assets/premium_skills.svg" width="100%" alt="Skills & Philosophy" />
</div>

<h2 align="center">Analytics & Activity</h2>
<div align="center">
  <img src="assets/premium_github.svg" width="100%" alt="GitHub Analytics" />
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Devadn11206/Devadn11206/output/github-contribution-grid-snake.svg">
  </picture>
</div>

<div align="center">
  <img src="assets/premium_footer.svg" width="100%" alt="Contact" />
</div>
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

if __name__ == '__main__':
    generate_svgs()
