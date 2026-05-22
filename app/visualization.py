import matplotlib.pyplot as plt
# skill frequency
skills = ["python", "sql", "pandas", "python", "sql", "java"]

skill_count = {}

for skill in skills:
    skill_count[skill] = skill_count.get(skill, 0) + 1

plt.figure(figsize=(8,5))

plt.bar(skill_count.keys(), skill_count.values())

plt.title("Skill Frequency")
plt.xlabel("Skills")
plt.ylabel("Count")
plt.savefig("C:\\Users\\anju&janu\\OneDrive\\kavya\\smart-resume-analyzer\\images\\skill_frequency.png")
plt.show()

# ATS score
score = 75

plt.figure(figsize=(6,4))

plt.bar(["ATS Score"], [score])

plt.ylim(0, 100)

plt.title("Resume ATS Score")

plt.savefig("C:\\Users\\anju&janu\\OneDrive\\kavya\\smart-resume-analyzer\\images\\ats_score.png")
plt.show()

# Missing skills
missing_skills = ["machine learning", "communication"]

values = [1, 1]

plt.figure(figsize=(7,4))

plt.bar(missing_skills, values)

plt.title("Missing Skills")

plt.ylabel("Need Improvement")
plt.savefig("C:\\Users\\anju&janu\\OneDrive\\kavya\\smart-resume-analyzer\\images\\missing_skills.png")
plt.show()