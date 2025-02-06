import time
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simuler une base de données d'abonnés avec segmentation
subscribers = {
    "user1": {"last_active": datetime.now(), "purchased": False, "preferences": "vidéos exclusives"},
    "user2": {"last_active": datetime.now() - timedelta(days=5), "purchased": True, "preferences": "photos VIP"},
    "user3": {"last_active": datetime.now() - timedelta(days=10), "purchased": False, "preferences": "contenu interactif"},
}

# Messages automatisés avec personnalisation
def send_welcome_message(user, preference):
    return f"Hey {user} 💖 ! Bienvenue ! J'ai des {preference} juste pour toi 😏. Dis-moi ce que tu aimerais voir !"

def send_paywall_offer(user):
    return f"J’ai une surprise pour toi... 🔥 Veux-tu un aperçu ? Réponds 'OUI' pour débloquer un contenu exclusif 😉."

def send_inactive_reminder(user):
    return f"Hey {user} 😘, tu me manques ! J'ai du nouveau contenu qui pourrait te plaire 😏. Viens vite voir !"

# Automatisation des réponses avec mots-clés et gestion des emojis
def chatbot_response(user, message):
    if "OUI" in message.upper():
        return f"Super {user} ! Voici ton lien exclusif 🔥 [Lien Payant]"
    elif "MERCI" in message.upper():
        return "Avec plaisir 😘 ! Tu veux encore plus d'exclusivité ? Fais-moi signe 💖."
    elif "CONTENU" in message.upper():
        return send_paywall_offer(user)
    else:
        return "Je ne suis pas sûr de comprendre... Essaye 'OUI' pour découvrir du contenu exclusif ! 😏"

# Vérification et relance des abonnés inactifs
def check_inactive_users():
    for user, data in subscribers.items():
        if data["last_active"] < datetime.now() - timedelta(days=7) and not data["purchased"]:
            print(send_inactive_reminder(user))

# API Endpoint pour Railway
@app.route("/message", methods=["POST"])
def handle_message():
    data = request.json
    user = data.get("user")
    message = data.get("message")
    response = chatbot_response(user, message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
