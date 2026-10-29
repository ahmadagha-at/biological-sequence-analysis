import sys
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python ex03_012314193.py "
            "<sequence_one> <sequence_two> <window_size>"
        )
        return 2

    sequence_one = sys.argv[1]
    sequence_two = sys.argv[2]

    try:
        window_size = int(sys.argv[3])
    except ValueError:
        print("Error: window_size must be an integer.")
        return 2

    if window_size <= 0 or window_size % 2 == 0:
        print("Error: window_size must be a positive odd integer.")
        return 2

    if not sequence_one or not sequence_two:
        print("Error: both sequences must be non-empty.")
        return 2

    half_window = window_size // 2
    x_positions = []
    y_positions = []

    # Valid center positions in sequence_two
    for y in range(half_window, len(sequence_two) - half_window):
        window_two = sequence_two[y - half_window:y + half_window + 1]

        # Valid center positions in sequence_one
        for x in range(half_window, len(sequence_one) - half_window):
            window_one = sequence_one[x - half_window:x + half_window + 1]

            if window_one == window_two:
                x_positions.append(x)
                y_positions.append(y)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 7))

    # Draw a dot for each match
    ax.scatter(x_positions, y_positions, color="black", marker=".", s=100)

    ax.set_xticks(range(len(sequence_one)))
    ax.set_xticklabels(list(sequence_one), family="monospace")

    ax.set_yticks(range(len(sequence_two)))
    ax.set_yticklabels(list(sequence_two), family="monospace")

    ax.set_xlim(-0.5, len(sequence_one) - 0.5)
    ax.set_ylim(len(sequence_two) - 0.5, -0.5)
    ax.set_aspect("equal")

    ax.set_xlabel("Sequence one")
    ax.set_ylabel("Sequence two")
    ax.set_title(f"Dot plot (window size = {window_size})")

    plt.tight_layout()
    plt.show()
    return 0


if __name__ == "__main__":
    sys.exit(main())