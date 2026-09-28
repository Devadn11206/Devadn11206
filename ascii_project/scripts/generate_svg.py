import os
import random
from image_to_ascii import convert_to_ascii

def generate_svgs(ascii_matrix, out_animated, out_static):
    height = len(ascii_matrix)
    width = len(ascii_matrix[0]) if height > 0 else 0
    
    char_width = 7.2
    char_height = 12
    
    svg_width = int(width * char_width)
    svg_height = int(height * char_height)
    
    # CSS Classes and Animations
    style = """
    <style>
        .bg { fill: #0d0d14; }
        .text-group {
            font-family: 'Courier New', Consolas, monospace;
            font-size: 12px;
            font-weight: bold;
            animation: breathe 10s ease-in-out infinite;
            transform-origin: center;
        }
        
        .char {
            opacity: 0;
            animation: assemble 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        }
        
        /* Different delays for chaotic assembly */
        .d0 { animation-delay: 0.2s; }
        .d1 { animation-delay: 0.5s; }
        .d2 { animation-delay: 0.8s; }
        .d3 { animation-delay: 1.1s; }
        .d4 { animation-delay: 1.4s; }
        
        /* Coloring ramp */
        .color-dark { fill: #4B0082; }
        .color-mid { fill: #8A2BE2; }
        .color-light { fill: #D8B4E2; filter: drop-shadow(0px 0px 2px rgba(138,43,226,0.8)); }
        .color-white { fill: #FFFFFF; filter: drop-shadow(0px 0px 4px rgba(255,255,255,0.9)); }
        
        /* Flickering classes */
        .flicker {
            animation: assemble 4s cubic-bezier(0.25, 1, 0.5, 1) forwards, glitch 6s infinite 4s;
        }
        
        @keyframes assemble {
            0% { opacity: 0; transform: translateY(-20px) scale(0.8); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }
        
        @keyframes breathe {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        @keyframes glitch {
            0%, 96%, 100% { opacity: 1; transform: translate(0, 0); fill: inherit; }
            97% { opacity: 0.8; transform: translate(1px, -1px); fill: #00ffff; }
            98% { opacity: 0.9; transform: translate(-1px, 1px); fill: #ff00ff; }
            99% { opacity: 0.5; transform: translate(0, 0); }
        }
        
        .scanline {
            width: 100%;
            height: 4px;
            fill: rgba(138, 43, 226, 0.3);
            animation: scan 8s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: translateY(-50px); }
            100% { transform: translateY(__HEIGHT__px); }
        }
    </style>
    """.replace("__HEIGHT__", str(svg_height + 50))
    
    # Static style without animations
    static_style = """
    <style>
        .bg { fill: #0d0d14; }
        .text-group {
            font-family: 'Courier New', Consolas, monospace;
            font-size: 12px;
            font-weight: bold;
        }
        .char { opacity: 1; }
        .color-dark { fill: #4B0082; }
        .color-mid { fill: #8A2BE2; }
        .color-light { fill: #D8B4E2; filter: drop-shadow(0px 0px 2px rgba(138,43,226,0.8)); }
        .color-white { fill: #FFFFFF; filter: drop-shadow(0px 0px 4px rgba(255,255,255,0.9)); }
    </style>
    """
    
    def get_color_class(char):
        if char in "@%#":
            return "color-dark"
        elif char in "*+=":
            return "color-mid"
        elif char in "-:.":
            return "color-light"
        else:
            return "color-white"

    elements = []
    ramp = "@%#*+=-:. "
    
    for r, row in enumerate(ascii_matrix):
        for c, char in enumerate(row):
            if char == " ":
                continue
                
            x = c * char_width
            y = (r + 1) * char_height
            
            color_cls = get_color_class(char)
            delay_cls = f"d{random.randint(0, 4)}"
            flicker_cls = "flicker" if random.random() < 0.05 else ""
            
            classes = f"char {color_cls} {delay_cls} {flicker_cls}".strip()
            static_classes = f"char {color_cls}".strip()
            
            # Using basic SVG translation instead of CSS transform on each element to keep SVG compatible and lightweight
            # However, for assembly animation we use CSS transform.
            # To isolate transforms per element in SVG safely:
            # We wrap in <g> or just apply to <text>. <text> transform origin is 0,0 but we can use relative movement.
            
            elements.append((
                f'<text x="{x:.1f}" y="{y:.1f}" class="{classes}">{char}</text>',
                f'<text x="{x:.1f}" y="{y:.1f}" class="{static_classes}">{char}</text>'
            ))
            
    svg_base = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">
    <rect width="100%" height="100%" class="bg" />"""
    
    animated_svg = [svg_base, style, '<g class="text-group">']
    static_svg = [svg_base, static_style, '<g class="text-group">']
    
    for anim_el, stat_el in elements:
        animated_svg.append(anim_el)
        static_svg.append(stat_el)
        
    animated_svg.append('</g>')
    animated_svg.append('<rect class="scanline" x="0" y="0" />')
    animated_svg.append('</svg>')
    
    static_svg.append('</g>')
    static_svg.append('</svg>')
    
    with open(out_animated, "w", encoding="utf-8") as f:
        f.write("\n".join(animated_svg))
        
    with open(out_static, "w", encoding="utf-8") as f:
        f.write("\n".join(static_svg))
        
    print(f"Generated {out_animated} and {out_static}")

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prepped_path = os.path.join(base_dir, "assets", "source-prepped.png")
    out_anim = os.path.join(base_dir, "assets", "devanandu-ascii.svg")
    out_stat = os.path.join(base_dir, "assets", "devanandu-ascii-static.svg")
    
    matrix = convert_to_ascii(prepped_path, width=80, char_aspect_ratio=0.5)
    generate_svgs(matrix, out_anim, out_stat)
