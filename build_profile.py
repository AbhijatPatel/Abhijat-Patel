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
        <stop offset="0%" stop-color="#0d172e" stop-opacity="0.88"/>
        <stop offset="100%" stop-color="#080e1e" stop-opacity="0.96"/>
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
        <stop offset="0%" stop-color="#247bff" stop-opacity="0.45"/>
        <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="{ns}crimsonGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#ff354f" stop-opacity="0.4"/>
        <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
      </radialGradient>
      <pattern id="{ns}dots" width="24" height="24" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="1.2" fill="#247bff" opacity="0.12"/>
      </pattern>
      <filter id="{ns}shadow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.65"/>
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
  <g transform="translate(60, 48)">
    <!-- Terminal Header / Status Tag -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="310" height="32" rx="16" fill="#0d1933" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.4"/>
      <circle cx="16" cy="16" r="4" fill="#00e676">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="21" class="h-text-mono" font-size="12" font-weight="600" fill="#247bff" letter-spacing="1.2">OPEN FOR SDET &amp; BACKEND ROLES</text>
    </g>

    <!-- Sub-greeting with typing prompt -->
    <g transform="translate(0, 62)">
      <text x="0" y="0" class="h-text-mono" font-size="15" fill="#94a3b8" letter-spacing="2">
        <tspan fill="#ff354f">&gt;</tspan> HELLO WORLD, I'M
      </text>
    </g>

    <!-- Giant Name Reveal with Mask -->
    <g transform="translate(0, 75)">
      <g clip-path="url(#h_nameClip)">
        <text x="0" y="70" class="h-text-sans" font-size="64" font-weight="900" fill="#ffffff" letter-spacing="-1">
          ABHIJAT <tspan fill="url(#h_crimsonGrad)">PATEL</tspan>
        </text>
      </g>
    </g>

    <!-- Animated Cycling Role Badges -->
    <g transform="translate(0, 175)">
      <!-- Base container badge -->
      <rect x="0" y="0" width="500" height="42" rx="10" fill="#0c152a" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.5"/>
      <rect x="0" y="0" width="6" height="42" rx="3" fill="url(#h_blueGrad)"/>

      <g transform="translate(24, 26)">
        <!-- Role 1: SDET / Testing -->
        <g class="h-role-1">
          <text x="0" y="0" class="h-text-mono" font-size="15" font-weight="700" fill="#247bff">🛡️ SDET &amp; SOFTWARE QUALITY ENGINEER</text>
        </g>
        <!-- Role 2: Backend Development -->
        <g class="h-role-2" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="15" font-weight="700" fill="#00d2ff">⚡ JAVA SPRING BOOT &amp; FASTAPI DEV</text>
        </g>
        <!-- Role 3: AI & Verification -->
        <g class="h-role-3" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="15" font-weight="700" fill="#ff354f">🤖 MULTI-AGENT AI &amp; SEMANTIC VERIFICATION</text>
        </g>
        <!-- Role 4: DSA & Core CS -->
        <g class="h-role-4" opacity="0">
          <text x="0" y="0" class="h-text-mono" font-size="15" font-weight="700" fill="#ffd166">🧠 C++, JAVA &amp; DSA PROBLEM SOLVER</text>
        </g>
      </g>
      <text x="470" y="27" class="h-text-mono h-cursor" font-size="18" fill="#247bff">_</text>
    </g>

    <!-- One-line Pitch based on Updated Career Objective -->
    <g transform="translate(0, 250)">
      <text x="0" y="0" class="h-text-sans" font-size="16.5" fill="#cbd5e1" font-weight="400">
        Engineering backend applications, database-driven REST APIs, and automated
      </text>
      <text x="0" y="25" class="h-text-sans" font-size="16.5" fill="#cbd5e1" font-weight="400">
        software verification pipelines with rigorous validation and high reliability.
      </text>
    </g>

    <!-- Info / Meta Row -->
    <g transform="translate(0, 325)">
      <!-- Location Chip -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="180" height="34" rx="8" fill="#0a1224" stroke="#1e2d4d" stroke-width="1"/>
        <circle cx="18" cy="17" r="4" fill="#ff354f"/>
        <text x="32" y="22" class="h-text-sans" font-size="13" font-weight="500" fill="#94a3b8">Noida, UP, India</text>
      </g>

      <!-- University / Org Chip -->
      <g transform="translate(195, 0)">
        <rect x="0" y="0" width="305" height="34" rx="8" fill="#0a1224" stroke="#1e2d4d" stroke-width="1"/>
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

    <!-- Clipped Real Executive Portrait Image -->
    <clipPath id="h_portraitClip">
      <rect x="42" y="17" width="336" height="366" rx="26"/>
    </clipPath>

    <g clip-path="url(#h_portraitClip)">
      <image href="{id_b64}" x="40" y="15" width="340" height="370" preserveAspectRatio="xMidYMid slice"/>
    </g>

    <!-- Floating Mini Code HUD Badge -->
    <g transform="translate(15, 305)" filter="url(#h_shadow)">
      <rect width="195" height="58" rx="12" fill="#060c1c" stroke="#247bff" stroke-width="1.2" opacity="0.95"/>
      <circle cx="16" cy="18" r="4" fill="#ff354f"/>
      <circle cx="28" cy="18" r="4" fill="#ffb703"/>
      <circle cx="40" cy="18" r="4" fill="#00e676"/>
      <text x="16" y="44" class="h-text-mono" font-size="12" font-weight="700" fill="#00d2ff">assert dev.status == OK</text>
    </g>
  </g>
