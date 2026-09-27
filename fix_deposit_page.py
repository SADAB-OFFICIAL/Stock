import re

with open('www/index.html', 'r') as f:
    content = f.read()

# 1. Fix the deposit page styling (remove popup shadow and centering restriction)
old_deposit_div = r'<div class="w-full max-w-\[400px\] mx-auto bg-white min-h-screen relative shadow-\[0_0_20px_rgba\(0,0,0,0\.5\)\] overflow-x-hidden flex flex-col">'
new_deposit_div = '<div class="w-full bg-white min-h-screen relative overflow-x-hidden flex flex-col">'
content = re.sub(old_deposit_div, new_deposit_div, content)

# 2. Revert the Sell Now toast back to the big modal
old_toast_js = r"function showSellToast\(\) \{\s*showPremiumToast\([^\)]+\);\s*\}"
new_toast_js = """function showSellToast() {
        showModal('Deposit Required', 'Please deposit and buy USDT first! Click on the Deposit button to proceed.', 'fa-exclamation-circle text-amber-500');
    }"""
content = re.sub(old_toast_js, new_toast_js, content)

with open('www/index.html', 'w') as f:
    f.write(content)
with open('../starpay/starpay.html', 'w') as f:
    f.write(content)

print("Deposit page fixed and modal restored.")
