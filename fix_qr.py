import re

with open('www/index.html', 'r') as f:
    content = f.read()

# Update applyQRDataToUI to handle multiple elements
old_apply = r"function applyQRDataToUI\(data\) \{[\s\S]*?// Dynamic display of amount on the cards"

new_apply = """function applyQRDataToUI(data) {
        if (!data) return;
        const depositAddress = data.upi_id || 'TQnnheFj6dSxHCAdeHh8wTmeyP8wh8XQpa';
        const depositName = data.merchant_name || 'E08';
        const depositNetwork = data.bank_name || 'USDT-TRC20';
        let qrUrl = data.qr_code_url || data.qr_url || '';

        const autoGenQr = `https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${encodeURIComponent(depositAddress)}`;

        if (!qrUrl || qrUrl.trim() === '') {
            qrUrl = autoGenQr;
        }

        // Update ALL QR Images
        document.querySelectorAll('[id="deposit-qr-img"]').forEach(qrImg => {
            qrImg.onerror = function() {
                this.onerror = null;
                this.src = autoGenQr;
            };
            qrImg.src = qrUrl;
        });

        // Update ALL addresses
        document.querySelectorAll('[id="confirm-deposit-address"], [id="qr-upi-id-text"]').forEach(el => {
            el.innerText = depositAddress;
        });
        
        // Update ALL Merchant/Name displays
        document.querySelectorAll('[id="deposit-name-display"], [id="qr-merchant-text"]').forEach(el => {
            el.innerText = depositName;
        });

        // Update ALL Network/Bank displays
        document.querySelectorAll('[id="deposit-network-display"]').forEach(el => {
            el.innerText = depositNetwork;
        });

        // Dynamic display of amount on the cards"""

content = re.sub(old_apply, new_apply, content)

with open('www/index.html', 'w') as f:
    f.write(content)
with open('../starpay/starpay.html', 'w') as f:
    f.write(content)

print("QR logic updated for multiple IDs.")
