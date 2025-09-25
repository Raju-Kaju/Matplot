# Teacher Transcript: Explaining Matplotlib to High School Students
## "Making Data Come Alive with Visualizations"

**Setting:** Computer lab, students have laptops open with Python/Colab ready  
**Duration:** 25-30 minutes  
**Context:** Part of Module 1 - Music AI lesson, before training the model

---

## Opening Hook (2 minutes)

**Teacher:** "Alright everyone, close your laptops for just a second and look up here. I want you to imagine you're a detective. You've just been handed a box with 1,000 pieces of evidence - but they're all just numbers written on scraps of paper. How would you even begin to make sense of it all?"

*[Wait for student responses]*

**Student responses might include:** "Organize them?" "Look for patterns?" "Group similar ones?"

**Teacher:** "Exactly! That's exactly what data visualization does. Instead of staring at 1,000 numbers in a spreadsheet until your eyes bleed, we create pictures that let us see patterns instantly. 

Today, you're going to become data visualization detectives. We're going to take our Spotify song data - all those numbers about danceability and energy - and turn them into pictures that tell stories. And by the end of this, you'll be able to spot patterns that will help our AI predict hit songs.

Open your laptops and let's become data artists!"

---

## Section 1: Understanding the Canvas - plt.figure() (5 minutes)

**Teacher:** "First, let's talk about creating our canvas. Everyone, type this with me:"

```python
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
```

**Teacher:** "Stop right there. Before we draw anything, we need to understand what we just did. 

Think of `plt.figure(figsize=(8, 6))` like going to an art store and buying a canvas. The `figsize` is literally how big your canvas is - 8 inches wide, 6 inches tall. 

Turn to the person next to you and explain this in your own words."

*[Give students 30 seconds to discuss]*

**Teacher:** "Good! Now, why does size matter? Sarah, what happens when you try to draw a detailed picture on a tiny piece of paper?"

**Sarah:** "It gets all cramped and hard to read?"

**Teacher:** "Exactly! Same with our data plots. Watch what happens:"

```python
# Small canvas - hard to read
plt.figure(figsize=(3, 2))
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('Tiny Plot - Can You Read This?')
plt.show()

# Large canvas - much clearer
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('Much Better! Easy to Read')
plt.show()
```

**Teacher:** "See the difference? The first one looks like someone tried to write their phone number on a grain of rice. The second one is clear and professional.

Key rule: ALWAYS start with `plt.figure(figsize=...)` before you create any plot. It's like setting up your workspace before you start cooking."

---

## Section 2: Dividing Your Canvas - plt.subplot() (6 minutes)

**Teacher:** "Now here's where it gets really cool. What if I told you we could put multiple plots on the same canvas, perfectly organized, like a comic book page?

That's what `plt.subplot()` does. Let me show you something that will blow your mind:"

```python
plt.figure(figsize=(12, 4))  # Wide canvas

plt.subplot(1, 3, 1)  # What do you think these numbers mean?
plt.plot([1, 2, 3], [1, 4, 2], 'ro-')
plt.title('Plot 1')

plt.subplot(1, 3, 2)
plt.plot([1, 2, 3], [2, 1, 3], 'go-')  
plt.title('Plot 2')

plt.subplot(1, 3, 3)
plt.plot([1, 2, 3], [3, 2, 1], 'bo-')
plt.title('Plot 3')

plt.show()
```

**Teacher:** "Whoa! Three plots, perfectly arranged! But how did the computer know where to put each one?

Let's decode `plt.subplot(1, 3, 1)` together. Think of it like an address for your plot:

- First number (1): How many ROWS of plots do we want?
- Second number (3): How many COLUMNS of plots do we want?  
- Third number (1): Which POSITION are we drawing in right now?

So `plt.subplot(1, 3, 1)` means: 'I want 1 row of plots, with 3 columns, and I'm drawing in position 1.'

Marcus, which position would be in the middle?"

**Marcus:** "Position 2?"

**Teacher:** "Perfect! And the rightmost?"

**Class:** "Position 3!"

**Teacher:** "You got it! The positions are numbered like reading a book - left to right, top to bottom. Let me show you a bigger example:"

