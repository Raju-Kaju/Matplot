import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("📊 Understanding plt.hist() and plt.scatter()")
print("=" * 60)

# Generate sample data for demonstrations
np.random.seed(42)

# ============================================
# PART 1: Understanding plt.hist()
# ============================================

print("\n📈 PART 1: plt.hist() - HISTOGRAMS")
print("-" * 50)

print("""
🎯 What is plt.hist()?
A histogram shows the DISTRIBUTION of your data:
- How many songs have low popularity? Medium? High?
- What's the most common value?
- Are values spread out or clustered together?

Think of it as sorting data into bins/buckets and counting how many items are in each bin!
""")

# Example 1: Basic histogram
test_scores = [45, 67, 89, 78, 92, 85, 76, 88, 91, 73, 82, 95, 69, 84, 77, 
               90, 86, 79, 93, 71, 88, 94, 81, 87, 75, 89, 83, 92, 78, 85]

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(test_scores, bins=5, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Test Scores Distribution\n(5 bins)', fontweight='bold')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
plt.hist(test_scores, bins=10, color='lightgreen', alpha=0.7, edgecolor='black')
plt.title('Test Scores Distribution\n(10 bins)', fontweight='bold')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 3)
plt.hist(test_scores, bins=15, color='salmon', alpha=0.7, edgecolor='black')
plt.title('Test Scores Distribution\n(15 bins)', fontweight='bold')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("🔍 Key Observations from the histograms above:")
print("- Most students scored between 75-95 (right-skewed distribution)")
print("- Very few students scored below 70")
print("- More bins = more detail, but can be harder to see overall pattern")

# ============================================
# PART 2: plt.hist() Parameters Explained
# ============================================

print("\n🛠️ PART 2: plt.hist() Parameters")
print("-" * 50)

# Create music popularity data for realistic example
song_popularity = np.concatenate([
    np.random.normal(30, 10, 150),  # Many unpopular songs
    np.random.normal(75, 8, 50),   # Some popular songs
    np.random.normal(90, 5, 20)    # Few mega-hits
])
song_popularity = np.clip(song_popularity, 0, 100)  # Keep in 0-100 range

plt.figure(figsize=(15, 10))

