import pickle
import matplotlib.pyplot as plt

# Function to load the pickle file and create a bar chart for the incorrect runs
def plot_incorrect_runs_distribution(pickle_file_path):
    try:
        # Load the pickle file
        with open(pickle_file_path, 'rb') as f:
            results = pickle.load(f)

        # Create a dictionary to track the number of incorrect runs for each query
        incorrect_run_counts = {}

        # Iterate over each query in the results
        for query, query_results in results.items():
            # Count how many runs were incorrect for this query
            incorrect_count = sum(1 for result in query_results if not result['correct'])
            if incorrect_count > 0:  # Only count queries that were incorrect in at least one run
                if incorrect_count not in incorrect_run_counts:
                    incorrect_run_counts[incorrect_count] = 0
                incorrect_run_counts[incorrect_count] += 1

        # Prepare data for the bar chart
        x_vals = list(incorrect_run_counts.keys())
        y_vals = [incorrect_run_counts[x] for x in x_vals]

        # Plot the bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(x_vals, y_vals, color='skyblue')

        # Set chart labels and title
        plt.xlabel('Number of Incorrect Runs')
        plt.ylabel('Number of Queries')
        plt.title('Distribution of Incorrect Runs for Queries')

        # Show the plot
        plt.xticks(range(1, 11))  # To show x-axis from 1 to 10
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error loading or reading pickle file: {e}")

# Example usage
if __name__ == "__main__":
    pickle_file_path = 'results.pkl'  # Path to your pickle file
    plot_incorrect_runs_distribution(pickle_file_path)
