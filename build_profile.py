import base64
from pathlib import Path
import zipfile

ROOT = Path(".")
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

# 1. Read and encode images
id_png = ASSETS / "id.png"
pointing_png = ASSETS / "right_pointing.png"

if not id_png.exists() or not pointing_png.exists():
    raise FileNotFoundError("id.png or right_pointing.png missing from assets/")

id_b64 = "data:image/png;base64," + base64.b64encode(id_png.read_bytes()).decode("utf-8")
pointing_b64 = "data:image/png;base64," + base64.b64encode(pointing_png.read_bytes()).decode("utf-8")

# Common styling tokens
COMMON_DEFS = """
    <defs>
      <linearGradient id="{ns}bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#070b16"/>
        <stop offset="50%" stop-color="#0b1329"/>
        <stop offset="100%" stop-color="#060a14"/>
      </linearGradient>
      <linearGradient id="{ns}cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0d172e" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#080e1e" stop-opacity="0.95"/>
      </linearGradient>
      <linearGradient id="{ns}blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#247bff"/>
        <stop offset="100%" stop-color="#00d2ff"/>
      </linearGradient>
      <linearGradient id="{ns}crimsonGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ff354f"/>
        <stop offset="100%" stop-color="#ff758c"/>
      </linearGradient>
      <linearGradient id="{ns}borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
        <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
        <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
      </linearGradient>
      <radialGradient id="{ns}blueGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#247bff" stop-opacity="0.4"/>
        <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="{ns}crimsonGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#ff354f" stop-opacity="0.35"/>
        <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
      </radialGradient>
      <pattern id="{ns}dots" width="24" height="24" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="1.2" fill="#247bff" opacity="0.12"/>
      </pattern>
      <filter id="{ns}glowFilter" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over"/>
      </filter>
      <filter id="{ns}shadow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
      </filter>
    </defs>
"""

