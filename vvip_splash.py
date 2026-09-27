import re

with open('www/index.html', 'r') as f:
    content = f.read()

# Replace the Splash Screen HTML block
old_splash = r'<!-- SPLASH SCREEN -->[\s\S]*?</div>\s*</div>'
new_splash = """<!-- VVIP PREMIUM SPLASH SCREEN -->
    <div id="splash-screen" class="fixed inset-0 bg-[#070A11] z-[999999] flex flex-col items-center justify-center transition-opacity duration-1000 ease-out overflow-hidden w-full h-full m-0 p-0">
        <!-- Luxury Animated Background Elements -->
        <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-gradient-to-br from-[#F4C928]/5 to-transparent rounded-full blur-[100px] pointer-events-none -mr-[250px] -mt-[250px]"></div>
        <div class="absolute bottom-0 left-0 w-[400px] h-[400px] bg-gradient-to-tr from-[#5B8DEF]/10 to-transparent rounded-full blur-[100px] pointer-events-none -ml-[200px] -mb-[200px]"></div>

        <div class="logo-container transform scale-95 opacity-0 transition-all duration-[1200ms] ease-out relative w-full px-8 flex flex-col items-center">
            
            <!-- VVIP Golden Logo -->
            <div class="relative mb-6">
                <div class="absolute inset-0 bg-[#F4C928] rounded-full blur-[40px] opacity-20 pulse-glow"></div>
                <div class="w-28 h-28 bg-gradient-to-br from-[#FCD535] to-[#D4A017] rounded-[28px] flex items-center justify-center transform rotate-12 shadow-[0_20px_50px_rgba(244,201,40,0.25)] relative z-10 mx-auto border border-[#F4C928]/30">
                    <i class="fas fa-chart-line text-[#0B0F19] text-5xl -rotate-12"></i>
                </div>
            </div>

            <!-- Sleek Text -->
            <h1 class="text-[44px] font-black text-white tracking-tight mt-4 text-center drop-shadow-lg leading-none font-sans">
                STOCK<span class="text-[#F4C928]">FLOW</span>
            </h1>
            <p class="text-[11px] font-bold text-[#F4C928]/70 tracking-[0.3em] uppercase mt-4 text-center">
                Pure Gaming Fund
            </p>
            
            <!-- VVIP Sleek Loading Bar -->
            <div class="w-48 h-[2px] bg-white/10 rounded-full mt-12 overflow-hidden relative">
                <div class="absolute top-0 left-0 h-full bg-gradient-to-r from-transparent via-[#F4C928] to-transparent w-full loading-bar-anim"></div>
            </div>
        </div>
    </div>"""
content = re.sub(old_splash, new_splash, content, count=1)

# Add loading-bar CSS if not exists
if 'loading-bar-anim' not in content:
    css = """
        .loading-bar-anim {
            animation: loadingBar 2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }
        @keyframes loadingBar {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        .vvip-fade-out {
            opacity: 0;
            pointer-events: none;
        }
"""
    content = content.replace('</style>', css + '</style>')

# Update JS logic to use VVIP fade out and longer duration
old_js = """// 2. Animate Out and Remove
        setTimeout(() => {
            splash.classList.add('splash-out');
            document.body.style.overflow = ''; // Restore scroll
            setTimeout(() => splash.remove(), 700);
        }, 2200);"""
new_js = """// 2. Animate Out and Remove (VVIP)
        setTimeout(() => {
            splash.classList.add('vvip-fade-out');
            document.body.style.overflow = ''; // Restore scroll
            setTimeout(() => splash.remove(), 1000);
        }, 2800);"""
content = content.replace(old_js, new_js)

with open('www/index.html', 'w') as f:
    f.write(content)
with open('../starpay/starpay.html', 'w') as f:
    f.write(content)

print("VVIP Splash added.")