```python
plt.figure(figsize=(10, 8))

# 2 rows, 2 columns = 4 total positions
positions = [
    "Top Left",
    "Top Right", 
    "Bottom Left",
    "Bottom Right"
]

for i in range(4):
    plt.subplot(2, 2, i+1)  # Positions 1, 2, 3, 4
    plt.text(0.5, 0.5, f'Position {i+1}\n{positions[i]}', 
             ha='center', va='center', fontsize=12, 
             bbox=dict(boxstyle='round', facecolor='lightblue'))
    plt.xlim(0, 1)
    plt.ylim(0, 1)

plt.tight_layout()
plt.show()
```

**Teacher:** "See how it's like a grid? The computer reads positions just like you read words on a page.

Now, everyone practice this. Create a figure with 1 row and 4 columns, and put a simple plot in position 3. Don't worry about making it pretty - just get the positions right."

*[Give students 2-3 minutes to practice]*

**Teacher:** "Great! One more critical tip: Notice I used `plt.tight_layout()` at the end? That's like using spell-check on an essay - it automatically fixes the spacing so your plots don't crash into each other. Always use it when you have multiple subplots!"

---

## Section 3: Your First Data Story - plt.hist() (8 minutes)

**Teacher:** "Now let's get to the real magic - making our Spotify data tell stories. We're going to start with something called a histogram, and I promise this will be the most useful graph you learn this year.

First, let's load our song data:"

```python
import pandas as pd
songs_data = pd.read_csv('spotify_songs_dataset.csv')  # Our 200 songs
popularity = songs_data['popularity']
print(f"We have {len(popularity)} songs with popularity scores!")
```

**Teacher:** "Okay, so we have 200 songs, each with a popularity score from 0 to 100. But what does that actually tell us? Are most songs super popular? Are most songs flops? We can't tell just by looking at numbers.

This is where histograms come to save the day. A histogram answers the question: 'How many of my data points fall into different ranges?'

Think of it like sorting your music library. If I asked you to put all your songs into five buckets - 'Terrible', 'Bad', 'Okay', 'Good', and 'Amazing' - and then count how many songs are in each bucket, that's exactly what a histogram does!

Let's see it in action:"

```python
plt.figure(figsize=(10, 6))
plt.hist(popularity, bins=20, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('How Popular Are Our Songs?', fontsize=16, fontweight='bold')
plt.xlabel('Popularity Score (0 = nobody listens, 100 = global hit)')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)
plt.show()
```

**Teacher:** "STOP! Before we run this code, everyone make a prediction. Do you think most of our songs will be:

A) Really popular (80-100)  
B) Medium popular (40-60)  
C) Not very popular (0-40)

Turn to someone and discuss your prediction and WHY you think that."

*[Give students 1 minute to discuss]*

**Teacher:** "Okay, let's find out! Run the code!"

*[Students run the code and see the histogram]*

**Teacher:** "Whoa! What do you see? Emma, describe the pattern:"

**Emma:** "It looks like most songs are kind of in the middle, maybe around 30-60? And there aren't many super popular ones?"

**Teacher:** "Excellent observation! This is telling us a story about the music industry. Most songs are moderately popular, but very few become mega-hits. This makes sense, right? If every song was a huge hit, then being a 'hit' wouldn't be special anymore.

Now let's decode the parts of our histogram code:

- `bins=20`: We're dividing our data into 20 buckets. More bins = more detail
- `color='skyblue'`: Pretty blue color  
- `alpha=0.7`: Makes it slightly transparent so it looks nicer
- `edgecolor='black'`: Puts black lines around each bar so we can see them clearly

Watch what happens when we change the number of bins:"

```python
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.hist(popularity, bins=5, color='red', alpha=0.7, edgecolor='black')
plt.title('5 bins (less detail)')

plt.subplot(1, 3, 2) 
plt.hist(popularity, bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title('20 bins (good detail)')

plt.subplot(1, 3, 3)
plt.hist(popularity, bins=50, color='green', alpha=0.7, edgecolor='black')
plt.title('50 bins (maybe too much detail)')

plt.tight_layout()
plt.show()
```

**Teacher:** "See how more bins give you more detail, but too many bins can make it hard to see the big picture? It's like zooming in on a photo - sometimes you want to see the whole landscape, sometimes you want to see individual trees.

