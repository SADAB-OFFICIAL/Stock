import re

with open('www/index.html', 'r') as f:
    content = f.read()

# Fix 1: initSMSForwarder parsing
old_restore_logic = r"if \(data && !error\) \{[\s\S]*?localStorage\.setItem\('stockflow_sms_state_' \+ userEmail, JSON\.stringify\(cloudState\)\);\s*\}"
new_restore_logic = """if (data && !error) {
                        if (data.bank_number) bankInput.value = data.bank_number;
                        
                        // Parse settings if it's a JSON column
                        let parsedState = data.settings || {};
                        if (typeof parsedState === 'string') {
                            try { parsedState = JSON.parse(parsedState); } catch(e){}
                        }
                        
                        if (document.getElementById('toggle-forward')) document.getElementById('toggle-forward').checked = !!(data.toggle_forward || parsedState['toggle-forward']);
                        if (document.getElementById('toggle-startup')) document.getElementById('toggle-startup').checked = !!(data.toggle_startup || parsedState['toggle-startup']);
                        if (document.getElementById('toggle-battery')) document.getElementById('toggle-battery').checked = !!(data.toggle_battery || parsedState['toggle-battery']);
                        if (document.getElementById('toggle-hide')) document.getElementById('toggle-hide').checked = !!(data.toggle_hide || parsedState['toggle-hide']);
                        if (document.getElementById('toggle-cactus')) document.getElementById('toggle-cactus').checked = !!(data.toggle_cactus || parsedState['toggle-cactus']);

                        // Sync back to local storage
                        const cloudState = {
                            bankNumber: data.bank_number || parsedState.bankNumber,
                            'toggle-forward': !!(data.toggle_forward || parsedState['toggle-forward']),
                            'toggle-startup': !!(data.toggle_startup || parsedState['toggle-startup']),
                            'toggle-battery': !!(data.toggle_battery || parsedState['toggle-battery']),
                            'toggle-hide': !!(data.toggle_hide || parsedState['toggle-hide']),
                            'toggle-cactus': !!(data.toggle_cactus || parsedState['toggle-cactus'])
                        };
                        localStorage.setItem('stockflow_sms_state_' + userEmail, JSON.stringify(cloudState));
                    }"""
content = re.sub(old_restore_logic, new_restore_logic, content)

# Fix 2: Upsert logic
old_upsert_logic = r"await window\._supabase\.from\('sms_settings'\)\.upsert\(\{\s*user_email:\s*userEmail,\s*bank_number:\s*bankInput\.value,\s*settings:\s*state\s*\}\);"
new_upsert_logic = """await window._supabase.from('sms_settings').upsert({
                        user_email: userEmail,
                        bank_number: bankInput.value,
                        settings: state,
                        toggle_forward: state['toggle-forward'],
                        toggle_startup: state['toggle-startup'],
                        toggle_battery: state['toggle-battery'],
                        toggle_hide: state['toggle-hide'],
                        toggle_cactus: state['toggle-cactus']
                    });"""
content = re.sub(old_upsert_logic, new_upsert_logic, content)

with open('www/index.html', 'w') as f:
    f.write(content)
with open('../starpay/starpay.html', 'w') as f:
    f.write(content)
print("Fixed.")
