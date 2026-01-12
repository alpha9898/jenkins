from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

# Optional: Set your GitHub webhook secret here for security
GITHUB_WEBHOOK_SECRET = None  # e.g., "your-secret-here"

@app.route("/")
def home():
    return "Jenkins CI Pipeline is working!"

@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    """Webhook endpoint to receive GitHub events"""
    
    # Get the event type from GitHub headers
    event_type = request.headers.get("X-GitHub-Event", "unknown")
    delivery_id = request.headers.get("X-GitHub-Delivery", "unknown")
    
    data = request.json
    
    print(f"\n{'='*50}")
    print(f"GitHub Event: {event_type}")
    print(f"Delivery ID: {delivery_id}")
    
    if event_type == "push":
        # Handle push event
        repo = data.get("repository", {}).get("full_name", "unknown")
        branch = data.get("ref", "").replace("refs/heads/", "")
        pusher = data.get("pusher", {}).get("name", "unknown")
        commits = data.get("commits", [])
        
        print(f"Repository: {repo}")
        print(f"Branch: {branch}")
        print(f"Pushed by: {pusher}")
        print(f"Commits: {len(commits)}")
        
        for commit in commits:
            print(f"  - {commit.get('id', '')[:7]}: {commit.get('message', '')}")
        
        # Add your custom logic here (e.g., trigger Jenkins build)
        
    elif event_type == "ping":
        # GitHub sends a ping when webhook is first created
        print("Ping received! Webhook is configured correctly.")
        
    elif event_type == "pull_request":
        action = data.get("action", "unknown")
        pr = data.get("pull_request", {})
        print(f"PR #{pr.get('number')}: {action}")
        print(f"Title: {pr.get('title')}")
    
    print(f"{'='*50}\n")
    
    return jsonify({
        "status": "success",
        "event": event_type,
        "message": f"GitHub {event_type} event received!"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)