</svg>"""

(ASSETS / "hero.svg").write_text(hero_svg, encoding="utf-8")
print("[OK] Created assets/hero.svg")

# ==============================================================================
# 2. ABOUT-LIFE.SVG (Resume-grounded Capabilities & 3-Slide Carousel)
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
    <text x="0" y="0" class="ab-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 02 // TECHNICAL CAPABILITIES &amp; SOFTWARE QUALITY</text>
  </g>

  <!-- Left Column: Core Technical Capabilities (4 Cards) -->
  <g transform="translate(60, 75)">
    <!-- Card 1: Software Testing & Quality -->
    <g transform="translate(0, 0)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#247bff"/>
      <circle cx="36" cy="37" r="18" fill="#0d244d"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🛡️</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Software Testing &amp; Quality Engineering</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">Software validation, semantic verification, data validation &amp; debugging</text>
    </g>

    <!-- Card 2: Backend Development & REST APIs -->
    <g transform="translate(0, 86)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#00d2ff"/>
      <circle cx="36" cy="37" r="18" fill="#0b2e3b"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">⚡</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Backend Development &amp; REST APIs</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">Java Spring Boot, Python FastAPI, PostgreSQL, MySQL &amp; SQLAlchemy</text>
    </g>

    <!-- Card 3: AI Verification & Multi-Agent -->
    <g transform="translate(0, 172)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#ff354f"/>
      <circle cx="36" cy="37" r="18" fill="#3b1523"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🤖</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">ClarifyAI &amp; AgentIQ Verification Engines</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">Evidence retrieval, claim validation (NLI), LangGraph &amp; RAG pipelines</text>
    </g>

    <!-- Card 4: DSA & Computer Science Core -->
    <g transform="translate(0, 258)">
      <rect width="520" height="74" rx="14" fill="url(#ab_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      <rect x="0" y="0" width="4" height="74" rx="2" fill="#ffd166"/>
      <circle cx="36" cy="37" r="18" fill="#3b320d"/>
      <text x="36" y="42" text-anchor="middle" font-size="18">🧩</text>
      <text x="68" y="32" class="ab-sans" font-size="16" font-weight="700" fill="#ffffff">Data Structures &amp; Core CS Foundations</text>
      <text x="68" y="54" class="ab-sans" font-size="13" fill="#94a3b8">OOP Principles, DBMS, Operating Systems, Networks in Java, Python, C++</text>
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
      <text x="0" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">01 / SDET &amp; QA</text>

      <!-- Segment 2 -->
      <rect x="160" y="0" width="140" height="4" rx="2" fill="#1b2a47"/>
      <rect x="160" y="0" width="0" height="4" rx="2" fill="#00d2ff" class="ab-bar-2"/>
      <text x="160" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">02 / BACKEND</text>

      <!-- Segment 3 -->
      <rect x="320" y="0" width="140" height="4" rx="2" fill="#1b2a47"/>
      <rect x="320" y="0" width="0" height="4" rx="2" fill="#ff354f" class="ab-bar-3"/>
      <text x="320" y="20" class="ab-mono" font-size="11" fill="#64748b" font-weight="600">03 / EXPERIENCE</text>
    </g>

    <!-- Slide 1: SDET & Software Quality -->
    <g class="ab-slide-1" transform="translate(30, 70)">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">Software Testing &amp; Verification</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1">
        Applying strong software validation, test automation logic, and
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        semantic verification to guarantee robust, bug-free production code.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#0e1b38" stroke="#247bff" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#247bff" font-weight="700">TARGET ROLE</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">SDET / QA Engineer</text>

        <rect x="230" width="225" height="60" rx="10" fill="#0e1b38" stroke="#247bff" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#00d2ff" font-weight="700">CORE FOCUS</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">Validation &amp; Verification</text>
      </g>
    </g>

    <!-- Slide 2: ClarifyAI & Backend Architecture -->
    <g class="ab-slide-2" transform="translate(30, 70)" opacity="0">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">ClarifyAI &amp; Backend Systems</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1">
        Engineered end-to-end evidence verification pipelines classifying
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        claims with confidence scoring on FastAPI, PostgreSQL &amp; SQLAlchemy.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#0c232e" stroke="#00d2ff" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#00d2ff" font-weight="700">VERIFICATION ENGINE</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">Evidence Retrieval &amp; NLI</text>

        <rect x="230" width="225" height="60" rx="10" fill="#0c232e" stroke="#00d2ff" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#ffd166" font-weight="700">BACKEND STACK</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">Spring Boot &amp; FastAPI</text>
      </g>
    </g>

    <!-- Slide 3: Industry Experience & Training -->
    <g class="ab-slide-3" transform="translate(30, 70)" opacity="0">
      <text x="0" y="28" class="ab-sans" font-size="24" font-weight="800" fill="#ffffff">Industry Internships &amp; Training</text>
      <text x="0" y="60" class="ab-sans" font-size="14" fill="#cbd5e1">
        Hands-on experience at Codec Technologies (AI Intern) and IBM
      </text>
      <text x="0" y="82" class="ab-sans" font-size="14" fill="#cbd5e1">
        SkillsBuild (GenAI &amp; Cloud), shipping verified software solutions.
      </text>

      <!-- Highlight Chips -->
      <g transform="translate(0, 115)">
        <rect width="215" height="60" rx="10" fill="#290e1b" stroke="#ff354f" stroke-width="1"/>
        <text x="16" y="26" class="ab-mono" font-size="12" fill="#ff354f" font-weight="700">CODEC TECH</text>
        <text x="16" y="46" class="ab-sans" font-size="13" fill="#ffffff">AI &amp; Data Validation Intern</text>

        <rect x="230" width="225" height="60" rx="10" fill="#290e1b" stroke="#ff354f" stroke-width="1"/>
        <text x="246" y="26" class="ab-mono" font-size="12" fill="#ff758c" font-weight="700">IBM SKILLSBUILD</text>
        <text x="246" y="46" class="ab-sans" font-size="13" fill="#ffffff">GenAI &amp; Cloud Fundamentals</text>
      </g>
    </g>
  </g>
</svg>"""

