from matplotlib import pyplot

def main():
    # List of continent names
    continents = ['North America', 'South America', 'Europe',
                'Asia', 'Africa', 'Australia', 'Antarctica']

    # measured areas of the continents
    data = [21330000, 17461112, 22134900, 31033131, 29648481, 8486460,
            13720000]

    # Create a pie chart
    pyplot.pie(data, labels=continents)
    # Create a legend
    pyplot.legend(continents, title="Continents",
                loc="upper left",
                bbox_to_anchor=(-0.4, 1.1))


    pyplot.show()
    
main()