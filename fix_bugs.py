import re

with open('www/index.html', 'r') as f:
    content = f.read()

# 1. Fix Hardcoded 9.00 INR -> 0.00 INR
content = content.replace('id="home-balance">9.00 INR', 'id="home-balance">0.00 INR')
content = content.replace('id="security-deposit-amt">9.00 INR', 'id="security-deposit-amt">0.00 INR')

# 2. Add a sleek Toast function and replace showSellToast() logic
toast_css = """
        /* Sleek Premium Toast */
        #premium-toast {
            position: fixed;
            top: -100px;
            left: 50%;
            transform: translateX(-50%);
            background: #172033;
            color: #fff;
            padding: 12px 20px;
            border-radius: 50px;
            font-size: 11px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            z-index: 99999;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(244, 201, 40, 0.2);
            white-space: nowrap;
        }
        #premium-toast.show {
            top: 50px;
        }
        #premium-toast i {
            color: #F4C928;
            font-size: 14px;
        }
"""
content = content.replace('</style>', toast_css + '</style>')

toast_html = """
    <!-- Premium Toast -->
    <div id="premium-toast"><i class="fas fa-info-circle"></i> <span id="premium-toast-msg">Message</span></div>
"""
content = content.replace('<div id="splash-screen"', toast_html + '\n    <div id="splash-screen"')

toast_js = """
    function showPremiumToast(msg) {
        const toast = document.getElementById('premium-toast');
        const toastMsg = document.getElementById('premium-toast-msg');
        if(!toast || !toastMsg) return;
        toastMsg.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }
    
    function showSellToast() {
        showPremiumToast('Please deposit and buy USDT first!');
    }
"""

# Replace old showSellToast
old_sell_toast = r'function showSellToast\(\)\s*\{\s*showModal\([^\)]+\);\s*\}'
content = re.sub(old_sell_toast, toast_js, content)

with open('www/index.html', 'w') as f:
    f.write(content)
with open('../starpay/starpay.html', 'w') as f:
    f.write(content)

print("Bugs fixed.")
