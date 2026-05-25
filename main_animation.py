import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

print("--- GENERATING ANIMATIONS ---")
print("Please wait, this might take 1 to 2 minutes on a phone...\n")

try:
    # Load the cleaned data we just made
    df = pd.read_csv("dataset_cleaned.csv")
    
    # Use only 60 frames to keep mobile memory safe
    anim_df = df.head(60).reset_index()

    # ==========================================
    # ANIMATION 1: HVAC Power Trend
    # ==========================================
    print("Creating Animation 1 (Power Trend)...")
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.set_xlim(0, 60)
    ax1.set_ylim(anim_df['Power'].min() - 10, anim_df['Power'].max() + 10)
    ax1.set_title("HVAC Power Volatility Over Time")
    ax1.set_ylabel("Power")
    line1, = ax1.plot([], [], lw=2, color='red')

    def init1():
        line1.set_data([], [])
        return line1,

    def update1(frame):
        line1.set_data(anim_df.index[:frame], anim_df['Power'].iloc[:frame])
        return line1,

    ani1 = FuncAnimation(fig1, update1, frames=len(anim_df), init_func=init1, blit=True)
    ani1.save("outputs/4_power_trend_animated.gif", writer=PillowWriter(fps=10))
    plt.close(fig1)
    print(" -> 1/2: Power Animation Saved!")

    # ==========================================
    # ANIMATION 2: Supply Temperature Trend
    # ==========================================
    print("Creating Animation 2 (Temperature Shift)...")
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.set_xlim(0, 60)
    ax2.set_ylim(anim_df['T_Supply'].min() - 2, anim_df['T_Supply'].max() + 2)
    ax2.set_title("Supply Temperature Shift")
    ax2.set_ylabel("T_Supply")
    line2, = ax2.plot([], [], lw=2, color='orange')

    def init2():
        line2.set_data([], [])
        return line2,

    def update2(frame):
        line2.set_data(anim_df.index[:frame], anim_df['T_Supply'].iloc[:frame])
        return line2,

    ani2 = FuncAnimation(fig2, update2, frames=len(anim_df), init_func=init2, blit=True)
    ani2.save("outputs/5_temp_trend_animated.gif", writer=PillowWriter(fps=10))
    plt.close(fig2)
    print(" -> 2/2: Temperature Animation Saved!")

    print("\nALL DONE! Check the 'outputs' folder for your two .gif files.")

except Exception as e:
    print(f"\nERROR: {e}")
