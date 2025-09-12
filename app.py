from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Flask CI/CD Demo</title>
        <style>
          body { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            background-color: #fdf6f0; 
            font-size: 60px;
          }
          .spin {
            display: inline-block;
            animation: spin 3s linear infinite;
          }
          @keyframes spin {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        </style>
      </head>
      <body>
        <div>
          <span class="spin">🐱</span>  
          <p style="font-size:50px; text-align:center;">CI/CD Pipeline is purr-fect! 🐾</p>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
