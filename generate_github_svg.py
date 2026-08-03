import os

def generate_github_svg():
    COLORS = {
        'bg': '#050816',
        'primary': '#7C3AED',
        'secondary': '#2563EB',
        'highlight': '#22D3EE',
        'text': '#F8FAFC',
        'text_sec': '#CBD5E1',
        'text_mut': '#94A3B8',
        'card': 'rgba(255,255,255,0.03)',
        'card_border': 'rgba(255,255,255,0.08)',
    }

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&amp;family=Inter:wght@300;400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap');
      * {{ box-sizing: border-box; }}
      .font-display {{ font-family: 'Space Grotesk', sans-serif; }}
      .glass-card {{ fill: {COLORS['card']}; stroke: {COLORS['card_border']}; stroke-width: 1px; rx: 16px; }}
      .h2 {{ font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 600; fill: {COLORS['text']}; }}
      .h3 {{ font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 600; fill: {COLORS['text']}; }}
      .p {{ font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 400; fill: {COLORS['text_sec']}; }}
      .p-mut {{ font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 400; fill: {COLORS['text_mut']}; }}
      .mono-sm {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: {COLORS['highlight']}; letter-spacing: 1px; }}
      .stat-num {{ font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; fill: {COLORS['text']}; }}
      .lang-dot {{ rx: 4px; ry: 4px; }}
    </style>
    <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(124, 58, 237, 0.05)" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="100%" height="100%" fill="{COLORS['bg']}"/>
  <rect width="100%" height="100%" fill="url(#grid)"/>
  
  <text x="40" y="60" class="mono-sm">04 // OPEN SOURCE</text>
  <text x="40" y="105" class="h2">GitHub Analytics &amp; Activity</text>
  
  <rect x="40" y="140" width="450" height="200" class="glass-card"/>
  <g transform="translate(80, 180)">
    <text x="0" y="0" class="h3">Contributions</text>
    <g transform="translate(0, 45)">
      <text x="0" y="0" class="stat-num">40+</text>
      <text x="0" y="25" class="p-mut">Repositories</text>
    </g>
    <g transform="translate(130, 45)">
      <text x="0" y="0" class="stat-num">120+</text>
      <text x="0" y="25" class="p-mut">Contributions/yr</text>
    </g>
    <g transform="translate(290, 45)">
      <text x="0" y="0" class="stat-num">6</text>
      <text x="0" y="25" class="p-mut">Day Streak</text>
    </g>
    
    <g transform="translate(0, 110)">
      <rect x="0" y="0" width="220" height="8" rx="4" fill="#7C3AED"/>
      <rect x="222" y="0" width="80" height="8" fill="#2563EB"/>
      <rect x="304" y="0" width="45" height="8" fill="#22D3EE"/>
      <rect x="351" y="0" width="20" height="8" rx="4" fill="#94A3B8"/>
      
      <text x="0" y="30" class="p-mut" font-size="11" fill="{COLORS['text_sec']}"><tspan fill="#7C3AED">●</tspan> Python 62%</text>
      <text x="90" y="30" class="p-mut" font-size="11" fill="{COLORS['text_sec']}"><tspan fill="#2563EB">●</tspan> TypeScript 18%</text>
      <text x="195" y="30" class="p-mut" font-size="11" fill="{COLORS['text_sec']}"><tspan fill="#22D3EE">●</tspan> Dockerfile 11%</text>
      <text x="295" y="30" class="p-mut" font-size="11" fill="{COLORS['text_sec']}"><tspan fill="#94A3B8">●</tspan> Other 9%</text>
    </g>
  </g>

  <rect x="510" y="140" width="450" height="200" class="glass-card"/>
  <g transform="translate(540, 180)">
    <text x="0" y="0" class="h3">Pinned Projects</text>
    
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="390" height="40" fill="transparent"/>
      <text x="0" y="15" class="mono-sm" fill="{COLORS['text']}">benefits-bureaucracy-navigator</text>
      <text x="390" y="15" class="mono-sm" fill="{COLORS['text_mut']}" text-anchor="end">Python</text>
      <text x="0" y="35" class="p-mut">Agentic platform for public services &amp; documentation.</text>
      <rect x="0" y="45" width="390" height="1" fill="{COLORS['card_border']}"/>
    </g>
    <g transform="translate(0, 85)">
      <rect x="0" y="0" width="390" height="40" fill="transparent"/>
      <text x="0" y="15" class="mono-sm" fill="{COLORS['text']}">dreamscape-ai</text>
      <text x="390" y="15" class="mono-sm" fill="{COLORS['text_mut']}" text-anchor="end">Python</text>
      <text x="0" y="35" class="p-mut">Cinematic AI storytelling pipeline.</text>
      <rect x="0" y="45" width="390" height="1" fill="{COLORS['card_border']}"/>
    </g>
    <g transform="translate(0, 140)">
      <rect x="0" y="0" width="390" height="40" fill="transparent"/>
      <text x="0" y="15" class="mono-sm" fill="{COLORS['text']}">researchmind-ai</text>
      <text x="390" y="15" class="mono-sm" fill="{COLORS['text_mut']}" text-anchor="end">Python</text>
      <text x="0" y="35" class="p-mut">RAG-powered research assistant.</text>
    </g>
  </g>
</svg>'''
    with open('assets/premium_github.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

if __name__ == '__main__':
    generate_github_svg()
