from openai import OpenAI
import json

client=OpenAI()

def analyze_resume(resume_text, user_goal):
    prompt = f"""
    You are a senior software engineer and hiring manager.
    Evaluate the resume based on the users goal.
    User goal: "{user_goal}"
    STRICT RULES:
    -Extractonly relevant skills for this goal
    -REMOVE irrelevant tools [excel for backend, etc]
    -Identify real gaps
    -generate roadmap only fro missing fields
    -make output different based on goal
    Return only json:
    {{
    "skills":[],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
    }}
    Resume:
    {resume_text}
""" 
    try:
        response=client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.3,
            messages=[
                {"role":"system","content":"You are a strict hiring manager."}
                {"role":"user","content":prompt}
            ]
        )
        content= response.choices[0].message.content.strip()
        
        start=content.find("{")
        end=content.rfind("}")+1
        return json.loads(content[start:end])
    except Exception as e:
        return {
            "skills":[],
            "missing_skills":[],
            "roadmap":[],
            "interview_questions":[],
            "error":str(e)
        }