# ==============================================================================
# 1. HERO.SVG
# ==============================================================================
hero_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450">
  <defs>
    {COMMON_DEFS.format(ns="h_")}
    <clipPath id="h_nameClip">
      <rect x="0" y="0" width="700" height="90">
        <animate attributeName="y" values="90;0" dur="0.9s" begin="0.2s" fill="freeze" keyTimes="0;1" keySplines="0.16 1 0.3 1" calcMode="spline"/>
      </rect>
    </clipPath>
  </defs>

  <style>
    .h-text-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif; }}
    .h-text-mono {{ font-family: ui-monospace, "SF Mono", "Cascadia Code", "Fira Code", monospace; }}
    
    @keyframes h_cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    .h-cursor {{ animation: h_cursorBlink 0.8s infinite; }}
    
    @keyframes h_roleCycle {{
      0%, 20% {{ opacity: 1; transform: translateY(0px); }}
      23%, 25% {{ opacity: 0; transform: translateY(-12px); }}
      26% {{ opacity: 0; transform: translateY(12px); }}
      28%, 45% {{ opacity: 1; transform: translateY(0px); }}
      48%, 50% {{ opacity: 0; transform: translateY(-12px); }}
      51% {{ opacity: 0; transform: translateY(12px); }}
      53%, 70% {{ opacity: 1; transform: translateY(0px); }}
      73%, 75% {{ opacity: 0; transform: translateY(-12px); }}
      76% {{ opacity: 0; transform: translateY(12px); }}
      78%, 95% {{ opacity: 1; transform: translateY(0px); }}
      98%, 100% {{ opacity: 0; transform: translateY(-12px); }}
    }}

    .h-role-1 {{ animation: h_role1 12s infinite; }}
    .h-role-2 {{ animation: h_role2 12s infinite; }}
    .h-role-3 {{ animation: h_role3 12s infinite; }}
    .h-role-4 {{ animation: h_role4 12s infinite; }}

    @keyframes h_role1 {{ 0%, 20% {{ opacity: 1; transform: translateY(0); }} 23%, 97% {{ opacity: 0; transform: translateY(-8px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes h_role2 {{ 0%, 22% {{ opacity: 0; transform: translateY(8px); }} 25%, 45% {{ opacity: 1; transform: translateY(0); }} 48%, 100% {{ opacity: 0; transform: translateY(-8px); }} }}
    @keyframes h_role3 {{ 0%, 47% {{ opacity: 0; transform: translateY(8px); }} 50%, 70% {{ opacity: 1; transform: translateY(0); }} 73%, 100% {{ opacity: 0; transform: translateY(-8px); }} }}
    @keyframes h_role4 {{ 0%, 72% {{ opacity: 0; transform: translateY(8px); }} 75%, 95% {{ opacity: 1; transform: translateY(0); }} 98%, 100% {{ opacity: 0; transform: translateY(-8px); }} }}

    @media (prefers-reduced-motion: reduce) {{
      .h-cursor, .h-role-1, .h-role-2, .h-role-3, .h-role-4 {{ animation: none !important; opacity: 1 !important; transform: none !important; }}
      .h-role-2, .h-role-3, .h-role-4 {{ display: none; }}
    }}
  </style>

  <!-- Container Frame -->
  <rect width="1200" height="450" rx="20" fill="url(#h_bg)"/>
  <rect width="1200" height="450" rx="20" fill="url(#h_dots)"/>
  <rect x="1" y="1" width="1198" height="448" rx="19" fill="none" stroke="url(#h_borderGrad)" stroke-width="1.5"/>

  <!-- Background Ambience Glows -->
  <circle cx="980" cy="225" r="240" fill="url(#h_blueGlow)"/>
  <circle cx="1060" cy="250" r="180" fill="url(#h_crimsonGlow)"/>
  <circle cx="200" cy="100" r="150" fill="url(#h_blueGlow)" opacity="0.3"/>

  <!-- Left Content Column -->
  <g transform="translate(60, 50)">
    <!-- Terminal Header / Status Tag -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="260" height="32" rx="16" fill="#0d1933" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.4"/>
      <circle cx="16" cy="16" r="4" fill="#00e676">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="21" class="h-text-mono" font-size="12" font-weight="600" fill="#247bff" letter-spacing="1.5">OPEN FOR ROLES &amp; COLLABS</text>
    </g>

    <!-- Sub-greeting with typing prompt -->
    <g transform="translate(0, 65)">
      <text x="0" y="0" class="h-text-mono" font-size="16" fill="#94a3b8" letter-spacing="2">
        <tspan fill="#ff354f">&gt;</tspan> HELLO WORLD, I'M
      </text>
    </g>

    <!-- Giant Name Reveal with Mask -->
    <g transform="translate(0, 80)">
      <g clip-path="url(#h_nameClip)">
        <text x="0" y="70" class="h-text-sans" font-size="64" font-weight="900" fill="#ffffff" letter-spacing="-1">
          ABHIJAT <tspan fill="url(#h_crimsonGrad)">PATEL</tspan>
        </text>
      </g>
    </g>

    <!-- Animated Cycling Role Badges -->
    <g transform="translate(0, 180)">
      <!-- Base container badge -->
      <rect x="0" y="0" width="460" height="42" rx="10" fill="#0c152a" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.5"/>
      <rect x="0" y="0" width="6" height="42" rx="3" fill="url(#h_blueGrad)"/>

      <g transform="translate(24, 26)">
        <!-- Role 1 -->
        <g class="h-role-1">
          <text x="0" y="0" class="h-text-mono" font-size="16" font-weight="700" fill="#247bff">⚡ FULL STACK DEVELOPER</text>
        </g>
        <!-- Role 2 -->
        <g class="h-role-2" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="16" font-weight="700" fill="#00d2ff">🚀 MERN STACK ARCHITECT</text>
        </g>
        <!-- Role 3 -->
        <g class="h-role-3" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="16" font-weight="700" fill="#ff354f">🧠 C++ &amp; DSA PROBLEM SOLVER</text>
        </g>
        <!-- Role 4 -->
        <g class="h-role-4" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="16" font-weight="700" fill="#ffd166">🤖 AI SYSTEMS &amp; TECH EXPLORER</text>
        </g>
      </g>
      <text x="430" y="27" class="h-text-mono h-cursor" font-size="18" fill="#247bff">_</text>
    </g>

    <!-- One-line Pitch -->
    <g transform="translate(0, 255)">
      <text x="0" y="0" class="h-text-sans" font-size="18" fill="#cbd5e1" font-weight="400">
        Crafting high-performance full-stack applications, intelligent AI tools,
      </text>
      <text x="0" y="26" class="h-text-sans" font-size="18" fill="#cbd5e1" font-weight="400">
        and scalable software with relentless curiosity.
      </text>
    </g>

    <!-- Info / Meta Row -->
    <g transform="translate(0, 325)">
      <!-- Location Chip -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="160" height="34" rx="8" fill="#0a1224" stroke="#1e2d4d" stroke-width="1"/>
        <circle cx="18" cy="17" r="4" fill="#ff354f"/>
        <text x="32" y="22" class="h-text-sans" font-size="13" font-weight="500" fill="#94a3b8">Noida, India</text>
      </g>

      <!-- University / Org Chip -->
      <g transform="translate(175, 0)">
        <rect x="0" y="0" width="310" height="34" rx="8" fill="#0a1224" stroke="#1e2d4d" stroke-width="1"/>
        <text x="16" y="22" class="h-text-sans" font-size="13" font-weight="500" fill="#94a3b8">
          🎓 <tspan fill="#e2e8f0">JSS Academy of Tech Education</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- Right Portrait Column with Neon Glow & Tech Accents -->
  <g transform="translate(760, 25)">
    <!-- Backdrop Card Frame with Dual Gradient Neon Rim -->
    <rect x="40" y="15" width="340" height="370" rx="28" fill="#091224" filter="url(#h_shadow)"/>
    <rect x="40" y="15" width="340" height="370" rx="28" fill="none" stroke="url(#h_blueGrad)" stroke-width="2"/>
    <rect x="40" y="15" width="340" height="370" rx="28" fill="none" stroke="url(#h_crimsonGrad)" stroke-width="1.2" opacity="0.6"/>

    <!-- Decorative Corner Marks -->
    <path d="M 40 45 L 40 25 Q 40 15 50 15 L 70 15" fill="none" stroke="#00d2ff" stroke-width="3"/>
    <path d="M 350 385 L 370 385 Q 380 385 380 375 L 380 355" fill="none" stroke="#ff354f" stroke-width="3"/>

    <!-- Clipped Portrait Image -->
    <clipPath id="h_portraitClip">
      <rect x="42" y="17" width="336" height="366" rx="26"/>
    </clipPath>

    <g clip-path="url(#h_portraitClip)">
      <image href="{id_b64}" x="35" y="10" width="350" height="380" preserveAspectRatio="xMidYMid slice"/>
    </g>

    <!-- Floating Mini Code HUD Badge -->
    <g transform="translate(15, 305)" filter="url(#h_shadow)">
      <rect width="180" height="58" rx="12" fill="#060c1c" stroke="#247bff" stroke-width="1.2" opacity="0.95"/>
      <circle cx="16" cy="18" r="4" fill="#ff354f"/>
      <circle cx="28" cy="18" r="4" fill="#ffb703"/>
      <circle cx="40" cy="18" r="4" fill="#00e676"/>
      <text x="16" y="44" class="h-text-mono" font-size="12" font-weight="700" fill="#00d2ff">const dev = "builder";</text>
    </g>
  </g>
</svg>"""

(ASSETS / "hero.svg").write_text(hero_svg, encoding="utf-8")
print("[OK] Created assets/hero.svg")

# ==============================================================================
# 2. ABOUT-LIFE.SVG (3-slide Carousel with segment progress bars & capabilities)
# ==============================================================================
about_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450">
  <defs>
    {COMMON_DEFS.format(ns="ab_")}
  </defs>

  <style>
    .ab-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif; }}
    .ab-mono {{ font-family: ui-monospace, "SF Mono", "Cascadia Code", "Fira Code", monospace; }}

    /* 3-Slide Carousel Keyframes (12s total: 4s per slide) */
    @keyframes slide1Fade {{
      0%, 30% {{ opacity: 1; visibility: visible; }}
      33.3%, 96.6% {{ opacity: 0; visibility: hidden; }}
      100% {{ opacity: 1; visibility: visible; }}
    }}
    @keyframes slide2Fade {{
      0%, 30% {{ opacity: 0; visibility: hidden; }}
      33.3%, 63.3% {{ opacity: 1; visibility: visible; }}
      66.6%, 100% {{ opacity: 0; visibility: hidden; }}
    }}
    @keyframes slide3Fade {{
      0%, 63.3% {{ opacity: 0; visibility: hidden; }}
      66.6%, 96.6% {{ opacity: 1; visibility: visible; }}
      100% {{ opacity: 0; visibility: hidden; }}
    }}

    @keyframes bar1Fill {{
      0% {{ width: 0px; }}
      30% {{ width: 140px; }}
      33.3%, 100% {{ width: 0px; }}
    }}
    @keyframes bar2Fill {{
      0%, 33.3% {{ width: 0px; }}
      63.3% {{ width: 140px; }}
      66.6%, 100% {{ width: 0px; }}
    }}
    @keyframes bar3Fill {{
      0%, 66.6% {{ width: 0px; }}
      96.6% {{ width: 140px; }}
      100% {{ width: 0px; }}
    }}

    .ab-slide-1 {{ animation: slide1Fade 12s infinite; }}
    .ab-slide-2 {{ animation: slide2Fade 12s infinite; }}
    .ab-slide-3 {{ animation: slide3Fade 12s infinite; }}

    .ab-bar-1 {{ animation: bar1Fill 12s infinite linear; }}
    .ab-bar-2 {{ animation: bar2Fill 12s infinite linear; }}
    .ab-bar-3 {{ animation: bar3Fill 12s infinite linear; }}

    @media (prefers-reduced-motion: reduce) {{
      .ab-slide-1 {{ animation: none; opacity: 1; visibility: visible; }}
      .ab-slide-2, .ab-slide-3 {{ display: none; }}
      .ab-bar-1 {{ width: 140px; animation: none; }}
      .ab-bar-2, .ab-bar-3 {{ animation: none; }}
    }}
  </style>

  <!-- Container Frame -->
  <rect width="1200" height="450" rx="20" fill="url(#ab_bg)"/>
  <rect width="1200" height="450" rx="20" fill="url(#ab_dots)"/>
  <rect x="1" y="1" width="1198" height="448" rx="19" fill="none" stroke="url(#ab_borderGrad)" stroke-width="1.5"/>

  <!-- Section Title -->
  <g transform="translate(60, 42)">
    <text x="0" y="0" class="ab-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 02 // CAPABILITIES &amp; BEYOND THE TERMINAL</text>
  </g>

  <!-- Left Column: Core Technical Capabilities (4 Cards) -->
  <g transform="translate(60, 75)">
    <!-- Card 1: Full-Stack Architecture -->
    <g transform="translate(0, 0)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#247bff"/>
      <circle cx="36" cy="37" r="18" fill="#0d244d"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">⚡</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Full-Stack Web Architecture</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">React, Node.js, Express &amp; Modern REST / GraphQL APIs</text>
    </g>

    <!-- Card 2: Algorithms & Problem Solving -->
    <g transform="translate(0, 86)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#ff354f"/>
      <circle cx="36" cy="37" r="18" fill="#3b1523"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🧩</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Data Structures &amp; Problem Solving</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">Deep foundation in C++, algorithmic optimization &amp; logic</text>
    </g>

    <!-- Card 3: Database & Cloud Infrastructure -->
    <g transform="translate(0, 172)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#00d2ff"/>
      <circle cx="36" cy="37" r="18" fill="#0b2e3b"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🗄️</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Database &amp; Data Systems</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">MongoDB, MySQL schema modeling, indexing &amp; performance</text>
    </g>

    <!-- Card 4: AI Integration & Tooling -->
    <g transform="translate(0, 258)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#ffd166"/>
      <circle cx="36" cy="37" r="18" fill="#3b320d"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🤖</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">AI Tooling &amp; Intelligent Workflows</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">LLM pipelines, AI-assisted development &amp; agentic features</text>
    </g>
  </g>

  <!-- Right Column: 3-Slide Carousel with Segment Progress Bars -->
  <g transform="translate(620, 75)">
    <!-- Outer Card Wrapper -->
    <rect width="520" height="332" rx="18" fill="#091224" stroke="#1e2d4d" stroke-width="1.2" filter="url(#ab_shadow)"/>

    <!-- Carousel Header / Tab Indicator -->
    <g transform="translate(30, 24)">
      <!-- Segment 1 -->
      <rect x="0" y="0" width="140" height="4" rx="2" fill="#1b2a47"/>
      <rect x="0" y="0" width="0" height="4" rx="2" fill="#247bff" class="ab-bar-1"/>
      <text x="0" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">01 / CREATOR</text>

      <!-- Segment 2 -->
      <rect x="160" y="0" width="140" height="4" rx="2" fill="#1b2a47"/>
      <rect x="160" y="0" width="0" height="4" rx="2" fill="#ff354f" class="ab-bar-2"/>
      <text x="160" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">02 / DISCIPLINE</text>

      <!-- Segment 3 -->
      <rect x="320" y="0" width="140" height="4" rx="2" fill="#1b2a47"/>
      <rect x="320" y="0" width="0" height="4" rx="2" fill="#00d2ff" class="ab-bar-3"/>
      <text x="320" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">03 / EXPLORER</text>
    </g>

    <!-- Slide 1: Software & Product Creation -->
    <g class="ab-slide-1" transform="translate(30, 70)">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">Software &amp; Digital Craft</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1" line-height="1.6">
        Passionate about crafting pixel-perfect, highly responsive interfaces
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        backed by robust server architectures and elegant data schemas.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#0e1b38" stroke="#247bff" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#247bff" font-weight="700">PROJECT FOCUS</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">Full-Stack SaaS &amp; AI Tools</text>

        <rect x="230" width="225" height="60" rx="10" fill="#0e1b38" stroke="#247bff" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#00d2ff" font-weight="700">CODE PHILOSOPHY</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">Clean, Modular &amp; Scalable</text>
      </g>
    </g>

    <!-- Slide 2: Fitness & Physical Discipline -->
    <g class="ab-slide-2" transform="translate(30, 70)" opacity="0">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">Fitness &amp; Daily Discipline</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1">
        Believing physical strength powers mental clarity. Daily workouts
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        and fitness routines instill consistency, grit, and long-term focus.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#290e1b" stroke="#ff354f" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#ff354f" font-weight="700">CORE HABIT</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">Strength &amp; Endurance</text>

        <rect x="230" width="225" height="60" rx="10" fill="#290e1b" stroke="#ff354f" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#ff758c" font-weight="700">MINDSET</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">1% Better Every Single Day</text>
      </g>
    </g>

    <!-- Slide 3: Travel, Gaming & Curiosity -->
    <g class="ab-slide-3" transform="translate(30, 70)" opacity="0">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">Travel, Gaming &amp; Curiosity</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1">
        Exploring new landscapes, immersing in gaming narratives, and
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        gathering perspectives that inspire fresh creative problem solving.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#0c232e" stroke="#00d2ff" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#00d2ff" font-weight="700">EXPLORATION</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">Travel &amp; New Cultures</text>

        <rect x="230" width="225" height="60" rx="10" fill="#0c232e" stroke="#00d2ff" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#ffd166" font-weight="700">LEISURE</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">Strategy Games &amp; Sci-Fi</text>
      </g>
    </g>
  </g>
</svg>"""

(ASSETS / "about-life.svg").write_text(about_svg, encoding="utf-8")
print("[OK] Created assets/about-life.svg")

# ==============================================================================
# 3. STACK.SVG (Tilted Orbits with Pulsing Nodes & Grouped Tech Chips)
# ==============================================================================
stack_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450">
  <defs>
    {COMMON_DEFS.format(ns="st_")}
  </defs>

  <style>
    .st-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif; }}
    .st-mono {{ font-family: ui-monospace, "SF Mono", "Cascadia Code", "Fira Code", monospace; }}

    @keyframes st_pulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.8; }}
      50% {{ transform: scale(1.15); opacity: 1; }}
    }}
    .st-core-node {{ transform-origin: 320px 240px; animation: st_pulse 4s infinite ease-in-out; }}
  </style>

  <!-- Container Frame -->
  <rect width="1200" height="450" rx="20" fill="url(#st_bg)"/>
  <rect width="1200" height="450" rx="20" fill="url(#st_dots)"/>
  <rect x="1" y="1" width="1198" height="448" rx="19" fill="none" stroke="url(#st_borderGrad)" stroke-width="1.5"/>

  <!-- Title -->
  <g transform="translate(60, 42)">
    <text x="0" y="0" class="st-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 03 // TECH STACK &amp; PLANETARY ECOSYSTEM</text>
  </g>

  <!-- Left Side: 3 Tilted Elliptical Orbits with Core Node & Tech Icons -->
  <g transform="translate(0, 10)">
    <!-- Glow behind orbit core -->
    <circle cx="320" cy="235" r="140" fill="url(#st_blueGlow)"/>

    <!-- Orbit 1: Outer Orbit (Cloud / DB) -->
    <g transform="rotate(-15 320 235)">
      <ellipse cx="320" cy="235" rx="260" ry="110" fill="none" stroke="#1b305c" stroke-width="1.5" stroke-dasharray="6 6"/>
      <!-- Orbit 1 Tech Nodes -->
      <g transform="translate(80, 210)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#47A248" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#47A248">Mongo</text>
      </g>
      <g transform="translate(520, 220)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#00618A" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#00758F">MySQL</text>
      </g>
      <g transform="translate(320, 115)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#F05032" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#F05032">Git</text>
      </g>
    </g>

    <!-- Orbit 2: Mid Orbit (Backend / Languages) -->
    <g transform="rotate(18 320 235)">
      <ellipse cx="320" cy="235" rx="190" ry="80" fill="none" stroke="#247bff" stroke-width="1.5" opacity="0.6"/>
      <!-- Orbit 2 Tech Nodes -->
      <g transform="translate(140, 215)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#83CD29" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#83CD29">Node</text>
      </g>
      <g transform="translate(460, 215)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#3776AB" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#3776AB">Python</text>
      </g>
      <g transform="translate(305, 145)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#00599C" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#659AD2">C++</text>
      </g>
    </g>

    <!-- Orbit 3: Inner Orbit (Frontend) -->
    <g transform="rotate(-5 320 235)">
      <ellipse cx="320" cy="235" rx="115" ry="50" fill="none" stroke="#ff354f" stroke-width="1.5" opacity="0.7"/>
      <!-- Orbit 3 Tech Nodes -->
      <g transform="translate(205, 218)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#61DAFB" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="10" font-weight="700" fill="#61DAFB">React</text>
      </g>
      <g transform="translate(395, 218)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#F7DF1E" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="10" font-weight="700" fill="#F7DF1E">JS</text>
      </g>
    </g>

    <!-- Planetary Core Node -->
    <g class="st-core-node">
      <circle cx="320" cy="235" r="36" fill="#0b1733" stroke="url(#st_blueGrad)" stroke-width="2.5" filter="url(#st_shadow)"/>
      <text x="320" y="242" text-anchor="middle" class="st-mono" font-size="15" font-weight="900" fill="#ffffff">&lt;/&gt;</text>
    </g>
  </g>

  <!-- Right Side: Categorized Stack Chips Grid -->
  <g transform="translate(640, 75)">
    <!-- Category 1: Frontend & UI -->
    <g transform="translate(0, 0)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#247bff" letter-spacing="1">FRONTEND &amp; CLIENT</text>
      <g transform="translate(0, 28)">
        <!-- React -->
        <rect x="0" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#61DAFB" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="16" cy="17" r="4" fill="#61DAFB"/>
        <text x="30" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">React.js</text>

        <!-- JavaScript -->
        <rect x="125" y="0" width="125" height="34" rx="8" fill="url(#st_cardBg)" stroke="#F7DF1E" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="141" cy="17" r="4" fill="#F7DF1E"/>
        <text x="155" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">JavaScript (ES6+)</text>

        <!-- HTML5/CSS3 -->
        <rect x="260" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#E34F26" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="276" cy="17" r="4" fill="#E34F26"/>
        <text x="290" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">HTML5 / CSS3</text>

        <!-- Tailwind -->
        <rect x="385" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#38BDF8" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="401" cy="17" r="4" fill="#38BDF8"/>
        <text x="415" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">TailwindCSS</text>
      </g>
    </g>

    <!-- Category 2: Backend & Server -->
    <g transform="translate(0, 90)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#00d2ff" letter-spacing="1">BACKEND &amp; RUNTIMES</text>
      <g transform="translate(0, 28)">
        <!-- Node.js -->
        <rect x="0" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#83CD29" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="16" cy="17" r="4" fill="#83CD29"/>
        <text x="30" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">Node.js</text>

        <!-- Express.js -->
        <rect x="125" y="0" width="125" height="34" rx="8" fill="url(#st_cardBg)" stroke="#ffffff" stroke-width="1" stroke-opacity="0.4"/>
        <circle cx="141" cy="17" r="4" fill="#ffffff"/>
        <text x="155" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">Express.js</text>

        <!-- REST APIs -->
        <rect x="260" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="276" cy="17" r="4" fill="#247bff"/>
        <text x="290" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">REST APIs</text>

        <!-- Python -->
        <rect x="385" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#3776AB" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="401" cy="17" r="4" fill="#3776AB"/>
        <text x="415" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">Python</text>
      </g>
    </g>

    <!-- Category 3: Databases, Algorithms & Tools -->
    <g transform="translate(0, 180)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#ff354f" letter-spacing="1">DATA, DSA &amp; SYSTEM TOOLS</text>
      <g transform="translate(0, 28)">
        <!-- MongoDB -->
        <rect x="0" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#47A248" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="16" cy="17" r="4" fill="#47A248"/>
        <text x="30" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">MongoDB</text>

        <!-- MySQL -->
        <rect x="125" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#00758F" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="141" cy="17" r="4" fill="#00758F"/>
        <text x="155" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">MySQL</text>

        <!-- C++ DSA -->
        <rect x="250" y="0" width="125" height="34" rx="8" fill="url(#st_cardBg)" stroke="#00599C" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="266" cy="17" r="4" fill="#659AD2"/>
        <text x="280" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">C++ &amp; DSA</text>

        <!-- Git / GitHub -->
        <rect x="385" y="0" width="115" height="34" rx="8" fill="url(#st_cardBg)" stroke="#F05032" stroke-width="1" stroke-opacity="0.6"/>
        <circle cx="401" cy="17" r="4" fill="#F05032"/>
        <text x="415" y="22" class="st-sans" font-size="13" font-weight="600" fill="#ffffff">Git / GitHub</text>
      </g>
    </g>

    <!-- Bottom Metrics Banner -->
    <g transform="translate(0, 275)">
      <rect width="500" height="50" rx="12" fill="#0c162d" stroke="#1f335c" stroke-width="1"/>
      <text x="20" y="30" class="st-sans" font-size="13" fill="#94a3b8">
        Focused on building <tspan fill="#00d2ff" font-weight="700">clean architectures</tspan>, optimized queries &amp; scalable web services.
      </text>
    </g>
  </g>