For most data, 15-25 bins is the sweet spot. Now everyone try this: create a histogram of the 'danceability' column from our dataset. Use 20 bins and make it your favorite color!"

*[Give students 3-4 minutes to practice]*

---

## Section 4: Finding Relationships - plt.scatter() (8 minutes)

**Teacher:** "Okay, histograms show us the distribution of ONE variable. But here's the million-dollar question for our AI project: Do certain song features actually relate to popularity?

Like, do more danceable songs tend to be more popular? Do high-energy songs get more streams? This is where scatter plots become our best friend.

A scatter plot shows the relationship between TWO variables. Every dot represents one song, and its position tells us about TWO different features of that song.

Let's investigate! Do you think more danceable songs are more popular?"

```python
danceability = songs_data['danceability'] 
popularity = songs_data['popularity']

plt.figure(figsize=(8, 6))
plt.scatter(danceability, popularity, alpha=0.6, color='green', s=50)
plt.title('The Big Question: Are Danceable Songs More Popular?')
plt.xlabel('Danceability (0 = funeral march, 1 = dance party)')
plt.ylabel('Popularity Score (0-100)')
plt.grid(True, alpha=0.3)
plt.show()
```

**Teacher:** "Everyone run this code and then tell me what you see. Look for patterns - do the dots trend upward? Downward? Random mess?"

*[Students run code and observe]*

**Teacher:** "Jake, what do you notice?"

**Jake:** "It kind of goes upward? Like, the more danceable songs seem to be more popular on average?"

**Teacher:** "YES! That's exactly right! You just discovered a CORRELATION. See how the dots generally trend from bottom-left to top-right? That's called a positive correlation - as one thing increases, the other tends to increase too.

This is HUGE for our AI project! If there's a pattern here, our AI can learn to use danceability to predict popularity!

Let me explain the scatter plot code:
- `alpha=0.6`: Makes dots semi-transparent so we can see overlapping points
- `s=50`: Size of the dots (bigger numbers = bigger dots)  
- `color='green'`: Color of all the dots

But what if we want to see MORE relationships at once? Check this out:"

```python
energy = songs_data['energy']

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(danceability, popularity, alpha=0.6, color='green', s=40)
plt.title('Danceability vs Popularity')
plt.xlabel('Danceability')
plt.ylabel('Popularity')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
plt.scatter(energy, popularity, alpha=0.6, color='red', s=40)
plt.title('Energy vs Popularity') 
plt.xlabel('Energy')
plt.ylabel('Popularity')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 3)
plt.scatter(danceability, energy, alpha=0.6, color='blue', s=40)
plt.title('Danceability vs Energy')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Teacher:** "Now we're cooking! We can see three relationships at once! This is exactly the kind of analysis that professional data scientists do.

Look at all three plots and tell me: Which relationship looks the strongest? Which one shows the clearest upward trend?"

*[Students analyze and discuss]*

**Teacher:** "This is incredible! You're doing the same analysis that Spotify's data scientists do when they build recommendation algorithms. You're literally seeing the patterns that AI will learn from.

Now here's a pro tip - what if we could show THREE variables in ONE plot? Watch this magic:"

```python
plt.figure(figsize=(8, 6))
scatter = plt.scatter(danceability, energy, c=popularity, s=60, 
                     cmap='viridis', alpha=0.8, edgecolors='black', linewidth=0.5)
plt.colorbar(scatter, label='Popularity Score')
plt.title('Danceability vs Energy (Color = Popularity)')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True, alpha=0.3)
plt.show()
```

**Teacher:** "MIND = BLOWN! The color of each dot now represents how popular that song is. Yellow/bright = popular, purple/dark = unpopular. Now we can see how ALL THREE variables relate to each other at once!

This is advanced data visualization that companies pay thousands of dollars for. And you just created it in 5 lines of code!"

---

## Section 5: Putting It All Together - Real Analysis (4 minutes)

**Teacher:** "Now let's put everything together and do some real data detective work. We're going to create the exact visualization that helps our AI understand what makes songs popular:"

```python
plt.figure(figsize=(15, 10))

