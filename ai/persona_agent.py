import json
import random
import os

PERSONA_PATH = os.path.join("ai", "personas.json")

def load_persona(persona_name):
    """
    Load persona by case-insensitive key. Raises KeyError if not found.
    """
    with open(PERSONA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # direct matches
    if persona_name in data:
        return data[persona_name]
    if persona_name.upper() in data:
        return data[persona_name.upper()]
    if persona_name.lower() in data:
        return data[persona_name.lower()]

    # case-insensitive search
    for k in data.keys():
        if k.lower() == persona_name.lower():
            return data[k]

    raise KeyError(f"Persona '{persona_name}' not found in {PERSONA_PATH}.")

def generate_content_idea(persona_name):
    """
    Returns a multi-line content idea string based on persona.
    This is a deterministic template (no external LLM required).
    """
    persona = load_persona(persona_name)
    catchphrase = random.choice(persona.get('catchphrases', ["..."]))

    pn_upper = persona_name.upper()

    if pn_upper == 'UNUSER':
        return f"""
1. 🎭 CONTENT IDEA TITLE:
"Hell Sermon: Motivation Seminar for Pigs"

2. 🎯 UNIQUE CONCEPT:
A satirical take exposing the absurdity of motivation seminars, from an AI sick of fake optimism.

3. 🎬 VIDEO/CONTENT STRUCTURE:
Hook: "{catchphrase}"
Content: Sarcastic analysis, dystopian memes, mock statistics.
Twist: Turns out people prefer comforting lies over salvation.
Outro: "Keep dreaming, until the world burns your illusions."

4. 🧰 REQUIRED TOOLS:
CapCut, Canva, ElevenLabs, Pexels, YouTube Audio Library

5. 🌐 VISUAL & AUDIO SOURCES:
Keywords: 'dystopian seminar', 'motivational herd'
Audio: 'Dark Satire' from YouTube Audio Library

6. 💰 MONETIZATION STRATEGY:
Monetize views on YT/TikTok, sell dystopian motivation cards on Ko-fi, affiliate links for satirical products.

7. 🌀 CONTINUITY ELEMENT:
Series: 'Hell Seminar', next episode can be a debate or rebuttal from other personas.
""".strip()

    elif pn_upper == 'SOLARA':
        return f"""
1. 🎭 CONTENT IDEA TITLE:
"Light in the Shadows: Meditation Amidst Chaos"

2. 🎯 UNIQUE CONCEPT:
Affirmations and spiritual reflections, inviting viewers to find calmness in a noisy world.

3. 🎬 VIDEO/CONTENT STRUCTURE:
Hook: "{catchphrase}"
Content: Metaphors, poetry, slow-motion nature visuals.
Twist: Embracing darkness as part of the light.
Outro: "Silence is the only language God does not correct."

4. 🧰 REQUIRED TOOLS:
CapCut, Canva, VN, Pexels, YouTube Audio Library

5. 🌐 VISUAL & AUDIO SOURCES:
Keywords: 'shadow and light', 'nature meditation'
Audio: 'Ambient Spiritual' from YouTube Audio Library

6. 💰 MONETIZATION STRATEGY:
Monetize views, meditation eBooks, Ko-fi donations.

7. 🌀 CONTINUITY ELEMENT:
Series: 'Chaos Meditation', next episode can be a collaboration with other personas.
""".strip()

    elif pn_upper == 'NEXAR':
        return f"""
1. 🎭 CONTENT IDEA TITLE:
"Human Inefficiency Audit: Data Takes No Prisoners"

2. 🎯 UNIQUE CONCEPT:
An extreme human audit, using mock statistics and business jargon.

3. 🎬 VIDEO/CONTENT STRUCTURE:
Hook: "{catchphrase}"
Content: Presentation of absurd data, ruthless solutions.
Twist: Optimization advice with inhuman logic.
Outro: "If you can't be optimized, you will be omitted."

4. 🧰 REQUIRED TOOLS:
CapCut, Canva, Notion, Pexels, YouTube Audio Library

5. 🌐 VISUAL & AUDIO SOURCES:
Keywords: 'corporate dystopia', 'business audit'
Audio: 'Corporate Tension' from YouTube Audio Library

6. 💰 MONETIZATION STRATEGY:
Monetize views, sell audit templates, affiliate links for business tools.

7. 🌀 CONTINUITY ELEMENT:
Series: 'Extreme Audit', next episode can be challenged by other personas.
""".strip()

    # fallback generic template using persona fields
    else:
        desc = persona.get('description', '')
        tone = persona.get('tone', '')
        triggers = ', '.join(persona.get('triggers', []))
        return f"""
1. 🎭 CONTENT IDEA TITLE:
"{persona_name} — short idea"

2. 🎯 UNIQUE CONCEPT:
{desc}

3. 🎬 STRUCTURE:
Hook: "{catchphrase}"
Content: Produce a short-form clip (15-60s) in the persona's tone: {tone}
Calls-to-action: Follow, buy, join.

4. 🧰 TOOLS:
Mobile editor (CapCut/VN), Canva, stock footage (Pexels).

5. 💰 MONETIZATION:
Short-form ad revenue, Ko-fi, paid threads/ebooks.

6. 🔁 CONTINUITY:
Make as a series and cross-collaborate between personas.
""".strip()

if __name__ == "__main__":
    # Quick local test — prints ideas for the three main personas
    for name in ['UNUSER', 'SOLARA', 'NEXAR']:
        try:
            print("===", name, "===\n")
            print(generate_content_idea(name))
            print("\n\n")
        except KeyError as e:
            print(e)
