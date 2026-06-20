import re

with open('admin_logic.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace onAuthStateChanged block
pattern = re.compile(r'onAuthStateChanged\(auth,user=>\{.*?\n\}\);', re.DOTALL)
replacement = '''// Bypass login para el TFM
document.getElementById('login-screen').classList.add('hidden');
document.getElementById('app-container').classList.remove('hidden');
setStatus('ok','Conectado V');
console.log('Auth bypassed for TFM');
startListeners();
setTimeout(()=>window.setTab('calendar_all'),100);'''

new_content = pattern.sub(replacement, content)

# Replace Frida Nails with UNIR
new_content = new_content.replace('Frida Nails', 'UNIR')
new_content = new_content.replace('FridaNails', 'UNIR')

with open('admin_logic.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
