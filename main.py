from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
 

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Henry Panel 2.0</title>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Kaushan+Script&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: linear-gradient(to right, #9932CC, #FF00FF);
      color: #fff;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      overflow-x: hidden;
      animation: fadeInBody 1s ease-in;
    }

    @keyframes fadeInBody {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    header {
      text-align: center;
      padding: 2rem;
      background: #1a1a2e;
      box-shadow: 0 0 20px #ff69b4;
    }

    header h1 {
      font-size: 3.2rem;
      color: #FFFFFF;
      text-shadow: 0 0 15px #FFFFFF, 0 0 30px #f0f;
      animation: pulse 2s infinite alternate;
    }

    @keyframes pulse {
      0% { text-shadow: 0 0 10px #ff69b4; }
      100% { text-shadow: 0 0 25px #ff69b4, 0 0 50px #f0f; }
    }

    .hero {
      text-align: center;
      padding: 3rem 1rem;
      animation: slideUp 1.5s ease-out;
    }

    @keyframes slideUp {
      from { transform: translateY(50px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .hero img {
      width: 380px;
      height: 240px;
      object-fit: cover;
      border: 6px solid #FFFFFF;
      box-shadow: 0 0 30px #FFFFFF;
      margin-bottom: 1rem;
      border-radius: 20px;
    }

    .hero p {
      font-size: 1.4rem;
      color: #FFFFFF;
      max-width: 600px;
      margin: 0 auto;
      padding: 1rem;
      line-height: 1.8;
    }

    .section {
      padding: 3rem 1rem;
      text-align: center;
    }

    .card {
      background: rgba(255, 105, 180, 0.1);
      border: 2px dashed #FFFFFF;
      border-radius: 20px;
      padding: 2rem;
      margin: 1.5rem auto;
      max-width: 500px;
      box-shadow: 0 0 20px #FFFFFF;
      transition: transform 0.4s ease;
      animation: fadeIn 1.5s ease forwards;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    .card:hover {
      transform: scale(1.05) rotate(1deg);
      box-shadow: 0 0 35px #FFFFFF;
    }

    .card h2 {
      font-size: 1.8rem;
      color: #fff;
      margin-bottom: 1rem;
    }

    .card p {
      color: #ff693;
      font-size: 1rem;
    }

    .btn {
      display: inline-block;
      margin-top: 1.2rem;
      padding: 0.7rem 1.5rem;
      background: linear-gradient(to right, #FFFFFF, #ff85c1);
      color: #000;
      border: none;
      border-radius: 50px 10px 50px 10px;
      font-weight: bold;
      font-family: 'Orbitron', sans-serif;
      text-decoration: none;
      box-shadow: 0 0 15px #FFFFFF;
      transition: all 0.3s ease;
    }

    .btn:hover {
      background: linear-gradient(to right, #ff85c1, #FFFFFF);
      box-shadow: 0 0 25px #FFFFFF, 0 0 40px #f0f;
      transform: scale(1.05);
    }

    footer {
      text-align: center;
      padding: 1.5rem;
      background: #1a1a2e;
      color: #ffb6d9;
      font-size: 0.85rem;
      border-top: 2px solid #FFFFFF;
    }
  </style>
</head>
<body>
  <header>
    <h1>𝗧𝗜𝗧𝗔𝗡-𝗫 2.0</h1>
  </header>

  <section class="hero">
    <img src="https://i.imgur.com/vR84jKy.jpeg" alt="Queen Shehara" />
  </section>

  <section class="section">
    <div class="card">
      <h2>Free Convo 2.0</h2>
      <p>Get Free Users Offline Convo Server By Owner Henry x Yuvi ! ... God Abusers Fucked By Owner Henry x Yuvi..!</p>
      <a class="btn" href="https://free-2-0.onrender.com">Start Servers</a>
    </div>

   
  
    <div class="card">
      <h2>Paid Servers</h2>
      <p>Get Paid Servers By Owner Henry x yuvi Inxide First Contact him !</p>
      <a class="btn" href="https://blank-page-henrykingherw-546912e5.koyeb.app/" target="_blank">Start Servers</a>
    </div>
  </section>

  <footer>
    © 2025 LAGEND HENRY X YUVI | All rights reserved 💫
  </footer>
</body>
</html>
 '''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