</svg>"""

(ASSETS / "stack.svg").write_text(stack_svg, encoding="utf-8")
print("[OK] Created assets/stack.svg")

# ==============================================================================
# 4. ID-DASHBOARD.SVG (Hanging Lanyard ID with Damped Swing Motion & Metrics)
# ==============================================================================
id_dash_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450">
  <defs>
    {COMMON_DEFS.format(ns="id_")}
    <linearGradient id="id_strap" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="id_metal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <clipPath id="id_passClip">
      <rect x="70" y="80" width="260" height="310" rx="18"/>
    </clipPath>
    <clipPath id="id_cardPhotoClip">
      <rect x="85" y="95" width="230" height="150" rx="12"/>
    </clipPath>
  </defs>

  <style>
    .id-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif; }}
    .id-mono {{ font-family: ui-monospace, "SF Mono", "Cascadia Code", "Fira Code", monospace; }}

    /* Pendulum entrance and continuous gentle swing (+-1.7 deg) */
    @keyframes id_pendulum {{
      0% {{ transform: rotate(-12deg); }}
      20% {{ transform: rotate(8deg); }}
      40% {{ transform: rotate(-4deg); }}
      60% {{ transform: rotate(2.5deg); }}
      80% {{ transform: rotate(-1.7deg); }}
      90% {{ transform: rotate(1.7deg); }}
      100% {{ transform: rotate(-1.7deg); }}
    }}
    @keyframes id_gentleSwing {{
      0%, 100% {{ transform: rotate(-1.7deg); }}
      50% {{ transform: rotate(1.7deg); }}
    }}

    .id-lanyard-assembly {{
      transform-origin: 200px 0px;
      animation: id_pendulum 3s ease-out forwards, id_gentleSwing 5s ease-in-out 3s infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .id-lanyard-assembly {{ animation: none; transform: rotate(0deg); }}
    }}
  </style>

  <!-- Container Frame -->
  <rect width="1200" height="450" rx="20" fill="url(#id_bg)"/>
  <rect width="1200" height="450" rx="20" fill="url(#id_dots)"/>
  <rect x="1" y="1" width="1198" height="448" rx="19" fill="none" stroke="url(#id_borderGrad)" stroke-width="1.5"/>

  <!-- Section Title -->
  <g transform="translate(60, 42)">
    <text x="0" y="0" class="id-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 04 // DEVELOPER PASS &amp; VERIFIED METRICS</text>
  </g>

  <!-- Left: Hanging Lanyard Pass Assembly -->
  <g class="id-lanyard-assembly">
    <!-- Strap -->
    <path d="M 185 0 L 195 55 L 205 55 L 215 0" fill="url(#id_strap)" opacity="0.9"/>
    
    <!-- Metal Clip Clasp -->
    <g transform="translate(188, 50)">
      <rect width="24" height="22" rx="4" fill="url(#id_metal)"/>
      <ellipse cx="12" cy="22" rx="6" ry="4" fill="#334155"/>
      <rect x="8" y="24" width="8" height="12" rx="2" fill="url(#id_metal)"/>
    </g>

    <!-- ID Badge Card Body -->
    <g filter="url(#id_shadow)">
      <rect x="70" y="80" width="260" height="310" rx="18" fill="#091326" stroke="#247bff" stroke-width="1.8"/>
      
      <!-- Top Lanyard Hole Slot -->
      <rect x="180" y="86" width="40" height="6" rx="3" fill="#020611"/>

      <!-- Embedded Photo inside Card -->
      <g clip-path="url(#id_cardPhotoClip)">
        <image href="{id_b64}" x="75" y="80" width="250" height="200" preserveAspectRatio="xMidYMid slice"/>
      </g>
      <rect x="85" y="95" width="230" height="150" rx="12" fill="none" stroke="#247bff" stroke-width="1" opacity="0.6"/>

      <!-- Cardholder Details -->
      <text x="85" y="272" class="id-sans" font-size="20" font-weight="900" fill="#ffffff">ABHIJAT PATEL</text>
      <text x="85" y="292" class="id-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1">FULL STACK DEVELOPER</text>
      
      <!-- Hologram / Barcode Footer -->
      <g transform="translate(85, 312)">
        <rect width="230" height="26" rx="4" fill="#040914"/>
        <path d="M 10 6 h 3 m 4 0 h 2 m 4 0 h 6 m 3 0 h 2 m 5 0 h 4 m 6 0 h 2 m 5 0 h 5 m 3 0 h 2 m 5 0 h 6 m 4 0 h 3 m 5 0 h 2 m 6 0 h 4 m 5 0 h 2 m 5 0 h 5 m 4 0 h 2 m 6 0 h 6 m 3 0 h 2 m 5 0 h 3" stroke="#e2e8f0" stroke-width="1.5"/>
        <text x="175" y="17" class="id-mono" font-size="9" fill="#247bff">#DEV-2027</text>
      </g>

      <!-- Verified Ribbon Badge -->
      <g transform="translate(265, 90)">
        <circle cx="16" cy="16" r="14" fill="#00e676" filter="url(#id_shadow)"/>
        <text x="16" y="21" text-anchor="middle" font-size="14" font-weight="900" fill="#020611">✓</text>
      </g>
    </g>
  </g>

  <!-- Right: Verified Developer Dashboard & Education Cards -->
  <g transform="translate(380, 75)">
    <!-- Top Row: Verified Metrics Cards -->
    <g transform="translate(0, 0)">
      <!-- Card 1: Primary Focus -->
      <g transform="translate(0, 0)">
        <rect width="245" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#247bff"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#247bff">CORE FOCUS</text>
        <text x="24" y="60" class="id-sans" font-size="20" font-weight="800" fill="#ffffff">MERN &amp; DSA</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">Active Daily Problem Solving</text>
      </g>

      <!-- Card 2: Degree & Academic standing -->
      <g transform="translate(265, 0)">
        <rect width="245" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#ff354f"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#ff354f">ACADEMIC CGPA</text>
        <text x="24" y="60" class="id-sans" font-size="20" font-weight="800" fill="#ffffff">7.13 / 10.0</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">Information Technology</text>
      </g>

      <!-- Card 3: Status -->
      <g transform="translate(530, 0)">
        <rect width="230" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#00e676"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#00e676">DEV STATUS</text>
        <text x="24" y="60" class="id-sans" font-size="20" font-weight="800" fill="#ffffff">ACTIVE</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">Available for Opportunities</text>
      </g>
    </g>

    <!-- Bottom Row: Education & Milestone Overview -->
    <g transform="translate(0, 120)">
      <rect width="760" height="205" rx="16" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      
      <!-- Education Section -->
      <g transform="translate(30, 25)">
        <text x="0" y="16" class="id-mono" font-size="12" font-weight="700" fill="#247bff" letter-spacing="1">EDUCATION &amp; FORMAL TRAINING</text>
        
        <text x="0" y="48" class="id-sans" font-size="18" font-weight="800" fill="#ffffff">Bachelor of Technology (B.Tech) — Information Technology</text>
        <text x="0" y="74" class="id-sans" font-size="14" fill="#cbd5e1">🏛️ JSS Academy of Technical Education, Noida</text>
        <text x="0" y="98" class="id-sans" font-size="13" fill="#94a3b8">📅 2023 – 2027 • Full-time Engineering</text>
      </g>

      <line x1="30" y1="138" x2="730" y2="138" stroke="#1b2d4d" stroke-width="1"/>

      <!-- Engineering Roadmap Goals -->
      <g transform="translate(30, 155)">
        <text x="0" y="16" class="id-mono" font-size="11" font-weight="700" fill="#00d2ff">CURRENT ENGINEERING GOAL:</text>
        <text x="0" y="36" class="id-sans" font-size="13" fill="#ffffff">
          "Mastering distributed systems, full-stack product development, and shipping real-world AI applications."
        </text>
      </g>
    </g>
  </g>
</svg>"""