(ASSETS / "about-life.svg").write_text(about_svg, encoding="utf-8")
print("[OK] Created assets/about-life.svg")

# ==============================================================================
# 3. STACK.SVG (Technical Skills Taxonomy from Updated Resume)
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
    <text x="0" y="0" class="st-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 03 // TECHNICAL SKILLS &amp; QA STACK</text>
  </g>

  <!-- Left Side: 3 Tilted Elliptical Orbits with Core Node & Tech Icons -->
  <g transform="translate(0, 10)">
    <!-- Glow behind orbit core -->
    <circle cx="320" cy="235" r="140" fill="url(#st_blueGlow)"/>

    <!-- Orbit 1: Outer Orbit (Databases & Tools) -->
    <g transform="rotate(-15 320 235)">
      <ellipse cx="320" cy="235" rx="260" ry="110" fill="none" stroke="#1b305c" stroke-width="1.5" stroke-dasharray="6 6"/>
      <g transform="translate(80, 210)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#00758F" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="10" font-weight="700" fill="#00758F">MySQL</text>
      </g>
      <g transform="translate(520, 220)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#336791" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="9" font-weight="700" fill="#336791">Postgres</text>
      </g>
      <g transform="translate(320, 115)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#F05032" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#F05032">Git</text>
      </g>
    </g>

    <!-- Orbit 2: Mid Orbit (Languages: Java, Python, C++, SQL) -->
    <g transform="rotate(18 320 235)">
      <ellipse cx="320" cy="235" rx="190" ry="80" fill="none" stroke="#247bff" stroke-width="1.5" opacity="0.6"/>
      <g transform="translate(135, 215)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#f89820" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#f89820">Java</text>
      </g>
      <g transform="translate(465, 215)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#00599C" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="11" font-weight="700" fill="#659AD2">C++</text>
      </g>
      <g transform="translate(305, 145)">
        <circle cx="16" cy="16" r="20" fill="#0d1b33" stroke="#3776AB" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="10" font-weight="700" fill="#3776AB">Python</text>
      </g>
    </g>

    <!-- Orbit 3: Inner Orbit (Frameworks & QA) -->
    <g transform="rotate(-5 320 235)">
      <ellipse cx="320" cy="235" rx="115" ry="50" fill="none" stroke="#ff354f" stroke-width="1.5" opacity="0.7"/>
      <g transform="translate(205, 218)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#6DB33F" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="9" font-weight="700" fill="#6DB33F">Spring</text>
      </g>
      <g transform="translate(395, 218)">
        <circle cx="16" cy="16" r="18" fill="#0d1b33" stroke="#00d2ff" stroke-width="1.5"/>
        <text x="16" y="21" text-anchor="middle" class="st-sans" font-size="9" font-weight="700" fill="#00d2ff">FastAPI</text>
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
    <!-- Category 1: Languages & Core Development -->
    <g transform="translate(0, 0)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#247bff" letter-spacing="1">PROGRAMMING &amp; FRAMEWORKS</text>
      <g transform="translate(0, 28)">
        <!-- Java & Spring Boot -->
        <rect x="0" y="0" width="145" height="34" rx="8" fill="url(#st_cardBg)" stroke="#6DB33F" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="16" cy="17" r="4" fill="#6DB33F"/>
        <text x="30" y="22" class="st-sans" font-size="12.5" font-weight="600" fill="#ffffff">Java • Spring Boot</text>

        <!-- Python & FastAPI -->
        <rect x="155" y="0" width="135" height="34" rx="8" fill="url(#st_cardBg)" stroke="#009688" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="171" cy="17" r="4" fill="#009688"/>
        <text x="185" y="22" class="st-sans" font-size="12.5" font-weight="600" fill="#ffffff">Python • FastAPI</text>

        <!-- C++ & DSA -->
        <rect x="300" y="0" width="105" height="34" rx="8" fill="url(#st_cardBg)" stroke="#00599C" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="316" cy="17" r="4" fill="#659AD2"/>
        <text x="330" y="22" class="st-sans" font-size="12.5" font-weight="600" fill="#ffffff">C++ • DSA</text>

        <!-- React.js / Node -->
        <rect x="415" y="0" width="85" height="34" rx="8" fill="url(#st_cardBg)" stroke="#61DAFB" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="428" cy="17" r="4" fill="#61DAFB"/>
        <text x="440" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">React.js</text>
      </g>
    </g>

    <!-- Category 2: Software Testing & Quality Engineering -->
    <g transform="translate(0, 90)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#00d2ff" letter-spacing="1">SOFTWARE TESTING &amp; QUALITY</text>
      <g transform="translate(0, 28)">
        <!-- Software Validation -->
        <rect x="0" y="0" width="155" height="34" rx="8" fill="url(#st_cardBg)" stroke="#00d2ff" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="16" cy="17" r="4" fill="#00d2ff"/>
        <text x="30" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">Software Validation</text>

        <!-- Semantic Verification (NLI) -->
        <rect x="165" y="0" width="165" height="34" rx="8" fill="url(#st_cardBg)" stroke="#ffd166" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="181" cy="17" r="4" fill="#ffd166"/>
        <text x="195" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">Semantic Verification</text>

        <!-- Debugging & Data Validation -->
        <rect x="340" y="0" width="160" height="34" rx="8" fill="url(#st_cardBg)" stroke="#ff354f" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="356" cy="17" r="4" fill="#ff354f"/>
        <text x="370" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">Debugging &amp; Model Eval</text>
      </g>
    </g>

    <!-- Category 3: Databases & AI/ML APIs -->
    <g transform="translate(0, 180)">
      <text x="0" y="16" class="st-mono" font-size="12" font-weight="700" fill="#ff354f" letter-spacing="1">DATABASES, RAG &amp; TOOLING</text>
      <g transform="translate(0, 28)">
        <!-- MySQL & PostgreSQL -->
        <rect x="0" y="0" width="160" height="34" rx="8" fill="url(#st_cardBg)" stroke="#00758F" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="16" cy="17" r="4" fill="#00758F"/>
        <text x="30" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">MySQL • PostgreSQL</text>

        <!-- LangChain & RAG -->
        <rect x="170" y="0" width="160" height="34" rx="8" fill="url(#st_cardBg)" stroke="#ffd166" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="186" cy="17" r="4" fill="#ffd166"/>
        <text x="200" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">LangGraph • RAG • LLM</text>

        <!-- Tools / Git -->
        <rect x="340" y="0" width="160" height="34" rx="8" fill="url(#st_cardBg)" stroke="#F05032" stroke-width="1" stroke-opacity="0.7"/>
        <circle cx="356" cy="17" r="4" fill="#F05032"/>
        <text x="370" y="22" class="st-sans" font-size="12" font-weight="600" fill="#ffffff">Git • VS Code • Antigravity</text>
      </g>
    </g>

    <!-- Bottom Metrics Banner -->
    <g transform="translate(0, 275)">
      <rect width="500" height="50" rx="12" fill="#0c162d" stroke="#1f335c" stroke-width="1"/>
      <text x="20" y="30" class="st-sans" font-size="13" fill="#94a3b8">
        Applying strong <tspan fill="#00d2ff" font-weight="700">programming and analytical skills</tspan> to software quality and testing.
      </text>
    </g>
  </g>
