# Homework Assignment: "The Early Bird Data Detective"
## Investigating Student Success Patterns with Data Visualization

**Due Date:** Next class  
**Estimated Time:** 45-60 minutes  
**Points:** 50 points  
**Submit:** Screenshots of your plots + written observations

---

## 🕐 The Mystery: Do Early Risers Really Get Better Grades?

Your mission is to analyze a dataset of 150 students to investigate whether there's truth to the saying "The early bird catches the worm!" You'll explore relationships between wake-up times, study habits, screen time, and academic performance using the matplotlib skills you learned today.

**The Big Questions:**
1. Do students who wake up earlier really get better grades?
2. What does the distribution of test scores look like in our school?
3. Are there other factors that predict academic success?
4. Can you find any surprising patterns in student behavior?

---

## 📊 Step 1: Set Up Your Data Laboratory (10 minutes)

### Create Your Dataset
Copy and run this code to generate realistic student data:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for consistent results
np.random.seed(42)

print("🎒 Welcome to the Early Bird Data Detective Challenge!")
print("=" * 60)

# Generate realistic student data
def create_student_dataset():
    n_students = 150
    
    # Wake up times (in hours after midnight)
    # Most students wake up between 6-8 AM, some early birds, some night owls
    wake_up_times = np.concatenate([
        np.random.normal(6.5, 0.5, 30),   # Early birds (6-7 AM)
        np.random.normal(7.2, 0.7, 80),   # Normal students (6:30-8 AM)  
        np.random.normal(8.5, 1.0, 40)    # Late risers (7:30-10 AM)
    ])
    wake_up_times = np.clip(wake_up_times, 5.5, 10.5)  # 5:30 AM to 10:30 AM
    
    # Study hours per day (correlated with wake-up time and performance)
    study_hours = []
    test_scores = []
    screen_time = []
    
    for wake_time in wake_up_times:
        # Early birds tend to study more and get better grades
        if wake_time < 7:  # Early birds
            study_hrs = np.random.normal(2.5, 0.8)
            base_score = 82
        elif wake_time < 8:  # Normal students  
            study_hrs = np.random.normal(1.8, 0.6)
            base_score = 78
        else:  # Late risers
            study_hrs = np.random.normal(1.2, 0.5) 
            base_score = 72
            
        study_hrs = max(0.5, study_hrs)  # At least 30 minutes
        study_hours.append(study_hrs)
        
        # Test scores based on study time + some randomness
        score = base_score + study_hrs * 6 + np.random.normal(0, 8)
        score = np.clip(score, 45, 98)  # Realistic range
        test_scores.append(score)
        
        # Screen time (inversely related to study time)
        screen = 8 - study_hrs + np.random.normal(0, 1.5)
        screen = max(2, min(12, screen))  # 2-12 hours per day
        screen_time.append(screen)
    
    # Create DataFrame
    students_df = pd.DataFrame({
        'student_id': range(1, n_students + 1),
        'wake_up_time': wake_up_times,
        'study_hours': study_hours,
        'test_score': test_scores,
        'screen_time_hours': screen_time
    })
    
    return students_df

# Create the dataset
student_data = create_student_dataset()
print(f"📚 Created dataset with {len(student_data)} students!")
print("\nFirst 5 students:")
print(student_data.head())

print("\n📈 Dataset Summary:")
print(student_data.describe())
```

### Your Task:
Run this code and **take a screenshot** of the output. This shows you understand how to load and examine data.

**Answer these questions** (2-3 sentences each):
1. What's the average wake-up time for students in our dataset?
2. What's the range of test scores (lowest to highest)?
3. What surprised you most about the data summary?

---

## 📊 Step 2: The Grade Distribution Investigation (15 minutes)

### Create a Professional Histogram
```python
# Investigation 1: How are test scores distributed?
plt.figure(figsize=(10, 6))
plt.hist(student_data['test_score'], bins=20, color='lightblue', 
         alpha=0.8, edgecolor='black', linewidth=1)
plt.title('Test Score Distribution in Our School', fontsize=16, fontweight='bold')
plt.xlabel('Test Score (0-100)')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)

