import asyncio
import datetime
import pypresence
import random
import json
import genshin

config = json.load(open("config.json", "r", encoding="utf-8"))
dialogue = json.load(open("dialogue.json", "r", encoding="utf-8"))

def resin_image(val):
    if val >= 90:
        return "resin_mid"
    elif val >= 150:
        return "resin_full"
    else:
        return "resin_low"

def is_show_remains(notes):
    if config["show_remains"]:
        _ = notes.remaining_resin_recovery_time+datetime.datetime.now()
        return _.timestamp()
    else:
        return None

async def gi_process() -> genshin.Client:
    cookies = {"ltuid": config["ltuid"], "ltoken": config["ltoken"]}
    client = genshin.Client(cookies)
    return client

async def main():
    gi_client = await gi_process()
    client = pypresence.AioPresence(
        client_id = 1139958041383542865
    )
    await client.connect()
    while True:
        notes = await gi_client.get_genshin_notes()
        resin_now = notes.current_resin
        remain = notes.remaining_resin_recovery_time+datetime.datetime.now()
        await client.update(
            details=config["details"].format(
                resin_now = resin_now
            ),
            end=is_show_remains(notes),
            large_image="paimon",
            large_text=random.choice(dialogue),
            small_image=resin_image(resin_now),
            small_text=str(resin_now)
        )
        await asyncio.sleep(300)

asyncio.run(main())