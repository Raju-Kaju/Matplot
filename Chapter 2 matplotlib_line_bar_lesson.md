# Module 1B Lesson Plan: "Music Genre Showdown"
## Line Plots & Bar Charts for AI Visualization

**Duration:** 20 minutes  
**Students:** High School (Ages 14-18)  
**Prerequisites:** Module 1A (figure, subplot, hist, scatter)  
**Tools:** Google Colab (or Jupyter Notebook)

---

## Opening Hook (2 minutes)

### Teacher Script:
"Alright everyone, you've become pros at spotting patterns with histograms and scatter plots. But what if I told you there are two more types of plots that are absolutely essential for AI work - and they're going to help us answer some burning questions about music?

Today we're going to settle some debates:
- Which music genre REALLY dominates the charts?
- Has music gotten more energetic over the decades?
- Which artists consistently produce hits?

We're going to learn two new plot types that professional data scientists use every single day: **bar charts** for comparing categories, and **line plots** for showing trends over time. 

By the end of these 20 minutes, you'll have the complete matplotlib toolkit you need for any AI project. Ready to crown the ultimate music genre champion?"

---

## Section 1: The Genre Battle - Bar Charts (8 minutes)

### Teacher Script:
"First, let's settle the ultimate music debate: which genre produces the most popular songs? For this, we need a bar chart - think of it as a visual scorecard where each bar represents how well each genre performs."

```python
# Let's extend our music dataset with genre information
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up our data (building on previous lesson)
np.random.seed(42)

# Create genre data
genres = ['Pop', 'Hip-Hop', 'Rock', 'Electronic', 'R&B/Soul', 'Country']
n_songs_per_genre = [40, 35, 30, 25, 25, 20]  # Different sample sizes

print("🎵 Welcome to the Ultimate Genre Showdown!")
print("=" * 50)

# Calculate average popularity by genre (with realistic differences)
genre_avg_popularity = {
    'Pop': 78.5,
    'Hip-Hop': 76.2, 
    'Electronic': 82.1,
    'Rock': 72.8,
    'R&B/Soul': 74.6,
    'Country': 69.3
}

print("📊 Average popularity by genre:")
for genre, avg in genre_avg_popularity.items():
    print(f"{genre}: {avg:.1f}")
```

### Teacher Explanation:
**Teacher:** "Now, I could just read you these numbers, but that's boring and hard to remember. Instead, let's create a bar chart that makes the winner obvious at a glance!"

```python
# Create our first bar chart
plt.figure(figsize=(10, 6))

genres_list = list(genre_avg_popularity.keys())
popularity_scores = list(genre_avg_popularity.values())

plt.bar(genres_list, popularity_scores, 
        color=['hotpink', 'purple', 'red', 'gold', 'navy', 'brown'],
        alpha=0.8, edgecolor='black', linewidth=1)

plt.title('Genre Popularity Showdown: Which Genre Wins?', 
          fontsize=16, fontweight='bold')
plt.xlabel('Music Genre')
plt.ylabel('Average Popularity Score')
plt.grid(True, alpha=0.3, axis='y')  # Only horizontal grid lines

# Rotate x-labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Interactive Discussion:
**Teacher:** "STOP! Before we run this code, everyone make a prediction. Which genre do you think will have the tallest bar? Turn to someone next to you and make your guess, then explain why."

*[Give students 30 seconds to discuss]*

**Teacher:** "Okay, let's find out! Run the code!"

*[Students run code and see results]*

**Teacher:** "Whoa! What do you see? Maya, what's the winner?"

**Maya:** "Electronic music has the highest bar!"

**Teacher:** "Exactly! And notice how easy it is to compare all the genres at once. Your brain can instantly process this visual comparison, while it would take much longer to compare a list of numbers.

Let me explain the key parts of our bar chart code:
- `plt.bar()` creates the bars (different from `plt.hist()` which bins data)
- `color=['hotpink', 'purple', ...]` gives each genre its own color
- `edgecolor='black'` puts borders around bars for clarity
- `plt.xticks(rotation=45)` tilts the genre names so they don't overlap

Now everyone try this: change the colors to your favorite colors and add your name to the title!"

*[Give students 2-3 minutes to customize]*

### Advanced Bar Chart Features:
```python
# Let's make it even more professional
plt.figure(figsize=(12, 7))

