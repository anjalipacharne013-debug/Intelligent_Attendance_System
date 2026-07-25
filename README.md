# SnapClass — Intelligent Attendance System

SnapClass is an AI-powered classroom attendance app built with **Streamlit** and **Supabase**. Instead of manual roll calls, teachers can take attendance for an entire class in seconds using face recognition on a group photo, or students can check in individually using face or voice ID.

## ✨ Features

**For Teachers**
- Secure registration/login (username + password, bcrypt-hashed)
- Create and manage subjects/classes, each with a unique join code
- Share a class via a QR code or copyable link so students can self-enroll
- Take attendance for a whole class at once by uploading classroom photo(s) — AI detects and matches every enrolled student's face
- Alternative voice-based attendance mode
- View attendance history and per-class analytics (total classes, students present/absent)

**For Students**
- Passwordless login via Face ID — no accounts/passwords to remember
- One-time profile setup: capture your face (and optionally your voice) to register
- Auto-enroll in a class instantly by scanning a QR code or opening a share link
- View enrolled subjects and personal attendance history
- Unenroll from a subject at any time

## 🧠 How the AI works

- **Face recognition**: `face_recognition` / `dlib` encodes each student's face into a numeric embedding at registration time. During attendance, every detected face in a classroom photo is compared against these stored embeddings to identify who's present.
- **Voice recognition**: `resemblyzer` + `librosa` generate a voice embedding from a short recorded phrase, used as an optional secondary identification method.

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / App framework | [Streamlit](https://streamlit.io/) |
| Database & Auth backend | [Supabase](https://supabase.com/) (Postgres) |
| Face recognition | `face_recognition`, `dlib-bin`, `scikit-learn` |
| Voice recognition | `librosa`, `resemblyzer` |
| Password hashing | `bcrypt` |
| QR code generation | `segno` |
| Data handling | `pandas`, `numpy` |

## 📁 Project Structure

```
.
├── app.py                          # App entry point & routing
├── requirements.txt
├── src/
│   ├── database/
│   │   ├── config.py                # Supabase client setup
│   │   └── db.py                    # All database queries
│   ├── pipelines/
│   │   ├── face_pipline.py          # Face embedding, training, prediction
│   │   └── voice_pipeline.py        # Voice embedding extraction
│   ├── screens/
│   │   ├── home_screen.py           # Landing page (choose Student/Teacher)
│   │   ├── teacher_screen.py        # Teacher login/register + dashboard
│   │   └── student_screen.py        # Student Face ID login + dashboard
│   ├── components/                  # Dialogs & reusable UI (create subject,
│   │                                 # enroll, share, add photo, results, etc.)
│   └── ui/
│       └── base_layout.py           # Shared page styling
```

## ⚙️ Setup

### 1. Clone and create a virtual environment
```bash
git clone https://github.com/anjalipacharne013-debug/Intelligent_Attendance_System.git
cd Intelligent_Attendance_System
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Supabase

1. Create a free project at [supabase.com](https://supabase.com/).
2. In the SQL Editor, create the following tables: `teachers`, `students`, `subjects`, `subject_students`, `attendance_logs` (with appropriate foreign keys — e.g. `subject_students.subject_id → subjects.subject_id`, `subject_students.student_id → students.student_id`).
3. **Enable Row Level Security policies** on every table so the app's anon key can read/write. Example for a table:
   ```sql
   CREATE POLICY "Enable insert for all users"
   ON "public"."teachers"
   FOR INSERT TO anon WITH CHECK (true);

   CREATE POLICY "Enable read access for all users"
   ON "public"."teachers"
   FOR SELECT TO anon USING (true);
   ```
   Repeat (adjusting operations as needed) for `students`, `subjects`, `subject_students`, and `attendance_logs`.
4. Grab your **Project URL** and **anon public API key** from Project Settings → API.

### 4. Configure secrets
Create `.streamlit/secrets.toml` in the project root:
```toml
SUPABASE_URL = "https://your-project-ref.supabase.co"
SUPABASE_KEY = "your-anon-public-key"
```

### 5. Run the app
```bash
streamlit run app.py
```

If running inside GitHub Codespaces, start it with an explicit host/port so the port forwards correctly:
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```
Then open the forwarded port from the **Ports** tab (set its visibility to Public) rather than typing the URL manually.

## 🚀 Usage

1. Open the app and choose **Teacher Portal** or **Student Portal**.
2. **Teachers**: register an account, create a subject, and share its QR code/link with your class.
3. **Students**: scan the QR/link to auto-enroll, then register your Face ID (and optionally your voice) on first use.
4. **Taking attendance**: teachers upload one or more classroom photos on the "Take Attendance" tab — SnapClass detects every face, matches it to an enrolled student, and generates a present/absent report automatically.

## 🗺️ Roadmap / Ideas
- Export attendance records to CSV/Excel
