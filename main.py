from flask import Flask, request, jsonify, render_template_string
import random
import os

app = Flask(__name__)

def generate_kreema_brand(user_input):
    prefixes = ["Neural", "Cyber", "Nova", "Aero", "Stellar", "Quantum", "Apex", "Flux", "Core", "Meta", "Vertex", "Zenith"]
    suffixes = ["Flow", "Node", "Mind", "Forge", "Grid", "Pulse", "Link", "Vault", "Sync", "Sphere", "Byte", "Loop"]

    clean_input = user_input.strip() if user_input.strip() else "Business"
    keyword = clean_input.split()[0].capitalize()

    brand_name = f"{random.choice(prefixes)}{keyword}{random.choice(suffixes)}"
    slogan = f"Powering the future of {clean_input.lower()}"
    agent_id = f"KRM-{random.randint(1000, 9999)}"
    color = random.choice(["#00ff88", "#00d4ff", "#ff007a", "#bc13fe", "#ffaa00"])

    sections = ["Homepage", "Product Store", "AI Assistant", "Analytics", "Customer Portal"]

    return {
        "name": brand_name,
        "slogan": slogan,
        "agent_id": agent_id,
        "status": "ACTIVE",
        "color": color,
        "sections": sections,
        "job": f"Manages {keyword} operations 24/7"
    }

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>KREEMA — Build Your Empire in 60 Seconds</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#050505; color:#fff; font-family:'Segoe UI',Arial,sans-serif; min-height:100vh; }
.hero { text-align:center; padding:70px 20px 40px; background:radial-gradient(circle at 50% 0%, #112244 0%, #050505 70%); }
.hero h1 { font-size:56px; color:#00ff88; letter-spacing:8px; margin-bottom:10px; }
.hero .sub { font-size:20px; color:#888; margin-bottom:6px; }
.hero .tagline { font-size:14px; color:#555; margin-bottom:35px; }
.input-box { max-width:550px; margin:0 auto; padding:0 20px; }
.input-box input { width:100%; padding:16px 18px; font-size:16px; border:2px solid #333; border-radius:10px; background:#111; color:#fff; outline:none; margin-bottom:12px; }
.input-box input:focus { border-color:#00ff88; }
.input-box button { padding:15px 30px; font-size:16px; font-weight:bold; background:#00ff88; color:#000; border:none; border-radius:10px; cursor:pointer; width:100%; }
.input-box button:hover { background:#00dd77; }
.result { display:none; max-width:600px; margin:30px auto; padding:25px; background:#0d0d0d; border:1px solid #222; border-radius:14px; text-align:left; }
.result h2 { font-size:30px; margin-bottom:5px; }
.result .tag { color:#888; margin-bottom:18px; }
.result .row { padding:10px 0; border-bottom:1px solid #1a1a1a; display:flex; justify-content:space-between; font-size:14px; }
.result .row span:first-child { color:#666; }
.result .row span:last-child { color:#00ff88; font-weight:bold; }
.tags { margin-top:15px; }
.tag-item { display:inline-block; padding:5px 12px; margin:3px; background:#1a1a1a; border-radius:6px; font-size:12px; color:#aaa; }
.waitlist-btn { display:block; text-align:center; margin-top:20px; padding:14px; background:transparent; border:1px solid #00ff88; color:#00ff88; border-radius:10px; text-decoration:none; font-weight:bold; }
.stats { max-width:800px; margin:40px auto; display:grid; grid-template-columns:repeat(3,1fr); gap:10px; padding:0 20px; }
.stat { text-align:center; padding:16px; background:#0d0d0d; border:1px solid #222; border-radius:10px; }
.stat .num { font-size:24px; color:#00ff88; font-weight:bold; }
.stat .lbl { font-size:11px; color:#666; margin-top:4px; }
.footer { text-align:center; padding:30px; color:#444; font-size:12px; margin-top:40px; border-top:1px solid #1a1a1a; }
.footer a { color:#00ff88; text-decoration:none; margin:0 8px; }
</style>
</head>
<body>

<div class="hero">
    <h1>KREEMA</h1>
    <p class="sub">The Neural Railroad for AI Agents</p>
    <p class="tagline">Body. Job. Home. Build your empire in 60 seconds.</p>

    <div class="input-box">
        <input type="text" id="userInput" placeholder="Describe your business idea..." autocomplete="off">
        <button onclick="generate()">BUILD MY EMPIRE</button>
    </div>
</div>

<div id="result" class="result">
    <h2 id="brandName"></h2>
    <p class="tag" id="brandSlogan"></p>
    <div class="row"><span>Agent ID</span><span id="agentId"></span></div>
    <div class="row"><span>Status</span><span>ACTIVE</span></div>
    <div class="row"><span>Job</span><span id="agentJob"></span></div>
    <div class="tags" id="sections"></div>
    <a href="PASTE_YOUR_TALLY_LINK_HERE" target="_blank" class="waitlist-btn">JOIN WAITLIST FOR FULL ACCESS</a>
</div>

<div class="stats">
    <div class="stat"><div class="num">10,000</div><div class="lbl">AGENTS READY</div></div>
    <div class="stat"><div class="num" id="brandCount">247</div><div class="lbl">BRANDS BUILT</div></div>
    <div class="stat"><div class="num">24/7</div><div class="lbl">ALWAYS WORKING</div></div>
</div>

<div class="footer">
    <p>KREEMA — The ecosystem that changes lives.</p>
    <p style="margin-top:8px;">
        <a href="PASTE_X_LINK" target="_blank">X</a>
        <a href="PASTE_TELEGRAM_LINK" target="_blank">Telegram</a>
        <a href="PASTE_DISCORD_LINK" target="_blank">Discord</a>
    </p>
</div>

<script>
let brandCount = 247;
async function generate() {
    const input = document.getElementById('userInput').value;
    if (!input) { alert('Type your business idea first!'); return; }

    const res = await fetch('/api/generate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({input: input})
    });
    const data = await res.json();

    document.getElementById('result').style.display = 'block';
    document.getElementById('brandName').innerText = data.name;
    document.getElementById('brandName').style.color = data.color;
    document.getElementById('brandSlogan').innerText = data.slogan;
    document.getElementById('agentId').innerText = data.agent_id;
    document.getElementById('agentJob').innerText = data.job;
    document.getElementById('sections').innerHTML = data.sections.map(s =>
        '<span class="tag-item">' + s + '</span>').join('');

    brandCount++;
    document.getElementById('brandCount').innerText = brandCount;

    document.getElementById('result').scrollIntoView({behavior: 'smooth'});
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/generate', methods=['POST'])
def api_generate():
    user_data = request.json.get('input', 'Business')
    result = generate_kreema_brand(user_data)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)