# Create bars and capture the bar objects
bars = plt.bar(genres_list, popularity_scores, 
               color=['hotpink', 'purple', 'red', 'gold', 'navy', 'brown'],
               alpha=0.8, edgecolor='black', linewidth=1)

# Add value labels on top of each bar
for bar, score in zip(bars, popularity_scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{score:.1f}', ha='center', va='bottom', fontweight='bold')

plt.title('Music Genre Popularity Championship 🏆', fontsize=18, fontweight='bold')
plt.xlabel('Music Genre', fontsize=12)
plt.ylabel('Average Popularity Score', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45)

# Highlight the winner
max_idx = popularity_scores.index(max(popularity_scores))
bars[max_idx].set_color('gold')
bars[max_idx].set_edgecolor('darkgoldenrod')
bars[max_idx].set_linewidth(3)

plt.tight_layout()
plt.show()
```

**Teacher:** "Now that's a professional visualization! Notice how we:
- Added exact numbers on top of each bar
- Highlighted the winner in gold
- Made the title more engaging with an emoji
- Added professional styling

This is exactly how data scientists present results to executives!"

---

## Section 2: Time Travel with Music - Line Plots (8 minutes)

### Teacher Script:
"Bar charts are perfect for comparing categories, but what if we want to show how something changes over time? That's where line plots become our best friend. Let's investigate: has music gotten more energetic over the decades?"

```python
# Create time series data for decades
decades = ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
avg_energy_by_decade = [0.45, 0.52, 0.58, 0.65, 0.72, 0.78]
avg_danceability_by_decade = [0.48, 0.55, 0.62, 0.68, 0.75, 0.79]

print("🕺 Music Evolution Over Time:")
print("Decade -> Energy | Danceability")
for decade, energy, dance in zip(decades, avg_energy_by_decade, avg_danceability_by_decade):
    print(f"{decade}: {energy:.2f} | {dance:.2f}")
```

### Teacher Explanation:
**Teacher:** "Again, looking at numbers is hard. But a line plot will show us the trend instantly!"

```python
# Create our first line plot
plt.figure(figsize=(10, 6))

plt.plot(decades, avg_energy_by_decade, 'ro-', linewidth=3, markersize=8, 
         label='Energy Level')
plt.title('Has Music Gotten More Energetic Over Time?', 
          fontsize=16, fontweight='bold')
plt.xlabel('Decade')
plt.ylabel('Average Energy Score (0-1)')
plt.grid(True, alpha=0.3)
plt.legend()

# Rotate x-labels
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Teacher:** "Look at that beautiful upward trend! The line makes it crystal clear that music has gotten progressively more energetic since the 1970s. 

Key parts of line plot code:
- `plt.plot()` creates connected lines (different from scattered dots)
- `'ro-'` means red circles connected by lines
- `linewidth=3` makes the line thick and easy to see
- `markersize=8` makes the dots bigger
- `label='Energy Level'` creates a legend entry

But here's where it gets really cool - what if we want to compare TWO trends on the same plot?"

### Multiple Lines - The Ultimate Comparison:
```python
# The power of multiple line plots
plt.figure(figsize=(12, 7))

plt.plot(decades, avg_energy_by_decade, 'ro-', linewidth=3, markersize=8, 
         label='Energy Level', alpha=0.8)
plt.plot(decades, avg_danceability_by_decade, 'bo-', linewidth=3, markersize=8, 
         label='Danceability', alpha=0.8)

plt.title('Music Evolution: Energy vs Danceability Over Time 🎵', 
          fontsize=16, fontweight='bold')
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Average Score (0-1)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12, loc='lower right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Teacher:** "WOW! Now we can see both trends at the same time. What do you notice? Jake, what's happening to both energy and danceability?"

**Jake:** "They're both going up, but danceability is going up faster?"

**Teacher:** "Brilliant observation! Both are increasing, but danceability (blue line) has a steeper slope. This tells us that modern music isn't just more energetic - it's also way more danceable than music from the 1970s.

This is exactly the kind of analysis that helps AI algorithms understand music trends!"

### Interactive Challenge:
**Teacher:** "Now your turn! I want everyone to:
1. Change the line colors to your favorites
2. Try different line styles: `'s--'` (squares with dashes), `'^:'` (triangles with dots)
3. Add a creative title with your name

You have 3 minutes - go!"

*[Students practice customization]*

---

## Section 3: The Complete Toolkit - Combining Everything (6 minutes)

### Teacher Script:
"Now for the grand finale - let's combine everything we've learned into one professional analysis that would impress any data scientist!"

```python
# The ultimate music analysis dashboard
plt.figure(figsize=(15, 10))

# Top left: Genre comparison (bar chart)
plt.subplot(2, 2, 1)
bars = plt.bar(genres_list, popularity_scores, 
               color=['hotpink', 'purple', 'red', 'gold', 'navy', 'brown'],
               alpha=0.8, edgecolor='black')
plt.title('Genre Popularity Ranking', fontweight='bold')
plt.ylabel('Average Popularity')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')

# Top right: Time trends (line plot)
plt.subplot(2, 2, 2)
plt.plot(decades, avg_energy_by_decade, 'ro-', linewidth=2, label='Energy')
plt.plot(decades, avg_danceability_by_decade, 'bo-', linewidth=2, label='Danceability')
plt.title('Music Evolution Over Time', fontweight='bold')
plt.ylabel('Score (0-1)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Bottom left: Distribution (histogram from previous lesson)
sample_popularity = np.random.normal(75, 12, 200)
sample_popularity = np.clip(sample_popularity, 0, 100)
plt.subplot(2, 2, 3)
plt.hist(sample_popularity, bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
plt.title('Song Popularity Distribution', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

# Bottom right: Relationship (scatter plot from previous lesson)
sample_dance = np.random.beta(2, 2, 200) * 0.8 + 0.2
sample_pop = sample_dance * 40 + np.random.normal(35, 15, 200)
sample_pop = np.clip(sample_pop, 0, 100)
plt.subplot(2, 2, 4)
plt.scatter(sample_dance, sample_pop, alpha=0.6, color='purple', s=30)
plt.title('Danceability vs Popularity', fontweight='bold')
plt.xlabel('Danceability')
plt.ylabel('Popularity')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Teacher:** "THIS is what professional data analysis looks like! We have:
- **Bar chart** showing which genres win
- **Line plot** showing trends over time  
- **Histogram** showing overall distribution
- **Scatter plot** showing relationships

This is exactly the kind of comprehensive analysis that AI companies use to understand their data before training models!"

### Essential Customization & Saving:
```python
# Professional touches every data scientist should know
plt.figure(figsize=(10, 6))

# Create a professional line plot
plt.plot(decades, avg_energy_by_decade, 'o-', linewidth=3, markersize=10, 
         color='darkblue', label='Energy Trend')

# Professional styling
plt.title('Music Energy Evolution: 1970s to 2020s', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=14, fontweight='bold')
plt.ylabel('Average Energy Score', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.4, linestyle='--')
plt.legend(fontsize=12, framealpha=0.9, shadow=True)

# Make it look professional
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save the plot (essential skill!)
plt.savefig('music_energy_analysis.png', dpi=300, bbox_inches='tight')
print("📊 Plot saved as 'music_energy_analysis.png'")
plt.show()
```

**Teacher:** "And there's one more crucial skill - `plt.savefig()`! This saves your beautiful visualizations so you can:
- Include them in reports
- Share them with friends
- Add them to presentations
- Build a portfolio of your data science work

The parameters:
- `dpi=300` makes it high resolution
- `bbox_inches='tight'` removes extra white space"

---

## Section 4: Quick Practice & Wrap-up (2 minutes)

### Teacher Script:
"Let's do a lightning round! I want everyone to create ONE plot in the next 90 seconds. Choose either:

**Option A: Your Favorite Artists Bar Chart**
```python
artists = ['Taylor Swift', 'Drake', 'Ed Sheeran', 'Billie Eilish']
hit_counts = [12, 15, 8, 7]  # Number of hit songs
plt.bar(artists, hit_counts, color='gold')
plt.title('Who Has the Most Hit Songs?')
plt.show()
```

**Option B: Study Hours Over the Week Line Plot**
```python
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
study_hours = [2, 3, 2.5, 3, 1, 0.5, 1]
plt.plot(days, study_hours, 'go-', linewidth=2)
plt.title('My Study Schedule')
plt.ylabel('Hours Studied')
plt.show()
```

GO!"

*[Students quickly create plots]*

**Teacher:** "Time's up! Show me your plots by holding up your screens!"

*[Quick gallery walk/celebration of student work]*

---

## Closing & AI Connection (2 minutes)

### Teacher Script:
"Outstanding work, everyone! In just 20 minutes, you've mastered the complete matplotlib toolkit:

✅ **Bar charts** - Compare categories (genres, artists, models)  
✅ **Line plots** - Show trends over time (learning curves, performance)  
✅ **Histograms** - Show distributions  
✅ **Scatter plots** - Show relationships  
✅ **Professional styling** - Clear labels, grids, legends  
✅ **Saving plots** - Share your results  

But here's the amazing part: these aren't just pretty pictures. In our AI music predictor project:
- **Bar charts** will show which features are most important
- **Line plots** will show how our AI improves during training
- **Histograms** will show the distribution of predictions
- **Scatter plots** will show actual vs predicted results

You now have every visualization tool you need for any AI or data science project. When we train our AI model next class, every chart it produces will use these exact techniques you just mastered!

Questions before we move on to actual AI training?"

*[Address any questions]*

**Teacher:** "Perfect! Next class: we take everything you've learned and use it to build an AI that predicts hit songs. You're going to see these visualization skills in action as we analyze our AI's performance step by step. Get ready to become AI music prediction experts!"

---

## Teacher Notes:

### **Timing Breakdown:**
- **Hook + Setup**: 2 minutes
- **Bar charts**: 8 minutes  
- **Line plots**: 8 minutes
- **Combined analysis**: 6 minutes
- **Practice + wrap**: 2 minutes
- **Total**: 20 minutes

### **Key Learning Objectives:**
- Create and customize bar charts for category comparisons
- Create and customize line plots for trend analysis
- Combine multiple plot types in professional layouts
- Save visualizations for sharing and reports
- Connect visualization skills to AI applications

### **Assessment Opportunities:**
- **Formative**: Quick customization challenges throughout
- **Participation**: Predictions and observations during discussions  
- **Technical**: Successfully running and modifying code
- **Understanding**: Connecting plot types to appropriate data questions

### **Extension for Advanced Students:**
- Multiple line plots with different y-axes
- Stacked bar charts for comparing subcategories  
- Adding annotations and arrows to highlight key points
- Creating custom color palettes

### **Common Student Questions & Responses:**

**Q**: "When should I use a bar chart vs line plot?"  
**A**: "Bar chart: comparing categories (genres, teams). Line plot: showing change over time (trends, growth)."

**Q**: "Can I put different types of plots in the same figure?"  
**A**: "Absolutely! That's what makes subplot() so powerful - mix and match as needed."

**Q**: "How do I know what colors to use?"  
**A**: "Start with defaults, then customize. Avoid red/green together (colorblind issues). Use consistent colors for the same data across plots."

This lesson perfectly complements the existing histogram/scatter plot foundation and gives students the complete matplotlib toolkit they need for professional AI visualization work!