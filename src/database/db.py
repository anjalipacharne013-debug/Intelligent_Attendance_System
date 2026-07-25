from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()


def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def check_teacher_exists(username):
    # check for unique username, returns false when username is already taken
    responce = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(responce.data) > 0


def create_teacher(username, password, name):
    data = { "username": username, "password": hash_pass(password), "name": name }
    responce = supabase.table("teachers").insert(data).execute()
    return responce.data


def teacher_login(username, password):
    responce = supabase.table("teachers").select("*").eq("username", username).execute()
    if responce.data:
        teacher = responce.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None


def get_all_students():
    responce = supabase.table('students').select("*").execute()
    return responce.data


def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'face_embedding': face_embedding, 'voice_embedding': voice_embedding}
    responce = supabase.table('students').insert(data).execute()
    return responce.data

def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    responce = supabase.table("subjects").insert(data).execute()
    return responce.data

def get_teacher_subjects(teacher_id):
    responce = supabase.table('subjects').select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = responce.data


    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get("subject_students") else 0
        attendance = sub.get("attendance_logs", [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions

        sub.pop("subject_students", None)
        sub.pop("attendance_logs", None)

    return subjects 



def enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, 'subject_id': subject_id}
    responce = supabase.table('subject_students').insert(data).execute()
    return responce.data


def unenroll_student_to_subject(student_id, subject_id):
    responce = supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return responce.data


def get_student_subjects(student_id):
    responce = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return responce.data


def get_student_attendance(student_id):
    responce = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return responce.data


def create_attendance(logs):
    responce = supabase.table("attendance_logs").insert(logs).execute()
    return responce.data


def get_attendance_for_teacher(teacher_id):
    responce = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq("subjects.teacher_id", teacher_id).execute()
    return responce.data