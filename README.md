# Telegram Info API for Vercel

This project is a small, Vercel-compatible Python API that preserves the broad response shape of the referenced service while keeping private phone-number lookup disabled. The visible developer credit is configured as **@rajanhackerd**.

## Endpoint

```text
GET /api/telegram-info?key=YOUR_API_KEY&tg=TELEGRAM_USER_ID
```

The `tg` value must be numeric. Configure `API_KEY` in Vercel environment variables. For local testing, the default key is `change-me`; set `API_KEY=*` only for a deliberately public test deployment.

## Deploy on Vercel

Create a new Vercel project from this directory, or import the repository after pushing it to GitHub. In **Project Settings → Environment Variables**, add `API_KEY` and optionally `CREDITS_REMAINING`, then redeploy.

Example response:

```json
{
  "channel": "",
  "credits_remaining": 0,
  "data": {
    "Today_Used": 0,
    "result": {
      "country": "",
      "country_code": "",
      "msg": "Public Telegram metadata only; private phone lookup is disabled",
      "number": null,
      "response_time": "0ms",
      "tg_id": "8235337601"
    }
  },
  "developer": "@rajanhackerd",
  "service": "telegram-info",
  "success": true
}
```

The endpoint does not infer, retrieve, or disclose private telephone numbers. If you have a compliant first-party source for public Telegram metadata, add only the permitted fields inside `api/telegram-info.py`.