# Add some style
plt.axvline(student_data['test_score'].mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Average: {student_data["test_score"].mean():.1f}')
plt.legend()
plt.show()
```

### Your Tasks:
1. **Run the code** and take a screenshot
2. **Modify the histogram**:
   - Change the color to your favorite color
   - Try different numbers of bins (15, 25, 30) - which looks best?
   - Add a title with your name: "Test Scores - [Your Name]'s Analysis"

**Written Analysis** (3-4 sentences):
- Describe the shape of the distribution
- Are most students getting high scores, low scores, or middle scores?
- What does this tell you about our school's academic performance?

---

## 🕐 Step 3: The Early Bird Investigation (20 minutes)

### The Main Event: Scatter Plot Analysis
```python
# Investigation 2: Do early risers really get better grades?
plt.figure(figsize=(12, 8))

# Main scatter plot
plt.subplot(2, 2, 1)
plt.scatter(student_data['wake_up_time'], student_data['test_score'], 
           alpha=0.7, color='green', s=60, edgecolors='black', linewidth=0.5)
plt.title('Wake-Up Time vs Test Score\n(The Early Bird Question!)')
plt.xlabel('Wake-Up Time (6.0 = 6:00 AM, 8.0 = 8:00 AM)')
plt.ylabel('Test Score')
plt.grid(True, alpha=0.3)

# Study hours vs test scores
plt.subplot(2, 2, 2)
plt.scatter(student_data['study_hours'], student_data['test_score'],
           alpha=0.7, color='blue', s=60, edgecolors='black', linewidth=0.5)
plt.title('Study Hours vs Test Score')
plt.xlabel('Hours Studied Per Day')
plt.ylabel('Test Score')
plt.grid(True, alpha=0.3)

# Screen time vs test scores
plt.subplot(2, 2, 3)
plt.scatter(student_data['screen_time_hours'], student_data['test_score'],
           alpha=0.7, color='red', s=60, edgecolors='black', linewidth=0.5)
plt.title('Screen Time vs Test Score')
plt.xlabel('Screen Time (Hours Per Day)')
plt.ylabel('Test Score')
plt.grid(True, alpha=0.3)

# Wake-up time vs study hours
plt.subplot(2, 2, 4)
plt.scatter(student_data['wake_up_time'], student_data['study_hours'],
           alpha=0.7, color='purple', s=60, edgecolors='black', linewidth=0.5)
plt.title('Wake-Up Time vs Study Hours')
plt.xlabel('Wake-Up Time')
plt.ylabel('Study Hours Per Day')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Your Tasks:
1. **Run the code** and take a screenshot of all four plots
2. **Create your own version** with these modifications:
   - Choose different colors for each subplot
   - Change point sizes (try s=30, s=80, s=120)
   - Add your own creative titles

**Pattern Detective Work** - Answer these questions:
1. **Early Bird Evidence**: Do you see an upward or downward trend in the wake-up time vs test score plot? What does this suggest?
2. **Study Power**: Which relationship looks strongest - study hours vs scores, or screen time vs scores?
3. **Surprising Discovery**: Which plot showed a pattern you didn't expect? Explain what you found.
4. **The Connection**: Do students who wake up early also tend to study more? What does the wake-up time vs study hours plot tell you?

---

## 🎨 Step 4: Advanced Analysis - The Color-Coded Mystery (10 minutes)

### Create a Professional 3-Variable Plot
```python
# Investigation 3: The ultimate visualization
plt.figure(figsize=(10, 8))

# Color-code points by study hours
scatter = plt.scatter(student_data['wake_up_time'], student_data['test_score'],
                     c=student_data['study_hours'], s=80, alpha=0.8,
                     cmap='YlOrRd', edgecolors='black', linewidth=0.5)

plt.colorbar(scatter, label='Study Hours Per Day')
plt.title('The Complete Picture: Wake-Up Time vs Test Score\n(Color = Study Hours)', 
          fontsize=14, fontweight='bold')
plt.xlabel('Wake-Up Time (earlier ← → later)')
plt.ylabel('Test Score')
plt.grid(True, alpha=0.3)

# Add some analysis zones
plt.axvline(7, color='blue', linestyle=':', alpha=0.7, label='7:00 AM')
plt.axvline(8, color='orange', linestyle=':', alpha=0.7, label='8:00 AM')
plt.axhline(80, color='green', linestyle=':', alpha=0.7, label='80% Score')
plt.legend()

plt.show()
```

### Your Challenge:
1. **Run the code** and screenshot the result
2. **Experiment** with different color maps:
   - Try `cmap='viridis'` (purple to yellow)
   - Try `cmap='plasma'` (purple to pink)  
   - Try `cmap='cool'` (cyan to magenta)
   - Which one do you think looks most professional?

**Advanced Analysis Questions:**
1. **Color Patterns**: Do the darker colored dots (higher study hours) tend to cluster in certain areas?
2. **Success Zone**: What combination of wake-up time and study hours seems to produce the highest test scores?
3. **Recommendation**: Based on this plot, what advice would you give to a student who wants to improve their grades?

---

## 🏆 Step 5: Your Personal Data Story (5 minutes)

### Reflection Questions
Write 2-3 sentences for each:

1. **The Early Bird Verdict**: Based on your analysis, is there evidence that students who wake up earlier get better grades? Support your answer with specific observations from your plots.

2. **The Strongest Factor**: Which factor seems to have the strongest relationship with test scores - wake-up time, study hours, or screen time? How can you tell?

3. **Personal Application**: How might you use these insights to improve your own academic performance?

4. **Data Scientist Skills**: What's one pattern you discovered that surprised you? How could this information be useful for teachers or school administrators?

5. **Next Investigation**: If you could add one more variable to this dataset (like hours of sleep, extracurricular activities, or breakfast eating habits), what would it be and why?

---

## 📝 Submission Requirements

Submit the following by the next class:

### Screenshots (30 points):
1. ✅ Data summary output from Step 1
2. ✅ Your customized histogram from Step 2  
3. ✅ Your four-panel scatter plot from Step 3
4. ✅ Your color-coded advanced plot from Step 4

### Written Responses (20 points):
1. ✅ All analysis questions answered (2-3 sentences each)
2. ✅ Personal reflection questions from Step 5
3. ✅ At least one "surprising discovery" mentioned

**Submission Format:**
- Create a document (Google Doc/Word) with your screenshots and written responses
- OR create a Jupyter notebook with your code, plots, and markdown answers
- OR submit handwritten responses with printed screenshots

---

## 🌟 Bonus Challenges (Optional - Extra Credit)

### Level 1: Style Master (+5 points)
- Create a histogram with custom colors that match your school colors
- Add professional styling with custom fonts and grid lines

### Level 2: Data Detective (+10 points)
- Find the student with the highest test score - what time do they wake up and how much do they study?
- Find the earliest riser - do they have a high test score?
- Create a "success profile" based on your findings

### Level 3: Presentation Pro (+15 points)
- Create a presentation slide with your best plot and three key findings
- Write a "news headline" that summarizes your most interesting discovery
- Suggest a follow-up study with different variables

---

## 🎯 Learning Objectives Check

By completing this assignment, you will have:
- ✅ Created professional histograms with custom styling
- ✅ Used scatter plots to identify relationships between variables  
- ✅ Applied subplot layouts for multi-panel analysis
- ✅ Experimented with color-coding for advanced visualization
- ✅ Interpreted data patterns and drawn evidence-based conclusions
- ✅ Connected data analysis to real-world applications

---

## 🆘 Help Resources

### Stuck on Code?
- Check your parentheses and commas
- Make sure you're using the exact variable names from the dataset
- Try running each section separately to find errors

### Can't See Patterns?
- Look for general trends, not perfect lines
- Compare the left side vs right side of scatter plots  
- Ask yourself: "As X increases, does Y tend to increase or decrease?"

### Need Inspiration?
- Think about your own school experience
- Consider what factors help YOU succeed academically
- Remember: surprising findings are often the most interesting!

### Technical Issues?
- Contact a classmate for help
- Check the class discussion forum
- Email me with specific error messages

---

## 📊 Sample Student Response (Partial)

*"Looking at my wake-up time vs test score scatter plot, I can see a clear downward trend - students who wake up earlier tend to have higher test scores. The early birds (waking up around 6-7 AM) mostly have scores above 80, while students waking up after 8:30 AM tend to score below 75. 

What surprised me most was the screen time relationship. I expected to see that more screen time = lower grades, and I was right! There's a clear downward trend showing that students with 8+ hours of screen time generally score lower than those with 4-6 hours.

The color-coded plot was amazing - I could see that the bright yellow dots (high study hours) were clustered in the upper left area (early wake-up times + high scores), while the dark red dots (low study hours) were scattered more in the lower right..."*

**Remember:** Your goal is to find genuine patterns in the data and explain them clearly. There are no "wrong" observations as long as you support them with evidence from your plots!

---

## 🎉 Why This Assignment Rocks

This homework bridges the gap between classroom learning and real-world application. You're not just practicing matplotlib syntax - you're developing data literacy skills that colleges and employers value highly. Plus, you might discover something useful about study habits that actually improves your own academic performance!

**Due next class - happy data detecting!** 🕵️‍♂️📊