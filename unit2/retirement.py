import pylab as plt

# monthly = monthly contribution to my retirement
# rate = yearly interest rate earned
# terms = number of months to iterate 
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings

def displayRetireWithMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='retire: ' + str(monthly))
        plt.legend(loc='upper left')

def displayRetireWithRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label='retire: ' + str(month) + 
                ':' + str(int(rate*100)))
        plt.legend(loc='upper left')

def displayRetireWithMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rateLabel = rateLabels[j % len(rateLabels)]
            xvals, yvals = retire(monthlies[i], rates[j], terms)
            plt.plot(xvals, yvals,
            monthLabel+rateLabel,
            label='retire: ' + str(monthlies[i]) + ':' + str(int(rates[j]*100)))
            plt.legend(loc='upper left')

monthlies = range(500, 1200, 200)
rates = [.03, .05, .07]

# displayRetireWithMonthlies(range(500, 1200, 100), .05, 40 * 12)
# displayRetireWithRates(800, [.03, .05, .07], 40 * 12)
# displayRetireWithMonthsAndRates(monthlies, rates, 40*12)
plt.show()