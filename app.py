import asyncio
import threading
from dance import app, StarTinG

# This makes the app available to Vercel
application = app

# For Vercel, we need to start the bot differently
# Start the bot in a separate thread only once
if not hasattr(app, '_bot_started'):
    def start_bot():
        # Run the bot in a separate event loop
        bot_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(bot_loop)
        bot_loop.run_until_complete(StarTinG())

    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    app._bot_started = True

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)