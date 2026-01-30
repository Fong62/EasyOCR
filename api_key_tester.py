from openai import OpenAI

def test_key(api_key: str) -> str:
    try:
        client = OpenAI(api_key=api_key)

        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=1,
        )

        return "✅ VALID (có quota)"

    except Exception as e:
        msg = str(e)

        if "invalid_api_key" in msg:
            return "❌ INVALID KEY"
        if "insufficient_quota" in msg:
            return "⚠️ KEY OK nhưng HẾT QUOTA"
        if "rate_limit" in msg:
            return "⚠️ RATE LIMITED"

        return f"❌ ERROR: {msg}"