(ASSETS / "id-dashboard.svg").write_text(id_dash_svg, encoding="utf-8")
print("[OK] Created assets/id-dashboard.svg")

# ==============================================================================
# 5. CONNECT.SVG (Right-Pointing Character with Social Cards & Nudging Arrows)
# ==============================================================================
connect_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450">
  <defs>
    {COMMON_DEFS.format(ns="cn_")}
    <clipPath id="cn_charClip">
      <rect x="40" y="40" width="440" height="390" rx="16"/>
    </clipPath>
  </defs>

  <style>
    .cn-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif; }}
    .cn-mono {{ font-family: ui-monospace, "SF Mono", "Cascadia Code", "Fira Code", monospace; }}

    @keyframes cn_nudge {{
      0%, 100% {{ transform: translateX(0px); }}
      50% {{ transform: translateX(10px); }}
    }}
    .cn-arrow-nudge {{ animation: cn_nudge 1.5s infinite ease-in-out; }}

    @media (prefers-reduced-motion: reduce) {{
      .cn-arrow-nudge {{ animation: none; }}
    }}
  </style>

  <!-- Container Frame -->
  <rect width="1200" height="450" rx="20" fill="url(#cn_bg)"/>
  <rect width="1200" height="450" rx="20" fill="url(#cn_dots)"/>
  <rect x="1" y="1" width="1198" height="448" rx="19" fill="none" stroke="url(#cn_borderGrad)" stroke-width="1.5"/>

  <!-- Ambient Glows -->
  <circle cx="280" cy="240" r="180" fill="url(#cn_blueGlow)"/>
  <circle cx="850" cy="225" r="220" fill="url(#cn_crimsonGlow)" opacity="0.4"/>

  <!-- Left: Pointing Character -->
  <g transform="translate(10, 20)">
    <g clip-path="url(#cn_charClip)">
      <image href="{pointing_b64}" x="20" y="25" width="460" height="400" preserveAspectRatio="xMidYMid meet"/>
    </g>
  </g>

  <!-- Dynamic Nudging Arrow from Finger towards Social Cards -->
  <g transform="translate(450, 220)" class="cn-arrow-nudge">
    <path d="M 0 0 C 40 -20, 60 10, 95 0" fill="none" stroke="#247bff" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="8 6"/>
    <polygon points="95,-8 112,0 95,8" fill="#ff354f"/>
  </g>

  <!-- Right: Generously Spaced Interactive-Styled Social Cards -->
  <g transform="translate(580, 50)">
    <!-- Header Title -->
    <g transform="translate(0, 0)">
      <text x="0" y="0" class="cn-mono" font-size="13" font-weight="700" fill="#ff354f" letter-spacing="2">&gt; 05 // LET'S COLLABORATE &amp; CONNECT</text>
      <text x="0" y="38" class="cn-sans" font-size="34" font-weight="900" fill="#ffffff">LET'S BUILD TOGETHER</text>
      <text x="0" y="66" class="cn-sans" font-size="14" fill="#94a3b8">
        Have an open role, project idea, or just want to talk tech? Reach out below!
      </text>
    </g>

    <!-- Social Grid Cards (4 High-Impact Cards) -->
    <g transform="translate(0, 95)">
      <!-- 1. GitHub Card -->
      <g transform="translate(0, 0)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#247bff" stroke-width="1.2"/>
        <!-- GitHub Mark -->
        <circle cx="36" cy="45" r="20" fill="#181717" stroke="#ffffff" stroke-width="0.8"/>
        <path d="M36 31c-7.7 0-14 6.3-14 14 0 6.2 4 11.4 9.6 13.3.7.1 1-.3 1-.7v-2.4c-3.9.8-4.7-1.9-4.7-1.9-.6-1.6-1.5-2.1-1.5-2.1-1.3-.9.1-.9.1-.9 1.4.1 2.2 1.4 2.2 1.4 1.2 2.2 3.3 1.5 4.1 1.2.1-.9.5-1.5.9-1.9-3.1-.4-6.4-1.6-6.4-7 0-1.5.5-2.8 1.4-3.8-.1-.4-.6-1.8.1-3.7 0 0 1.2-.4 3.9 1.5 1.1-.3 2.3-.5 3.5-.5s2.4.2 3.5.5c2.7-1.9 3.9-1.5 3.9-1.5.8 1.9.3 3.3.1 3.7.9 1 1.4 2.3 1.4 3.8 0 5.4-3.3 6.6-6.4 7 .5.4 1 1.3 1 2.5v3.8c0 .4.3.8 1 .7 5.6-1.9 9.6-7.1 9.6-13.3 0-7.7-6.3-14-14-14z" fill="#ffffff"/>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">GitHub</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#247bff">@AbhijatPatel</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#247bff">→</text>
      </g>

      <!-- 2. LinkedIn Card -->
      <g transform="translate(290, 0)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#0A66C2" stroke-width="1.2"/>
        <circle cx="36" cy="45" r="20" fill="#0A66C2"/>
        <text x="36" y="52" text-anchor="middle" class="cn-sans" font-size="18" font-weight="900" fill="#ffffff">in</text>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">LinkedIn</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#00d2ff">Connect &amp; Message</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#00d2ff">→</text>
      </g>

      <!-- 3. Instagram / Social Card -->
      <g transform="translate(0, 105)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#E4405F" stroke-width="1.2"/>
        <circle cx="36" cy="45" r="20" fill="#E4405F"/>
        <text x="36" y="52" text-anchor="middle" class="cn-sans" font-size="16" font-weight="900" fill="#ffffff">📷</text>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">Instagram</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#ff758c">Follow Journey</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#ff758c">→</text>
      </g>

      <!-- 4. Email / YouTube Card -->
      <g transform="translate(290, 105)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#ff354f" stroke-width="1.2"/>
        <circle cx="36" cy="45" r="20" fill="#ff354f"/>
        <text x="36" y="52" text-anchor="middle" class="cn-sans" font-size="16" font-weight="900" fill="#ffffff">▶</text>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">YouTube &amp; Media</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#ff354f">Tech &amp; Dev Content</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#ff354f">→</text>
      </g>
    </g>

    <!-- Interactive Links Notice -->
    <g transform="translate(0, 312)">
      <text x="0" y="0" class="cn-mono" font-size="11" fill="#64748b">
        💡 <tspan fill="#cbd5e1">Clickable badges and repository links are available below the artwork.</tspan>
      </text>
    </g>
  </g>
