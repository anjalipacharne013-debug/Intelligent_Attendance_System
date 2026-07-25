import os
import streamlit as st

from supabase import create_client, Client


def _get_config(key):
    # Prefer Streamlit secrets (used on Streamlit Cloud / .streamlit/secrets.toml),
    # but fall back to environment variables so the app doesn't crash with an
    # unhelpful error when secrets.toml is missing (e.g. local dev, Docker).
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key)


SUPABASE_URL = _get_config("SUPABASE_URL")
SUPABASE_KEY = _get_config("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error(
        "Supabase is not configured. Add SUPABASE_URL and SUPABASE_KEY to "
        ".streamlit/secrets.toml (or set them as environment variables) "
        "before using Register/Login."
    )
    st.stop()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



# import streamlit as st

# from supabase import create_client, Client


# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]

# )