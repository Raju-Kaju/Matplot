import matplotlib.pyplot as plt
import numpy as np

print("📊 Understanding plt.figure() and plt.subplot()")
print("=" * 60)

# ============================================
# PART 1: Understanding plt.figure(figsize)
# ============================================

print("\n🔍 PART 1: plt.figure(figsize=(width, height))")
print("-" * 50)

print("""
plt.figure(figsize=(12, 4)) creates a new figure (like a blank canvas) with:
- Width: 12 inches
- Height: 4 inches

Think of it as setting up your canvas before you start painting!
""")

# Example: Different figure sizes
fig1 = plt.figure(figsize=(8, 3))  # Wide and short
plt.plot([1, 2, 3, 4], [1, 4, 2, 3], 'b-o', linewidth=2, markersize=8)
plt.title('Small Figure: 8x3 inches', fontsize=14, fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)
plt.show()

fig2 = plt.figure(figsize=(6, 8))  # Tall and narrow  
plt.plot([1, 2, 3, 4], [1, 4, 2, 3], 'r-s', linewidth=2, markersize=8)
plt.title('Tall Figure: 6x8 inches', fontsize=14, fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)
plt.show()

print("""
Key Points about plt.figure(figsize):
✅ figsize=(width, height) - measurements in INCHES
✅ Default size is usually (6.4, 4.8) if not specified
✅ Larger figures = more detail, but take more space
✅ Must be called BEFORE creating plots
""")

# ============================================
# PART 2: Understanding plt.subplot()
# ============================================

print("\n🔍 PART 2: plt.subplot(rows, cols, index)")
print("-" * 50)

print("""
plt.subplot(1, 3, 1) means:
- 1 row of subplots
- 3 columns of subplots  
- Position 1 (first subplot)

Think of it as dividing your canvas into a grid!
""")

# Example: Basic subplot usage
plt.figure(figsize=(15, 4))  # Wide canvas for 3 side-by-side plots

# Subplot 1: Position 1 (leftmost)
plt.subplot(1, 3, 1)  # 1 row, 3 columns, position 1
plt.plot([1, 2, 3, 4], [2, 5, 3, 8], 'bo-', linewidth=2, markersize=8)
plt.title('Subplot 1 (Left)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)

# Subplot 2: Position 2 (middle)
plt.subplot(1, 3, 2)  # 1 row, 3 columns, position 2
plt.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5], color=['red', 'green', 'blue', 'orange'])
plt.title('Subplot 2 (Middle)', fontweight='bold')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)

# Subplot 3: Position 3 (rightmost)
plt.subplot(1, 3, 3)  # 1 row, 3 columns, position 3
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), 'g-', linewidth=2, label='sin(x)')
plt.title('Subplot 3 (Right)', fontweight='bold')
plt.xlabel('X values')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()  # Automatically adjusts spacing
plt.show()

# ============================================
# PART 3: Different Subplot Arrangements
# ============================================

print("\n🔍 PART 3: Different Subplot Arrangements")
print("-" * 50)