</svg>"""

(ASSETS / "stack.svg").write_text(stack_svg, encoding="utf-8")
print("[OK] Created assets/stack.svg")

# ==============================================================================
# 4. ID-DASHBOARD.SVG (Verified Resume CGPA 7.27, JSS Noida, SDET Career Objective)
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
    <text x="0" y="0" class="id-mono" font-size="13" font-weight="700" fill="#247bff" letter-spacing="2">&gt; 04 // DEVELOPER PASS &amp; VERIFIED CREDENTIALS</text>
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
        <image href="{id_b64}" x="85" y="90" width="230" height="170" preserveAspectRatio="xMidYMid slice"/>
      </g>
      <rect x="85" y="95" width="230" height="150" rx="12" fill="none" stroke="#247bff" stroke-width="1" opacity="0.6"/>

      <!-- Cardholder Details -->
      <text x="85" y="272" class="id-sans" font-size="20" font-weight="900" fill="#ffffff">ABHIJAT PATEL</text>
      <text x="85" y="292" class="id-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1">SDET &amp; SOFTWARE ENGINEER</text>
      
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
      <!-- Card 1: Verified CGPA -->
      <g transform="translate(0, 0)">
        <rect width="245" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#247bff"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#247bff">VERIFIED ACADEMIC</text>
        <text x="24" y="60" class="id-sans" font-size="22" font-weight="800" fill="#ffffff">7.27 / 10.0</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">B.Tech IT • 2023–2027</text>
      </g>

      <!-- Card 2: Industry Internship -->
      <g transform="translate(265, 0)">
        <rect width="245" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#ff354f"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#ff354f">INTERNSHIP EXP</text>
        <text x="24" y="60" class="id-sans" font-size="20" font-weight="800" fill="#ffffff">Codec Tech</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">AI Intern + IBM SkillsBuild</text>
      </g>

      <!-- Card 3: Target Role -->
      <g transform="translate(530, 0)">
        <rect width="230" height="100" rx="14" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
        <rect x="0" y="0" width="4" height="100" rx="2" fill="#00e676"/>
        <text x="24" y="32" class="id-mono" font-size="11" font-weight="700" fill="#00e676">TARGET ROLE</text>
        <text x="24" y="60" class="id-sans" font-size="19" font-weight="800" fill="#ffffff">SDET / Backend</text>
        <text x="24" y="82" class="id-sans" font-size="12" fill="#94a3b8">Software Quality &amp; Dev</text>
      </g>
    </g>

    <!-- Bottom Row: Education & Milestone Overview -->
    <g transform="translate(0, 120)">
      <rect width="760" height="205" rx="16" fill="url(#id_cardBg)" stroke="#1a2d52" stroke-width="1.2"/>
      
      <!-- Education Section -->
      <g transform="translate(30, 25)">
        <text x="0" y="16" class="id-mono" font-size="12" font-weight="700" fill="#247bff" letter-spacing="1">ACADEMIC &amp; ENGINEERING CREDENTIALS</text>
        
        <text x="0" y="48" class="id-sans" font-size="18" font-weight="800" fill="#ffffff">Bachelor of Technology (B.Tech) — Information Technology</text>
        <text x="0" y="74" class="id-sans" font-size="14" fill="#cbd5e1">🏛️ JSS Academy of Technical Education, Noida • CGPA: 7.27/10</text>
        <text x="0" y="98" class="id-sans" font-size="13" fill="#94a3b8">📜 Certifications: TCS iON Communication Skills • IBM SkillsBuild GenAI • Codec Tech AI</text>
      </g>

      <line x1="30" y1="138" x2="730" y2="138" stroke="#1b2d4d" stroke-width="1"/>

      <!-- Engineering Roadmap Goals -->
      <g transform="translate(30, 155)">
        <text x="0" y="16" class="id-mono" font-size="11" font-weight="700" fill="#00d2ff">CAREER OBJECTIVE:</text>
        <text x="0" y="36" class="id-sans" font-size="13" fill="#ffffff">
          "Applying strong programming in Java, Python, C++, and analytical skills to software quality, testing, and backend engineering."
        </text>
      </g>
    </g>
  </g>
</svg>"""

