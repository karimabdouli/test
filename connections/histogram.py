from random import randint
import matplotlib.pyplot as plt

def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    n = len(bins)
    result = [[0]*(n-1), ['']*(n-1)]
    for i in range(n-1) :
        result[1][i] = '%d' %bins[i] + '-' +'%d' %bins[i+1]
    for j in data :
        for k in range(1,n) :
            if j < bins[k] :
                result[0][k-1] += 1
                break
    return result


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    plt.bar(bins_count[1], height = bins_count[0], color = 'dodgerblue')
    plt.xlabel('some metric bins')
    plt.ylabel('count')
    plt.title('Distribution of something')
    plt.show()
    
    
if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