# Example 1: 2 rows, 2 columns (2x2 grid)
print("Example 1: 2x2 Grid of Subplots")
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)  # Top-left
plt.plot([1, 2, 3], [1, 4, 2], 'ro-')
plt.title('Top Left (2,2,1)')
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)  # Top-right
plt.plot([1, 2, 3], [2, 1, 3], 'go-')
plt.title('Top Right (2,2,2)')
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 3)  # Bottom-left
plt.plot([1, 2, 3], [3, 2, 4], 'bo-')
plt.title('Bottom Left (2,2,3)')
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)  # Bottom-right
plt.plot([1, 2, 3], [1, 3, 1], 'mo-')
plt.title('Bottom Right (2,2,4)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Example 2: 3 rows, 1 column (vertical stack)
print("\nExample 2: 3x1 Vertical Stack")
plt.figure(figsize=(6, 12))

plt.subplot(3, 1, 1)  # Top
plt.bar(['Mon', 'Tue', 'Wed'], [20, 35, 30], color='skyblue')
plt.title('Top Plot (3,1,1)')
plt.ylabel('Temperature')

plt.subplot(3, 1, 2)  # Middle
plt.plot([1, 2, 3, 4, 5], [10, 15, 13, 17, 20], 'g-o')
plt.title('Middle Plot (3,1,2)')
plt.ylabel('Sales')

plt.subplot(3, 1, 3)  # Bottom
plt.hist([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5, color='orange', alpha=0.7)
plt.title('Bottom Plot (3,1,3)')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# ============================================
# PART 4: Real-World Example from Our Music Lesson
# ============================================

print("\n🔍 PART 4: Music Lesson Example")
print("-" * 50)

# Simulate some music data for demonstration
np.random.seed(42)
n_songs = 200
danceability = np.random.beta(2, 2, n_songs)
energy = np.random.beta(2, 2, n_songs)
popularity = danceability * 40 + energy * 30 + np.random.normal(0, 10, n_songs)
popularity = np.clip(popularity, 0, 100)

print("Creating the exact visualization from our music lesson...")

# This is the code from our lesson
plt.figure(figsize=(12, 4))  # Wide canvas for 3 side-by-side plots

# Plot 1: Distribution of popularity scores
plt.subplot(1, 3, 1)  # 1 row, 3 columns, position 1 (left)
plt.hist(popularity, bins=20, alpha=0.7, color='skyblue')
plt.title('Song Popularity Distribution')
plt.xlabel('Popularity Score')
plt.ylabel('Number of Songs')

# Plot 2: Danceability vs Popularity
plt.subplot(1, 3, 2)  # 1 row, 3 columns, position 2 (middle)
plt.scatter(danceability, popularity, alpha=0.5, color='green')
plt.title('Danceability vs Popularity')
plt.xlabel('Danceability')
plt.ylabel('Popularity')

# Plot 3: Energy vs Popularity
plt.subplot(1, 3, 3)  # 1 row, 3 columns, position 3 (right)
plt.scatter(energy, popularity, alpha=0.5, color='red')
plt.title('Energy vs Popularity')
plt.xlabel('Energy')
plt.ylabel('Popularity')

plt.tight_layout()  # Prevents overlapping
plt.show()

# ============================================
# PART 5: Common Patterns and Best Practices
# ============================================

print("\n🔍 PART 5: Subplot Numbering System")
print("-" * 50)

print("""
Subplot Position Numbering (like reading a book):

For 2x3 grid (2 rows, 3 columns):
┌─────┬─────┬─────┐
│  1  │  2  │  3  │  ← First row
├─────┼─────┼─────┤
│  4  │  5  │  6  │  ← Second row  
└─────┴─────┴─────┘

Code examples:
plt.subplot(2, 3, 1)  # Top-left
plt.subplot(2, 3, 2)  # Top-middle
plt.subplot(2, 3, 3)  # Top-right
plt.subplot(2, 3, 4)  # Bottom-left
plt.subplot(2, 3, 5)  # Bottom-middle
plt.subplot(2, 3, 6)  # Bottom-right
""")

# Visual demonstration of numbering
fig = plt.figure(figsize=(12, 6))
positions = [(2, 3, i+1) for i in range(6)]
titles = ['Position 1', 'Position 2', 'Position 3', 'Position 4', 'Position 5', 'Position 6']

for i, (pos, title) in enumerate(zip(positions, titles)):
    plt.subplot(*pos)
    plt.text(0.5, 0.5, f'subplot({pos[0]}, {pos[1]}, {pos[2]})\n{title}', 
             ha='center', va='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xticks([])
    plt.yticks([])

plt.suptitle('Subplot Numbering System (2 rows × 3 columns)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ============================================
# PART 6: Best Practices and Tips
# ============================================

print("\n💡 BEST PRACTICES AND TIPS")
print("-" * 50)

print("""
🎯 Key Guidelines:

1. ALWAYS call plt.figure(figsize=...) BEFORE plt.subplot()
   ✅ Correct: plt.figure(figsize=(12,4)) then plt.subplot(1,3,1)
   ❌ Wrong: plt.subplot(1,3,1) then plt.figure(figsize=(12,4))

2. Use plt.tight_layout() to prevent overlapping
   - Call it AFTER all subplots are created
   - Automatically adjusts spacing between plots

3. Choose figsize based on your layout:
   - Wide layouts: figsize=(15, 5) for 1 row, multiple columns
   - Tall layouts: figsize=(6, 12) for multiple rows, 1 column  
   - Square grids: figsize=(10, 10) for equal rows and columns

4. Common subplot patterns:
   - plt.subplot(1, 3, i) → 3 plots side by side
   - plt.subplot(2, 2, i) → 2×2 grid of plots
   - plt.subplot(3, 1, i) → 3 plots stacked vertically

5. Alternative syntax (same result):
   - plt.subplot(1, 3, 1) 
   - plt.subplot(131)  ← shorthand when all digits are < 10
""")

# Example of good vs bad spacing
print("\nExample: With and Without tight_layout()")

# Without tight_layout - plots overlap
fig = plt.figure(figsize=(10, 8))
fig.suptitle('WITHOUT tight_layout() - Plots Overlap!', fontsize=14, color='red')

for i in range(1, 5):
    plt.subplot(2, 2, i)
    plt.plot([1, 2, 3], [1, 4, 2], 'o-')
    plt.title(f'Plot {i} - This title might overlap!')
    plt.xlabel('X axis label that might get cut off')
    plt.ylabel('Y axis')

plt.show()

# With tight_layout - proper spacing
fig = plt.figure(figsize=(10, 8))
fig.suptitle('WITH tight_layout() - Perfect Spacing!', fontsize=14, color='green')

for i in range(1, 5):
    plt.subplot(2, 2, i)
    plt.plot([1, 2, 3], [1, 4, 2], 'o-')
    plt.title(f'Plot {i} - Clear and readable!')
    plt.xlabel('X axis label fits perfectly')
    plt.ylabel('Y axis')

plt.tight_layout()  # This makes all the difference!
plt.show()

print("\n🎉 Now you understand plt.figure() and plt.subplot()!")
print("Use these tools to create organized, professional-looking visualizations!")