(ASSETS / "id-dashboard.svg").write_text(id_dash_svg, encoding="utf-8")
print("[OK] Created assets/id-dashboard.svg")

# ==============================================================================
# 5. CONNECT.SVG (Accurate Instagram @theabhijatpatel, Portfolio & Links)
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
        Open for SDET, Software Testing, Backend Engineering &amp; AI Opportunities!
      </text>
    </g>

    <!-- Social Grid Cards (4 High-Impact Cards) -->
    <g transform="translate(0, 95)">
      <!-- 1. GitHub Card -->
      <g transform="translate(0, 0)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#247bff" stroke-width="1.2"/>
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
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#00d2ff">/in/abhijatpatel01</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#00d2ff">→</text>
      </g>

      <!-- 3. Portfolio Card -->
      <g transform="translate(0, 105)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#00e676" stroke-width="1.2"/>
        <circle cx="36" cy="45" r="20" fill="#0b2e1f"/>
        <text x="36" y="52" text-anchor="middle" class="cn-sans" font-size="16" font-weight="900" fill="#00e676">🌐</text>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">Portfolio Website</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#00e676">Live Projects &amp; Demos</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#00e676">→</text>
      </g>

      <!-- 4. Instagram Card -->
      <g transform="translate(290, 105)">
        <rect width="270" height="90" rx="14" fill="url(#cn_cardBg)" stroke="#E4405F" stroke-width="1.2"/>
        <circle cx="36" cy="45" r="20" fill="#E4405F"/>
        <text x="36" y="52" text-anchor="middle" class="cn-sans" font-size="16" font-weight="900" fill="#ffffff">📷</text>
        
        <text x="68" y="38" class="cn-sans" font-size="15" font-weight="700" fill="#ffffff">Instagram</text>
        <text x="68" y="58" class="cn-mono" font-size="12" fill="#ff758c">@theabhijatpatel</text>
        <text x="240" y="52" class="cn-sans" font-size="18" fill="#ff758c">→</text>
      </g>
    </g>

    <!-- Interactive Links Notice -->
    <g transform="translate(0, 312)">
      <text x="0" y="0" class="cn-mono" font-size="11" fill="#64748b">
        💡 <tspan fill="#cbd5e1">Clickable badges and project links are available directly below.</tspan>
      </text>
    </g>
  </g>
