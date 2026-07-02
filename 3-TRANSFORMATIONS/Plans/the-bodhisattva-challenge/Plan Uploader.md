# CMS API: Add Plans to a Series

API reference for content authors to create plans inside an existing series and upload plan text, images, and audio.

**Base URL:** `https://api.webuddhist.com/api/v1`

---

## Required Context

Before calling any endpoint below, you need three values:

| Variable | Description | Example |
|----------|-------------|---------|
| `SERIES_ID` | UUID of the series the plan belongs to | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `LANGUAGE` | Language code for the plan content being uploaded | `EN`, `BO`, `ZH`, `HI`, `NE`, `MN` |
| `AUTH_TOKEN` | Author JWT access token from login | `eyJhbGciOiJIUzI1NiIs...` |

Use the token on every authenticated request:

```http
Authorization: Bearer {AUTH_TOKEN}
```

---

## Table of Contents

1. [Authentication](#authentication)
2. [Typical Workflow](#typical-workflow)
3. [Plan Creation](#plan-creation)
4. [Media Uploads](#media-uploads)
5. [Days](#days)
6. [Tasks](#tasks)
7. [Sub-tasks (Text Content)](#sub-tasks-text-content)
8. [Sub-task Presets](#sub-task-presets)
9. [Clone Plans for Another Language](#clone-plans-for-another-language)
10. [Publish Plan](#publish-plan)
11. [Read Endpoints](#read-endpoints)
12. [Request Schemas](#request-schemas)
13. [Error Handling](#error-handling)

---

## Authentication

### Login

Obtain `AUTH_TOKEN` from the login response (`auth.access_token`).

```http
POST /api/v1/cms/auth/login
Content-Type: application/json
```

**Request body:**

```json
{
  "email": "author@example.com",
  "password": "your-password"
}
```

**Response (200):**

```json
{
  "user": {
    "name": "Author Name",
    "image_url": null
  },
  "auth": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
  }
}
```

### Refresh Token

```http
POST /api/v1/cms/auth/refresh-token
Content-Type: application/json
```

**Request body:**

```json
{
  "token": "{refresh_token}"
}
```

---

## Typical Workflow

```
Login → Create plan (series_id + language) → Upload cover image
  → Add days → Create tasks → Create sub-tasks (TEXT content)
  → Upload text images / audio (optional) → Publish plan
```

To add the same plan structure in another language, use **Clone Plans for Another Language** instead of rebuilding from scratch.

---

## Plan Creation

### Create Plan in Series

Creates a new plan and attaches it to `SERIES_ID` with the given `LANGUAGE`.

```http
POST /api/v1/cms/plans
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "title": "Introduction to Mindfulness",
  "description": "A 7-day introductory plan",
  "difficulty_level": "BEGINNER",
  "total_days": 7,
  "language": "{LANGUAGE}",
  "group_id": "group-uuid-here",
  "series_id": "{SERIES_ID}",
  "display_order": 1,
  "image_url": null,
  "tag_ids": [],
  "start_date": null
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Yes | Plan title |
| `description` | Yes | Plan description |
| `difficulty_level` | Yes | `BEGINNER`, `INTERMEDIATE`, or `ADVANCED` |
| `total_days` | Yes | Expected number of days |
| `language` | Yes | `EN`, `BO`, `ZH`, `HI`, `NE`, or `MN` |
| `group_id` | Yes | Author group that owns the plan |
| `series_id` | Yes | `{SERIES_ID}` — links plan to the series |
| `display_order` | No | Order of this plan within the series |
| `image_url` | No | S3 key from cover image upload |
| `tag_ids` | No | List of tag UUIDs |
| `start_date` | No | ISO 8601 datetime |

**Response (201):** `PlanDTO` — save `id` as `PLAN_ID`.

### Update Plan Metadata

Update plan fields (title, description, image, display order, etc.). Does not change series metadata.

```http
PUT /api/v1/cms/plans/{PLAN_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body (all fields optional):**

```json
{
  "title": "Updated title",
  "description": "Updated description",
  "language": "{LANGUAGE}",
  "difficulty_level": "INTERMEDIATE",
  "total_days": 10,
  "image_url": "plans/images/abc123.jpg",
  "tag_ids": [],
  "start_date": null,
  "series_id": "{SERIES_ID}",
  "display_order": 2
}
```

---

## Media Uploads

All upload endpoints use `multipart/form-data` and require `Authorization: Bearer {AUTH_TOKEN}`.

### Upload Plan Cover Image

```http
POST /api/v1/cms/media/upload?plan_id={PLAN_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: multipart/form-data
```

| Field | Type | Required |
|-------|------|----------|
| `file` | binary | Yes — JPEG, PNG, or WebP |

**Response (201):**

```json
{
  "image": {
    "thumbnail": "https://...",
    "medium": "https://...",
    "original": "https://..."
  },
  "key": "plans/images/...",
  "path": "plans/images/...",
  "message": "Image uploaded successfully"
}
```

Use `key` as `image_url` when creating or updating the plan.

### Upload Text Image (inline image in sub-task content)

```http
POST /api/v1/cms/media/upload/text
Authorization: Bearer {AUTH_TOKEN}
Content-Type: multipart/form-data
```

| Field | Type | Required |
|-------|------|----------|
| `text_id` | string (form) | Yes — identifier for the text block |
| `file` | binary | Yes |

**Response (201):** `TextImageUploadResponse` with `image` URLs and `key`.

### Upload Day Audio

```http
POST /api/v1/cms/media/upload/day-audio?day_id={DAY_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: multipart/form-data
```

| Field | Type | Required |
|-------|------|----------|
| `file` | binary | Yes |
| `duration_ms` | integer (form) | No |

### Upload Sub-task Audio

```http
POST /api/v1/cms/media/upload/subtask-audio?sub_task_id={SUB_TASK_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: multipart/form-data
```

| Field | Type | Required |
|-------|------|----------|
| `file` | binary | Yes |
| `duration_ms` | integer (form) | No |

### Upload Day Shareable Image

```http
POST /api/v1/cms/media/upload/day-shareable-image?day_id={DAY_ID}&image_type={TYPE}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: multipart/form-data
```

| Query param | Values |
|-------------|--------|
| `image_type` | Shareable image type enum value |

### Assign Existing Audio to a Day

Use when audio was uploaded separately and needs to be linked to a day.

```http
PATCH /api/v1/cms/plans/days/{DAY_ID}/audio
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "audio_key": "plans/audio/...",
  "duration_ms": 120000
}
```

### Generate Plan Audio (TTS)

Generates audio for a day or sub-task via text-to-speech. No auth header required.

```http
POST /api/v1/cms/plans/audio/generate
Content-Type: application/json
```

**Request body:**

```json
{
  "day_id": "{DAY_ID}",
  "language": "{LANGUAGE}",
  "type": "TEXT_READING",
  "voice_name": "dolkar_lhasa_female"
}
```

Or for a sub-task:

```json
{
  "sub_task_id": "{SUB_TASK_ID}",
  "language": "{LANGUAGE}",
  "type": "TEXT_READING",
  "voice_name": "dolkar_lhasa_female"
}
```

| `type` values | `RECITATION`, `INSTRUCTION`, `TEXT_READING` |

---

## Days

### Add Days to Plan

```http
POST /api/v1/cms/plans/{PLAN_ID}/days
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "number_of_days": 1,
  "source_day_id": null
}
```

| Field | Notes |
|-------|-------|
| `number_of_days` | How many days to add (default `1`) |
| `source_day_id` | Optional — clone content from an existing day |

**Response (201):** Array of `ItemDTO` — each item has `id` (use as `DAY_ID`), `plan_id`, `day_number`.

### Reorder Days

```http
PUT /api/v1/cms/plans/{PLAN_ID}/reorder-days
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "days": [
    { "id": "{DAY_ID}", "day_number": 1 },
    { "id": "{DAY_ID_2}", "day_number": 2 }
  ]
}
```

### Delete Days

```http
DELETE /api/v1/cms/plans/{PLAN_ID}/days
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "day_ids": ["{DAY_ID}"]
}
```

---

## Tasks

### Create Task

```http
POST /api/v1/cms/tasks
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "plan_id": "{PLAN_ID}",
  "day_id": "{DAY_ID}",
  "title": "Morning reading",
  "description": "Read the assigned text",
  "estimated_time": 15
}
```

**Response (201):** `TaskDTO` with `id` — save as `TASK_ID`.

### Update Task Title

```http
PUT /api/v1/cms/tasks/{TASK_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "title": "Updated task title"
}
```

### Move Task to Another Day

```http
PATCH /api/v1/cms/tasks/{TASK_ID}
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "target_day_id": "{DAY_ID}"
}
```

### Reorder Tasks Within a Day

```http
PUT /api/v1/cms/tasks/{DAY_ID}/order
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "tasks": [
    { "id": "{TASK_ID}", "display_order": 1 },
    { "id": "{TASK_ID_2}", "display_order": 2 }
  ]
}
```

### Delete Task

```http
DELETE /api/v1/cms/tasks/{TASK_ID}
Authorization: Bearer {AUTH_TOKEN}
```

---

## Sub-tasks (Text Content)

Sub-tasks hold the actual reading content (text, audio references, images, source references).

### Create Sub-tasks

```http
POST /api/v1/cms/sub-tasks
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "task_id": "{TASK_ID}",
  "sub_tasks": [
    {
      "content_type": "TEXT",
      "content": "<p>Your reading text here...</p>",
      "duration": null,
      "source_text_id": null,
      "pecha_segment_id": null,
      "segment_ids": null,
      "start_ms": null,
      "end_ms": null
    }
  ]
}
```

| `content_type` | Description |
|----------------|-------------|
| `TEXT` | HTML or plain text content |
| `AUDIO` | Audio content reference |
| `VIDEO` | Video content reference |
| `IMAGE` | Image content reference |
| `SOURCE_REFERENCE` | Reference to a Pecha source text |

**Response (201):** `SubTaskResponse` with `sub_tasks[]` — each has `id` (save as `SUB_TASK_ID`).

### Update Sub-tasks

```http
PUT /api/v1/cms/sub-tasks
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "task_id": "{TASK_ID}",
  "sub_tasks": [
    {
      "id": "{SUB_TASK_ID}",
      "content_type": "TEXT",
      "content": "<p>Updated text...</p>",
      "display_order": 1,
      "duration": null,
      "image_url": null,
      "audio_url": null,
      "source_text_id": null,
      "pecha_segment_id": null,
      "segment_ids": null,
      "start_ms": null,
      "end_ms": null
    }
  ]
}
```

### Reorder Sub-tasks

```http
PUT /api/v1/cms/sub-tasks/{TASK_ID}/order
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "subtasks": [
    { "id": "{SUB_TASK_ID}", "display_order": 1 },
    { "id": "{SUB_TASK_ID_2}", "display_order": 2 }
  ]
}
```

---

## Sub-task Presets

Link a sub-task to a Pecha text version preset (for `SOURCE_REFERENCE` content).

### Create or Update Preset

```http
POST /api/v1/cms/sub-tasks/{SUB_TASK_ID}/preset
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "version_id": "pecha-version-id",
  "language": "{LANGUAGE}"
}
```

### Get Preset

```http
GET /api/v1/cms/sub-tasks/{SUB_TASK_ID}/preset
```

### Delete Preset

```http
DELETE /api/v1/cms/sub-tasks/{SUB_TASK_ID}/preset
Authorization: Bearer {AUTH_TOKEN}
```

---

## Clone Plans for Another Language

Copy all plans from one language to another within the same series. Use this when adding a translated version instead of creating each plan manually.

```http
POST /api/v1/cms/series/{SERIES_ID}/clone-plans
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "source_language": "EN",
  "target_language": "BO"
}
```

| Field | Notes |
|-------|-------|
| `source_language` | Language of existing plans to copy from |
| `target_language` | New language for cloned plans (must differ from source) |

**Response (200):** `SeriesDTO` with the updated `plans` list.

---

## Publish Plan

Plans are created in `DRAFT` status. Publish when content is complete.

```http
PATCH /api/v1/cms/plans/{PLAN_ID}/status
Authorization: Bearer {AUTH_TOKEN}
Content-Type: application/json
```

**Request body:**

```json
{
  "status": "PUBLISHED"
}
```

| Status | Description |
|--------|-------------|
| `DRAFT` | Work in progress |
| `PUBLISHED` | Live for users |
| `UNPUBLISHED` | Hidden from users |
| `ARCHIVED` | Archived |
| `DELETED` | Soft-deleted |

---

## Read Endpoints

Use these to verify uploaded content.

### Get Series with Plans (filter by language)

```http
GET /api/v1/cms/series/{SERIES_ID}?language={LANGUAGE}
Authorization: Bearer {AUTH_TOKEN}
```

Returns `SeriesDTO` including `plans[]` for the requested language.

### Get Plan with All Days

```http
GET /api/v1/cms/plans/{PLAN_ID}
Authorization: Bearer {AUTH_TOKEN}
```

Returns `PlanWithDays` — plan metadata plus nested days, tasks, and sub-tasks.

### Get Single Day Content

```http
GET /api/v1/cms/plans/{PLAN_ID}/days/{DAY_NUMBER}
Authorization: Bearer {AUTH_TOKEN}
```

`DAY_NUMBER` is the 1-based day index (not the day UUID).

### Get Task with Sub-tasks

```http
GET /api/v1/cms/tasks/{TASK_ID}
Authorization: Bearer {AUTH_TOKEN}
```

### List Plans (filter by series)

```http
GET /api/v1/cms/plans?language={LANGUAGE}&skip=0&limit=10
Authorization: Bearer {AUTH_TOKEN}
```

---

## Request Schemas

### CreatePlanRequest

```json
{
  "title": "string",
  "description": "string",
  "difficulty_level": "BEGINNER | INTERMEDIATE | ADVANCED",
  "total_days": 7,
  "language": "EN | BO | ZH | HI | NE | MN",
  "group_id": "uuid",
  "series_id": "uuid",
  "display_order": 1,
  "image_url": "string | null",
  "tag_ids": ["uuid"],
  "start_date": "2026-01-01T00:00:00Z | null"
}
```

### SubTaskRequestFields

```json
{
  "content_type": "TEXT | AUDIO | VIDEO | IMAGE | SOURCE_REFERENCE",
  "content": "string",
  "duration": "string | null",
  "source_text_id": "uuid | null",
  "pecha_segment_id": "string | null",
  "segment_ids": ["uuid"] | null,
  "start_ms": 0 | null,
  "end_ms": 0 | null
}
```

### CloneSeriesPlansRequest

```json
{
  "source_language": "EN | BO | ZH | HI | NE | MN",
  "target_language": "EN | BO | ZH | HI | NE | MN"
}
```

---

## Error Handling

| Status | Meaning |
|--------|---------|
| `400` | Invalid request body or validation error |
| `401` | Missing or invalid `AUTH_TOKEN` |
| `403` | Author does not have permission for this series/plan |
| `404` | Series, plan, day, task, or sub-task not found |
| `413` | Uploaded file exceeds size limit |

All error responses follow:

```json
{
  "error": "error_code",
  "message": "Human-readable description"
}
```

---

## Quick Reference

| Step | Method | Endpoint |
|------|--------|----------|
| Login | `POST` | `/cms/auth/login` |
| Create plan in series | `POST` | `/cms/plans` |
| Upload cover image | `POST` | `/cms/media/upload?plan_id={PLAN_ID}` |
| Add days | `POST` | `/cms/plans/{PLAN_ID}/days` |
| Create task | `POST` | `/cms/tasks` |
| Upload text content | `POST` | `/cms/sub-tasks` |
| Upload text image | `POST` | `/cms/media/upload/text` |
| Upload day audio | `POST` | `/cms/media/upload/day-audio?day_id={DAY_ID}` |
| Upload sub-task audio | `POST` | `/cms/media/upload/subtask-audio?sub_task_id={SUB_TASK_ID}` |
| Clone plans to new language | `POST` | `/cms/series/{SERIES_ID}/clone-plans` |
| Publish plan | `PATCH` | `/cms/plans/{PLAN_ID}/status` |
| View series plans | `GET` | `/cms/series/{SERIES_ID}?language={LANGUAGE}` |