</svg>"""

(ASSETS / "connect.svg").write_text(connect_svg, encoding="utf-8")
print("[OK] Created assets/connect.svg")

# ==============================================================================
# 6. ROOT README.MD (With all 5 relative paths ?v=1, Projects Table & Clickable Socials)
# ==============================================================================
readme_content = """<div align="center">

# ⚡ ABHIJAT PATEL
### Full Stack Developer • MERN Architect • C++ & DSA • AI Explorer

![Hero](./assets/hero.svg?v=1)

![About](./assets/about-life.svg?v=1)

![Stack](./assets/stack.svg?v=1)

![Developer ID](./assets/id-dashboard.svg?v=1)

![Connect](./assets/connect.svg?v=1)

</div>

---

## 🚀 Featured Projects

| Project | Description | Stack / Category | Status |
| :--- | :--- | :--- | :---: |
| 🛡️ **[Clever AI](https://github.com/AbhijatPatel)** | AI Content Intelligence & Forensics Platform for deepfake detection and semantic verification | `React` `Python` `AI/LLM` `Node.js` | 🟢 Active |
| ⚽ **[MatchStory.AI](https://github.com/AbhijatPatel)** | Automated AI-powered sports storytelling & interactive match commentary generation engine | `React` `FastAPI` `NLP` `TailwindCSS` | 🟢 Active |
| 🌐 **[Developer Portfolio](https://github.com/AbhijatPatel)** | Ultra-fast personal engineering portfolio with sleek dark mode, micro-animations and interactive UI | `HTML5` `CSS3` `JavaScript` `Responsive` | 🟢 Active |
| 🌦️ **[Weather Dashboard](https://github.com/AbhijatPatel)** | Real-time weather intelligence dashboard with geolocation forecasting and climate analytics | `JavaScript` `OpenWeather API` `CSS Grid` | 🟢 Active |
| 🔢 **[NebulaCalc Pro](https://github.com/AbhijatPatel)** | High-precision scientific calculator with formula history parsing and custom themes | `C++` `Modern Web` `Algorithms` | 🟢 Active |

---

## 🔗 Connect With Me

<div align="center">

<a href="https://github.com/AbhijatPatel" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-AbhijatPatel-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
&nbsp;
<a href="https://linkedin.com/in/abhijat-patel" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
&nbsp;
<a href="https://instagram.com" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
</a>
&nbsp;
<a href="https://youtube.com" target="_blank">
  <img src="https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/>
</a>

<br/><br/>

```bash
npx abhijat-patel
```

---

<p align="center">
  <b>BUILD • LEARN • SOLVE • REPEAT</b><br/>
  <i>Crafted with passion by Abhijat Patel</i>
</p>

</div>
"""

(ROOT / "README.md").write_text(readme_content, encoding="utf-8")
print("[OK] Created README.md")

# ==============================================================================
# 7. PREVIEW.HTML (Interactive local preview with timeline scrubbing & responsive testing)
# ==============================================================================
preview_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhijat Patel - GitHub Profile Live Preview</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: #030712;
      color: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 30px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .header {
      max-width: 1200px;
      width: 100%;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 24px;
      background: #091224;
      border: 1px solid #1e293b;
      border-radius: 12px;
    }
    .header h1 { font-size: 20px; font-weight: 700; color: #ffffff; }
    .badge {
      background: #247bff;
      color: #fff;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }
    .container {
      max-width: 1200px;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .card {
      width: 100%;
      background: #070b16;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .card img, .card object {
      display: block;
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <div class="header">
    <div>
      <h1>Abhijat Patel — GitHub Profile Visual Verification</h1>
      <p style="color: #94a3b8; font-size: 13px; margin-top: 4px;">Standalone SVG + SMIL animation suite matching GitHub rendering engine</p>
    </div>
    <span class="badge">100% GITHUB SAFE</span>
  </div>

  <div class="container">
    <div class="card">
      <img src="./assets/hero.svg?v=1" alt="Hero Section"/>
    </div>
    <div class="card">
      <img src="./assets/about-life.svg?v=1" alt="About Section"/>
    </div>
    <div class="card">
      <img src="./assets/stack.svg?v=1" alt="Tech Stack Section"/>
    </div>
    <div class="card">
      <img src="./assets/id-dashboard.svg?v=1" alt="ID Dashboard Section"/>
    </div>
    <div class="card">
      <img src="./assets/connect.svg?v=1" alt="Connect Section"/>
    </div>
  </div>
</body>
</html>
"""

(ROOT / "preview.html").write_text(preview_html, encoding="utf-8")
print("[OK] Created preview.html")

# ==============================================================================
# 8. ZIP PACKAGE GENERATOR
# ==============================================================================
zip_path = ROOT / "Abhijat_GitHub_Profile_Complete.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(ROOT / "README.md", arcname="README.md")
    z.write(ROOT / "preview.html", arcname="preview.html")
    for asset in ASSETS.iterdir():
        if asset.is_file():
            z.write(asset, arcname=f"assets/{asset.name}")

print(f"[OK] Created zip package: {zip_path.name}")
print("ALL DONE!")