# Row 1: Individual distributions
plt.subplot(2, 3, 1)
plt.hist(popularity, bins=25, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Popularity Distribution\n(What are we trying to predict?)')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 2)
plt.hist(danceability, bins=20, alpha=0.7, color='gold', edgecolor='black')
plt.title('Danceability Distribution\n(Input Feature #1)')
plt.xlabel('Danceability')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 3)
plt.hist(energy, bins=20, alpha=0.7, color='orange', edgecolor='black')
plt.title('Energy Distribution\n(Input Feature #2)')
plt.xlabel('Energy')
plt.ylabel('Number of Songs')
plt.grid(True, alpha=0.3)

# Row 2: Relationships
plt.subplot(2, 3, 4)
plt.scatter(danceability, popularity, alpha=0.6, color='green', s=40)
plt.title('Danceability → Popularity\n(Strong pattern!)')
plt.xlabel('Danceability')
plt.ylabel('Popularity')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 5)
plt.scatter(energy, popularity, alpha=0.6, color='red', s=40)
plt.title('Energy → Popularity\n(Weaker pattern)')
plt.xlabel('Energy')
plt.ylabel('Popularity')
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 6)
scatter = plt.scatter(danceability, energy, c=popularity, s=50, 
                     cmap='plasma', alpha=0.7, edgecolors='black', linewidth=0.5)
plt.colorbar(scatter, label='Popularity')
plt.title('All Variables Together\n(The full picture!)')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Teacher:** "This is it! This is the complete picture of our data. Look at what we've discovered:

1. **Top row**: Shows us the distribution of each variable individually
2. **Bottom row**: Shows us how variables relate to each other

From this analysis, we can predict that our AI will probably find danceability more useful than energy for predicting popularity. And we'd be right!

The best part? When our AI makes predictions later, they won't seem like magic anymore. You've already seen the patterns it's going to learn from!"

---

## Closing & Transition (2 minutes)

**Teacher:** "Alright everyone, let's recap what you just mastered:

✅ **plt.figure(figsize=(w,h))** - Set up your canvas  
✅ **plt.subplot(rows, cols, position)** - Organize multiple plots  
✅ **plt.hist()** - Show distribution of one variable  
✅ **plt.scatter()** - Show relationships between two variables  
✅ **Professional data analysis** - You're doing real data science!

But here's the crazy part - everything you just discovered by looking at these plots? Our AI is about to learn the exact same patterns automatically. 

You've just done the detective work to understand WHY our AI will be successful at predicting hit songs. When we train our model in the next section and it achieves 75% accuracy, you'll know exactly why - because you've already seen the patterns in the data!

Questions before we move on to training our AI music predictor?"

*[Address any questions]*

**Teacher:** "Perfect! Save your plots - you'll want to show them to your friends. Up next: we're going to train an AI that can predict whether any song will be a hit or flop based on exactly the patterns you just discovered. Let's go build some artificial intelligence!"

---

## Teacher Notes:

### **Timing Management:**
- **Total time**: ~25-30 minutes
- **If running short**: Skip the 3-variable color-coded scatter plot
- **If running long**: Have students work in pairs to speed up coding

### **Common Student Questions & Responses:**

**Q**: "Why do we need alpha transparency?"  
**A**: "When dots overlap, you can't see how many are there. Transparency lets you see 'hot spots' where lots of dots pile up."

**Q**: "What if there's no pattern in the scatter plot?"  
**A**: "That's valuable information too! It tells us that feature won't be useful for our AI model."

**Q**: "Can we use other colors?"  
**A**: "Absolutely! Try 'purple', 'crimson', 'forestgreen', or even hex codes like '#FF5733'."

### **Extension Activities:**
- Have advanced students try different color maps (`cmap='cool'`, `cmap='hot'`)
- Challenge students to create a 2×2 subplot layout
- Ask students to find the least correlated variables in the dataset

### **Assessment Opportunities:**
- **Formative**: Walk around and check subplot layouts
- **Quick check**: "Raise your hand if your scatter plot shows an upward trend"
- **Exit ticket**: "Name one pattern you discovered in the data today"

This transcript balances explanation with hands-on practice, building from simple concepts to complex analysis while maintaining student engagement through predictions and discoveries.