# Example 1: Different number of bins
plt.subplot(2, 3, 1)
plt.hist(song_popularity, bins=10, color='blue', alpha=0.6, edgecolor='black')
plt.title('bins=10 (default-ish)', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

plt.subplot(2, 3, 2)
plt.hist(song_popularity, bins=25, color='red', alpha=0.6, edgecolor='black')
plt.title('bins=25 (more detail)', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

plt.subplot(2, 3, 3)
plt.hist(song_popularity, bins=50, color='green', alpha=0.6, edgecolor='black')
plt.title('bins=50 (lots of detail)', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

# Example 2: Different colors and transparency
plt.subplot(2, 3, 4)
plt.hist(song_popularity, bins=20, color='purple', alpha=0.8, edgecolor='white', linewidth=2)
plt.title('Purple with white edges', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

plt.subplot(2, 3, 5)
plt.hist(song_popularity, bins=20, color='orange', alpha=0.5, edgecolor='black')
plt.title('Semi-transparent orange', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

plt.subplot(2, 3, 6)
plt.hist(song_popularity, bins=20, color='gold', alpha=0.9, edgecolor='darkred', linewidth=1.5)
plt.title('Gold with dark red edges', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

plt.tight_layout()
plt.show()

print("📋 plt.hist() Parameter Guide:")
print("• bins: Number of buckets (more bins = more detail)")
print("• color: Fill color ('blue', 'red', 'skyblue', '#FF5733', etc.)")  
print("• alpha: Transparency (0.0 = invisible, 1.0 = solid)")
print("• edgecolor: Border color around each bar")
print("• linewidth: Thickness of the border lines")

# ============================================
# PART 3: Understanding plt.scatter()
# ============================================

print("\n🎯 PART 3: plt.scatter() - SCATTER PLOTS")
print("-" * 50)

print("""
🎯 What is plt.scatter()?
A scatter plot shows RELATIONSHIPS between two variables:
- Do songs with higher danceability tend to be more popular?
- Is there a pattern between study hours and test scores?
- Are two variables correlated (connected)?

Each dot represents one data point (one song, one student, etc.)
X-position = value of first variable
Y-position = value of second variable
""")

# Generate correlated data for demonstration
n_songs = 100
danceability = np.random.beta(2, 2, n_songs)  # Values between 0-1
energy = danceability * 0.7 + np.random.normal(0, 0.2, n_songs)  # Somewhat correlated
energy = np.clip(energy, 0, 1)
popularity = danceability * 30 + energy * 40 + np.random.normal(0, 15, n_songs)
popularity = np.clip(popularity, 0, 100)

plt.figure(figsize=(15, 5))

# Basic scatter plots showing different relationships
plt.subplot(1, 3, 1)
plt.scatter(danceability, popularity, alpha=0.7, color='green', s=50)
plt.title('Danceability vs Popularity', fontweight='bold')
plt.xlabel('Danceability (0=not danceable, 1=very danceable)')
plt.ylabel('Popularity Score (0-100)')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
plt.scatter(energy, popularity, alpha=0.7, color='red', s=50)
plt.title('Energy vs Popularity', fontweight='bold')
plt.xlabel('Energy (0=low energy, 1=high energy)')
plt.ylabel('Popularity Score (0-100)')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 3)
plt.scatter(danceability, energy, alpha=0.7, color='blue', s=50)
plt.title('Danceability vs Energy', fontweight='bold')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("🔍 What to look for in scatter plots:")
print("✅ Upward trend: As X increases, Y increases (positive correlation)")
print("✅ Downward trend: As X increases, Y decreases (negative correlation)")
print("✅ Random cloud: No clear pattern (no correlation)")
print("✅ Tight clustering: Strong relationship")
print("✅ Spread out dots: Weak relationship")

# ============================================
# PART 4: plt.scatter() Parameters Explained  
# ============================================

print("\n🛠️ PART 4: plt.scatter() Parameters")
print("-" * 50)

# Generate data for parameter examples
x_vals = np.random.normal(50, 15, 80)
y_vals = x_vals * 0.8 + np.random.normal(0, 10, 80)

plt.figure(figsize=(15, 10))

# Different point sizes
plt.subplot(2, 3, 1)
plt.scatter(x_vals, y_vals, s=20, color='blue', alpha=0.7)  # Small points
plt.title('Small points (s=20)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 2)
plt.scatter(x_vals, y_vals, s=100, color='red', alpha=0.7)  # Large points
plt.title('Large points (s=100)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 3)
sizes = np.random.randint(20, 200, len(x_vals))  # Variable sizes
plt.scatter(x_vals, y_vals, s=sizes, color='green', alpha=0.6)
plt.title('Variable point sizes', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

# Different transparency levels
plt.subplot(2, 3, 4)
plt.scatter(x_vals, y_vals, s=80, color='purple', alpha=1.0)  # Solid
plt.title('Solid points (alpha=1.0)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 5)
plt.scatter(x_vals, y_vals, s=80, color='purple', alpha=0.3)  # Very transparent
plt.title('Transparent (alpha=0.3)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

# Color-coded by a third variable
plt.subplot(2, 3, 6)
colors = y_vals  # Use Y values to determine color
plt.scatter(x_vals, y_vals, s=80, c=colors, cmap='viridis', alpha=0.8)
plt.colorbar(label='Y value')
plt.title('Color-coded by Y value', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("📋 plt.scatter() Parameter Guide:")
print("• x, y: The two variables to plot against each other")
print("• s: Size of dots (default ~20, larger numbers = bigger dots)")
print("• color or c: Color ('red', 'blue', array of values for color-coding)")
print("• alpha: Transparency (0.0 = invisible, 1.0 = solid)")
print("• cmap: Color map when using c= with numerical values")

# ============================================
# PART 5: Real-World Examples from Music Lesson
# ============================================

print("\n🎵 PART 5: Music Lesson Examples")
print("-" * 50)

# Simulate realistic Spotify data
np.random.seed(42)
n_songs = 200

# Create different music genres with different characteristics
pop_songs = 50
dance_songs = 40
ballad_songs = 60
rock_songs = 50

# Pop songs: medium-high danceability, medium energy, good popularity
pop_dance = np.random.beta(3, 2, pop_songs) * 0.8 + 0.2
pop_energy = np.random.beta(2, 2, pop_songs) * 0.6 + 0.4
pop_popularity = pop_dance * 25 + pop_energy * 30 + np.random.normal(20, 10, pop_songs)

# Dance songs: very high danceability, high energy, high popularity
dance_dance = np.random.beta(4, 1, dance_songs) * 0.8 + 0.2
dance_energy = np.random.beta(3, 1, dance_songs) * 0.7 + 0.3
dance_popularity = dance_dance * 30 + dance_energy * 35 + np.random.normal(15, 8, dance_songs)

# Ballads: low danceability, low energy, variable popularity
ballad_dance = np.random.beta(1, 4, ballad_songs) * 0.5
ballad_energy = np.random.beta(1, 3, ballad_songs) * 0.4
ballad_popularity = np.random.normal(45, 20, ballad_songs)

# Rock: medium danceability, high energy, medium popularity
rock_dance = np.random.beta(2, 2, rock_songs) * 0.7 + 0.1
rock_energy = np.random.beta(4, 1, rock_songs) * 0.8 + 0.2
rock_popularity = rock_dance * 20 + rock_energy * 25 + np.random.normal(10, 15, rock_songs)

# Combine all genres
all_danceability = np.concatenate([pop_dance, dance_dance, ballad_dance, rock_dance])
all_energy = np.concatenate([pop_energy, dance_energy, ballad_energy, rock_energy])
all_popularity = np.concatenate([pop_popularity, dance_popularity, ballad_popularity, rock_popularity])
all_popularity = np.clip(all_popularity, 0, 100)

plt.figure(figsize=(15, 10))

# Histogram of popularity - shows distribution
plt.subplot(2, 3, 1)
plt.hist(all_popularity, bins=25, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Song Popularity Distribution\n(What our AI learns from)', fontweight='bold')
plt.xlabel('Popularity Score (0-100)')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

# Add interpretation text
plt.text(0.02, 0.98, 'Key Insights:\n• Most songs: 20-60 popularity\n• Few mega-hits: 80-100\n• Very few flops: 0-20', 
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8), fontsize=9)

# Scatter: Danceability vs Popularity - shows relationship
plt.subplot(2, 3, 2)
plt.scatter(all_danceability, all_popularity, alpha=0.6, color='green', s=40)
plt.title('Danceability vs Popularity\n(Is there a pattern?)', fontweight='bold')
plt.xlabel('Danceability (0=not danceable, 1=very danceable)')
plt.ylabel('Popularity Score')
plt.grid(True, alpha=0.3)

# Add trend interpretation
plt.text(0.02, 0.98, 'Pattern Found!\n• More danceable songs\n  tend to be more popular\n• But lots of variation', 
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8), fontsize=9)

# Scatter: Energy vs Popularity
plt.subplot(2, 3, 3)
plt.scatter(all_energy, all_popularity, alpha=0.6, color='red', s=40)
plt.title('Energy vs Popularity\n(Another pattern?)', fontweight='bold')
plt.xlabel('Energy (0=low energy, 1=high energy)')
plt.ylabel('Popularity Score')
plt.grid(True, alpha=0.3)

plt.text(0.02, 0.98, 'Weak Pattern:\n• High energy songs\n  slightly more popular\n• But very scattered', 
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8), fontsize=9)

# Histogram of danceability - shows feature distribution
plt.subplot(2, 3, 4)
plt.hist(all_danceability, bins=20, alpha=0.7, color='gold', edgecolor='black')
plt.title('Danceability Distribution\n(Input feature)', fontweight='bold')
plt.xlabel('Danceability Score')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

# Histogram of energy - another feature distribution
plt.subplot(2, 3, 5)
plt.hist(all_energy, bins=20, alpha=0.7, color='orange', edgecolor='black')
plt.title('Energy Distribution\n(Another input feature)', fontweight='bold')
plt.xlabel('Energy Score')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

# Color-coded scatter plot - advanced visualization
plt.subplot(2, 3, 6)
scatter = plt.scatter(all_danceability, all_energy, c=all_popularity, s=50, 
                     cmap='viridis', alpha=0.7, edgecolors='black', linewidth=0.5)
plt.colorbar(scatter, label='Popularity Score')
plt.title('Danceability vs Energy\n(Color = Popularity)', fontweight='bold')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True, alpha=0.3)

plt.text(0.02, 0.98, 'Advanced View:\n• Yellow dots = popular\n• Purple dots = unpopular\n• Shows 3 variables at once!', 
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.9), fontsize=9)

plt.tight_layout()
plt.show()

# ============================================
# PART 6: When to Use Each Plot Type
# ============================================

print("\n🎯 PART 6: When to Use Histograms vs Scatter Plots")
print("-" * 50)

print("""
📈 USE HISTOGRAMS when you want to understand:
✅ Distribution of ONE variable
✅ "What's typical?" and "What's rare?"
✅ Shape of your data (normal, skewed, bimodal)
✅ How many data points fall in different ranges

Examples in our music lesson:
• How are popularity scores distributed across all songs?
• Are most songs unpopular with few hits? Or evenly distributed?
• What's the typical danceability score?

🎯 USE SCATTER PLOTS when you want to understand:
✅ Relationship between TWO variables  
✅ "As X increases, does Y increase/decrease?"
✅ How strong is the correlation?
✅ Are there outliers or unusual patterns?

Examples in our music lesson:
• Do more danceable songs tend to be more popular?
• Is there a relationship between energy and popularity?
• Can we predict popularity from audio features?
""")

# ============================================
# PART 7: Code Templates for Students
# ============================================

print("\n💻 PART 7: Code Templates for Students")
print("-" * 50)

print("""
🔧 HISTOGRAM TEMPLATE:
```python
plt.figure(figsize=(8, 5))
plt.hist(your_data, bins=20, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Your Variable')
plt.xlabel('Variable Name')
plt.ylabel('Number of Items')
plt.grid(True, alpha=0.3)
plt.show()
```

🔧 SCATTER PLOT TEMPLATE:
```python
plt.figure(figsize=(8, 6))
plt.scatter(x_variable, y_variable, alpha=0.6, color='green', s=50)
plt.title('X Variable vs Y Variable')
plt.xlabel('X Variable Name')
plt.ylabel('Y Variable Name') 
plt.grid(True, alpha=0.3)
plt.show()
```

🔧 COMBINED ANALYSIS TEMPLATE (like our music lesson):
```python
plt.figure(figsize=(12, 4))

# Plot 1: Distribution of outcome variable
plt.subplot(1, 3, 1)
plt.hist(target_variable, bins=20, alpha=0.7, color='skyblue')
plt.title('Distribution of Target')
plt.xlabel('Target Variable')
plt.ylabel('Count')

# Plot 2: Feature 1 vs Target
plt.subplot(1, 3, 2)
plt.scatter(feature1, target_variable, alpha=0.6, color='green')
plt.title('Feature 1 vs Target')
plt.xlabel('Feature 1')
plt.ylabel('Target')

# Plot 3: Feature 2 vs Target  
plt.subplot(1, 3, 3)
plt.scatter(feature2, target_variable, alpha=0.6, color='red')
plt.title('Feature 2 vs Target')
plt.xlabel('Feature 2')
plt.ylabel('Target')

plt.tight_layout()
plt.show()
```
""")

# ============================================
# PART 8: Common Mistakes and How to Fix Them
# ============================================

print("\n⚠️ PART 8: Common Mistakes and Solutions")
print("-" * 50)

print("""
❌ MISTAKE 1: Too few bins in histogram
plt.hist(data, bins=3)  # Can't see the pattern!

✅ SOLUTION: Use 15-30 bins for most datasets
plt.hist(data, bins=20)  # Much better!

❌ MISTAKE 2: Points too small to see in scatter plot
plt.scatter(x, y, s=1)  # Tiny invisible dots

✅ SOLUTION: Use s=50-100 for visibility
plt.scatter(x, y, s=60)  # Easy to see!

❌ MISTAKE 3: No transparency with overlapping points
plt.scatter(x, y, alpha=1.0)  # Can't see overlapping points

✅ SOLUTION: Use alpha=0.6-0.7 for transparency
plt.scatter(x, y, alpha=0.6)  # Can see overlapping points!

❌ MISTAKE 4: No grid makes it hard to read values
plt.scatter(x, y)  # Hard to estimate values

✅ SOLUTION: Always add grid
plt.grid(True, alpha=0.3)  # Easy to read values!

❌ MISTAKE 5: Unclear axis labels
plt.xlabel('x')  # What is 'x'??

✅ SOLUTION: Descriptive labels
plt.xlabel('Danceability (0=not danceable, 1=very danceable)')  # Clear!
""")

print("\n🎉 SUMMARY")
print("-" * 50)
print("📈 plt.hist(): Shows DISTRIBUTION of one variable")
print("🎯 plt.scatter(): Shows RELATIONSHIP between two variables")
print("🔧 Both are essential for exploring data before training AI!")
print("💡 Use them together to understand your data completely!")

print(f"\n🎵 In our music lesson, these plots help students:")
print("• See what makes songs popular (scatter plots)")
print("• Understand their dataset (histograms)")  
print("• Discover patterns their AI will learn from")
print("• Build intuition before the 'black box' AI training")

print("\n" + "="*60)
print("Now you can create meaningful visualizations! 📊🎵🤖")