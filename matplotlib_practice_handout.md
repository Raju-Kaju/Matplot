# The Early Bird Data Detective
## Practice Assignment: Student Success Patterns with Data Visualization

**Estimated Time:** 45-60 minutes  
**Purpose:** Practice matplotlib skills with interesting student data

---

## 🕐 The Mystery: Do Early Risers Really Get Better Grades?

Your mission is to analyze a dataset of 150 students to investigate whether there's truth to the saying "The early bird catches the worm!" You'll explore relationships between wake-up times, study habits, screen time, and academic performance.

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

### Explore Your Data:
Run this code and look at the output. Notice:
1. What's the average wake-up time for students?
2. What's the range of test scores (lowest to highest)?
3. What patterns do you notice in the summary statistics?

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

# Add average line
plt.axvline(student_data['test_score'].mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Average: {student_data["test_score"].mean():.1f}')
plt.legend()
plt.show()
```

### Practice Tasks:
1. **Run the code** and observe the histogram
2. **Customize your histogram**:
   - Change the color to your favorite color
   - Try different numbers of bins (15, 25, 30) - which looks best?
   - Add a creative title

### Questions to Think About:
- What's the shape of the distribution?
- Are most students getting high scores, low scores, or middle scores?
- What does this tell you about academic performance?

---

## 🕐 Step 3: The Early Bird Investigation (20 minutes)

### The Main Event: Multi-Panel Scatter Plot Analysis
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

### Practice Tasks:
1. **Run the code** and study all four plots
2. **Create your own version** with:
   - Different colors for each subplot
   - Different point sizes (try s=30, s=80, s=120)
   - Your own creative titles

### Pattern Detective Work - Look For:
1. **Early Bird Evidence**: Do you see an upward or downward trend in wake-up time vs test score?
2. **Study Power**: Which relationship looks strongest - study hours vs scores, or screen time vs scores?
3. **Surprising Discovery**: Which plot showed a pattern you didn't expect?
4. **The Connection**: Do students who wake up early also study more?

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

# Add reference lines
plt.axvline(7, color='blue', linestyle=':', alpha=0.7, label='7:00 AM')
plt.axvline(8, color='orange', linestyle=':', alpha=0.7, label='8:00 AM')
plt.axhline(80, color='green', linestyle=':', alpha=0.7, label='80% Score')
plt.legend()

plt.show()
```

### Your Challenge:
1. **Run the code** and study the color patterns
2. **Experiment** with different color maps:
   - Try `cmap='viridis'` (purple to yellow)
   - Try `cmap='plasma'` (purple to pink)  
   - Try `cmap='cool'` (cyan to magenta)

### Advanced Analysis Questions:
1. **Color Patterns**: Do the brighter colored dots (higher study hours) cluster in certain areas?
2. **Success Zone**: What combination of wake-up time and study hours produces the highest test scores?
3. **Your Advice**: Based on this plot, what would you tell a friend who wants better grades?

---

## 🏆 Step 5: Reflection - Your Data Story (5 minutes)

### Think About These Questions:
Write down your thoughts for each:

1. **The Early Bird Verdict**: Is there evidence that students who wake up earlier get better grades? What do you see in the plots?

2. **The Strongest Factor**: Which factor seems most important for test scores - wake-up time, study hours, or screen time? How can you tell?

3. **Personal Application**: How might you use these insights in your own life?

4. **Surprising Discovery**: What pattern surprised you most? Why?

5. **Next Investigation**: If you could study one more factor (like hours of sleep, sports participation, or eating breakfast), what would it be and why?

**Have fun being a data detective!** 🕵️‍♂️📊