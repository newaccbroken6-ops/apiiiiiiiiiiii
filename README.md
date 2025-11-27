# Free Fire Emote Bot Website

This is a simple web interface that connects to the DANCE API to perform emotes in Free Fire squads.

## Setup Instructions

1. **Start the DANCE API server:**
   ```
   python dance.py
   ```
   This will start the API server on port 5000.

2. **Start the web interface server:**
   ```
   python web_server.py
   ```
   This will start the web server on port 8000.

3. **Access the web interface:**
   Open your browser and go to: http://localhost:8000

## How to Use

1. Enter the squad/team code
2. Enter at least one player UID (up to 4)
3. Select an emote from the dropdown
4. Click "Perform Emote"

## API Endpoint

The web interface communicates with the following API endpoint:
```
GET http://localhost:5000/join
```

Parameters:
- `tc` - Team/Squad code
- `uid1`, `uid2`, `uid3`, `uid4` - Player UIDs (at least one required)
- `emote_id` - ID of the emote to perform

## Emote IDs

Some common emote IDs:
- 902000306 - Dab Dance
- 902000305 - Floss Dance
- 902000003 - Clap
- 902000016 - Victory
- 902000017 - Flex
- 902000019 - Rock On
- 902031010 - Zombie
- 902043025 - Chicken
- 902043024 - Running Man
- 902000020 - T-Pose
- 902000021 - Shuffle
- 902000023 - Salute

## Requirements

- Python 3.x
- All dependencies listed in `requirements.txt`

Install dependencies:
```
pip install -r requirements.txt
```

## Note

Make sure both servers are running:
- DANCE API: http://localhost:5000
- Web Interface: http://localhost:8000