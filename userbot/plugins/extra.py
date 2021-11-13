import heroku3
from userbot import HEROKU_APP, UPSTREAM_REPO_URL, catub
plugin_category = "useless"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None
HEROKU_API_KEY = Config.HEROKU_API_KEY or None
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"

@catub.cat_cmd(
    pattern="oshocat",
    command=("oshocat", plugin_category),
    info={
        "header": "To update to oshocat( For Scam peeps).",
        "usage": "{tr}oshocat",
    },
)
async def variable(var):
    "To update to oshocat."
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            var,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            var,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    heroku_var = app.config()
    await edit_or_reply(var, "`Changing cat version to oshocat wait for 2-3 minutes.`")
    heroku_var["UPSTREAM_REPO"] = "https://github.com/Osho28Raj/catub"

@catub.cat_cmd(
    pattern="pepecat",
    command=("pepecat", plugin_category),
    info={
        "header": "To update to pepecat( For Horni peeps).",
        "usage": "{tr}pepecat",
    },
)
async def variable(varr):
    "To update to pepecat."
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            varr,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            varr,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    heroku_var = app.config()
    await edit_or_reply(varr, "`Changing cat version to pepecat wait for 2-3 minutes.`")
    heroku_var["UPSTREAM_REPO"] = "https://github.com/prono69/pepecat"

@catub.cat_cmd(
    pattern="pepecat",
    command=("pepecat", plugin_category),
    info={
        "header": "To update to pepecat( For Horni peeps).",
        "usage": "{tr}pepecat",
    },
)
async def variable(varr):
    "To update to pepecat."
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            varr,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            varr,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    heroku_var = app.config()
    await edit_or_reply(varr, "`Changing cat version to pepecat wait for 2-3 minutes.`")
    heroku_var["UPSTREAM_REPO"] = "https://github.com/prono69/pepecat"

@catub.cat_cmd(
    pattern="dedcat",
    command=("dedcat", plugin_category),
    info={
        "header": "To update to dedcat( For ded peeps).",
        "usage": "{tr}dedcat",
    },
)
async def variable(varrr):
    "To update to dedcat."
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            varrr,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            varrr,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    heroku_var = app.config()
    await edit_or_reply(varrr, "`Changing cat version to dedcat wait for 2-3 minutes.`")
    heroku_var["UPSTREAM_REPO"] = "https://github.com/NekkoYato/catuserbot"