</svg>"""

(ASSETS / "connect.svg").write_text(connect_svg, encoding="utf-8")
print("[OK] Created assets/connect.svg")

# ==============================================================================
# 6. ROOT README.MD (With updated ClarifyAI, CampusConnect, AgentIQ & SDET profile)
# ==============================================================================
readme_content = """<div align="center">

# ⚡ ABHIJAT PATEL
### SDET & Software Quality Engineer • Java Spring Boot & FastAPI • Multi-Agent AI & Verification

![Hero](./assets/hero.svg?v=1)

![About](./assets/about-life.svg?v=1)

![Stack](./assets/stack.svg?v=1)

![Developer ID](./assets/id-dashboard.svg?v=1)

![Connect](./assets/connect.svg?v=1)

</div>

---

## 🚀 Featured Projects

| Project | Description | Stack & Architecture | Links |
| :--- | :--- | :--- | :---: |
| 🎓 **CampusConnect** | **AI-Powered Placement & Resume Matching Portal**<br/>• Developed a Java Spring Boot and MySQL backend for managing student profiles, company job postings, and applications.<br/>• Built an end-to-end software workflow connecting student/company profiles, job postings, an AI microservice, ranking engine, and recruiter dashboard.<br/>• Designed a priority-based ranking algorithm using DSA and an NLP microservice to calculate resume-to-job-description similarity and rank candidates.<br/>• Worked across Java backend, Python services, database operations, and frontend components while validating end-to-end application workflows. | `Java` `Spring Boot` `MySQL` `React` `Python` `AI/NLP` `DSA` | [GitHub](https://github.com/AbhijatPatel) |
| 🔍 **ClarifyAI** | **Confidence-Scored, Source-Verified Answer Engine**<br/>• Developed an end-to-end verification pipeline covering evidence retrieval, answer generation, claim extraction, evidence-claim matching, confidence scoring, and verified output.<br/>• Built a modular FastAPI backend with PostgreSQL and SQLAlchemy and implemented validation logic to classify claims as *Supported*, *Contradicted*, or *Insufficient*.<br/>• Engineered confidence-scoring mechanisms using evidence relevance, semantic support, contradiction signals, and source quality.<br/>• Debugged and validated software components across the verification pipeline. | `Python` `FastAPI` `PostgreSQL` `SQLAlchemy` `LLM APIs` `NLI` | [GitHub](https://github.com/AbhijatPatel) |
| 🤖 **AgentIQ** | **Autonomous Multi-Agent Research & Task Assistant**<br/>• Developed a multi-agent software pipeline consisting of planning, research, writing, and critique stages.<br/>• Implemented RAG and web-search retrieval to validate and ground generated outputs.<br/>• Developed a self-critique workflow in which generated drafts are reviewed and revised before producing the final report.<br/>• Exposed the application through FastAPI and developed a React dashboard for monitoring agent workflows and tool calls. | `Python` `LangChain` `LangGraph` `LLM APIs` `RAG` `FastAPI` `React` | [GitHub](https://github.com/AbhijatPatel) |
| 🌐 **Developer Portfolio** | **Interactive Modern Engineering Portfolio**<br/>High-performance developer showcase highlighting production projects, technical capabilities, interactive demos, and contact integration. | `HTML5` `CSS3` `JavaScript` `Responsive UI` | [Live Site](https://abhijatpatel.github.io/My-Portfolio-Website/) • [GitHub](https://github.com/AbhijatPatel) |

---

## 💼 Industry Experience & Education

- 🏢 **Artificial Intelligence Intern** — *Codec Technologies Pvt. Ltd.* (Jun 2026 – Jul 2026)
  - Applied Python and core AI/ML concepts across practical modules and real-world tasks.
  - Worked on projects involving data preprocessing and model evaluation, strengthening validation, debugging, and analytical problem-solving skills.
  - Developed and evaluated software-based solutions using Python.
- ☁️ **GenAI & Cloud Computing Intern** — *IBM SkillsBuild AICTE–BharatCares Program*
  - Gained industry-aligned exposure to Generative AI, AI tools, and cloud computing fundamentals.
  - Completed structured modules involving cloud fundamentals and practical GenAI use cases.
- 🎓 **Bachelor of Technology (B.Tech) in Information Technology** (2023 – 2027)
  - *JSS Academy of Technical Education, Noida* | **CGPA: 7.27 / 10**
- 📜 **Certifications**:
  - Communication Skills — *TCS iON, Tata Consultancy Services*
  - GenAI & Cloud Computing Internship — *IBM SkillsBuild, AICTE–BharatCares*
  - Artificial Intelligence Internship Certificate — *Codec Technologies Pvt. Ltd.*

---

## 🔗 Connect With Me

<div align="center">

<a href="https://github.com/AbhijatPatel" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-AbhijatPatel-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
&nbsp;
<a href="https://linkedin.com/in/abhijatpatel01" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-abhijatpatel01-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
&nbsp;
<a href="https://abhijatpatel.github.io/My-Portfolio-Website/" target="_blank">
  <img src="https://img.shields.io/badge/Portfolio-Live_Demo-00E676?style=for-the-badge&logo=googlechrome&logoColor=black" alt="Portfolio"/>
</a>
&nbsp;
<a href="https://www.instagram.com/theabhijatpatel" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-@theabhijatpatel-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/>
</a>
&nbsp;
<a href="mailto:abhijatpatelfaizabad@gmail.com" target="_blank">
  <img src="https://img.shields.io/badge/Email-Get_in_Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
</a>

<br/><br/>

```bash
npx abhijat-patel
```

---

<p align="center">
  <b>VALIDATE • TEST • BUILD • SCALE</b><br/>
  <i>Crafted with precision for Abhijat Patel</i>
</p>

</div>
"""

(ROOT / "README.md").write_text(readme_content, encoding="utf-8")
print("[OK] Created README.md")

# ==============================================================================
# 7. PREVIEW.HTML (Interactive local preview)
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
    .card img {
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
