""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	 	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	 	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 		  		  		    	 		 		   		 		  
or edited.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	 	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Student Name: Ari Takvorian 		  	   		 	 	 		  		  		    	 		 		   		 		  
GT User ID: atakvorian7  	   		 	 	 		  		  		    	 		 		   		 		  
GT ID: 903304559  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def author():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return "atakvorian7"  # replace tb34 with your Georgia Tech username.
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def gtid():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return 903304559  # replace with your GT ID number
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    result = False  		  	   		 	 	 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	 	 		  		  		    	 		 		   		 		  
        result = True  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return result  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  

def simulate_episode_experiment_one(win_prob, n_spins=1000):

    total_winnings = 0
    spin_results = []
    results_by_spin = [0]
    last_result = True
    bet_amount = 0

    for i in range(n_spins):

        if total_winnings < 80:

            if last_result:
                bet_amount = 1

            if get_spin_result(win_prob):
                last_result = True
                total_winnings += bet_amount
                spin_results.append(bet_amount)
                results_by_spin.append(results_by_spin[i] + bet_amount)
            else:
                total_winnings -= bet_amount
                spin_results.append(-bet_amount)
                results_by_spin.append(results_by_spin[i] - bet_amount)

                if last_result:
                    last_result = False
                    bet_amount = 1
                else:
                    bet_amount = bet_amount*2

        else:
            spin_results.append('')
            results_by_spin.append(total_winnings)

    return total_winnings, spin_results, results_by_spin


def experiment_one(win_prob):

    ## FIGURE ONE ##
    results = []

    eighty = 0
    not_eighty = 0

    for i in range(10):
        total_winnings, _, results_by_spin = simulate_episode_experiment_one(win_prob)
        results.append(results_by_spin)
        plt.plot(results_by_spin, label=f'Episode #{i+1}')

        if total_winnings == 80:
            eighty += 1
        else:
            not_eighty += 1

    # print(f'Eighty: {eighty}')
    # print(f'Not Eighty: {not_eighty}')
    # print(f'Proportion: {eighty/(eighty+not_eighty)}')

    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Accumulated Winnings ($)')
    plt.legend()
    plt.title('Figure 1 - Accumulated Winnings ($)')
    plt.savefig('images/figure_one')

    plt.show()

    ## FIGURE TWO AND THREE ##
    results = []

    for i in range(1000):
        total_winnings, spin_results, results_by_spin = simulate_episode_experiment_one(win_prob)
        results.append(results_by_spin)

    transposed_data = zip(*results)
    means = []
    medians = []
    stds = []
    for col in transposed_data:
        means.append(np.mean(col))
        medians.append(np.median(col))
        stds.append(np.std(col, ddof=0))

    plt.plot(means)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Mean Accumulated Winnings ($)')
    plt.title('Figure 2 - Mean Accumulated Winnings ($)')
    plt.savefig('images/figure_two')
    plt.show()

    upper = [m + s for m, s in zip(medians, stds)]
    lower = [m - s for m, s in zip(medians, stds)]

    plt.plot(medians, label="Median", color="blue")
    plt.plot(upper, label="Median + Std Dev", linestyle="--", color="green")
    plt.plot(lower, label="Median - Std Dev", linestyle="--", color="red")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Median Accumulated Winnings ($)')
    plt.title('Figure 3 - Median Accumulated Winnings ($)')
    plt.savefig('images/figure_three')
    plt.show()


def simulate_episode_experiment_two(win_prob, n_spins=1000):
    total_winnings = 0
    spin_results = []
    results_by_spin = [0]
    last_result = True
    bet_amount = 0

    for i in range(n_spins):

        if total_winnings <= -256 or total_winnings >= 80:
            spin_results.append('')
            results_by_spin.append(total_winnings)
            continue

        if last_result:
            bet_amount = 1

        bankroll_left = 256 + total_winnings
        if bet_amount > bankroll_left:
            bet_amount = bankroll_left

        if get_spin_result(win_prob):
            last_result = True
            total_winnings += bet_amount
            spin_results.append(bet_amount)
            results_by_spin.append(results_by_spin[i] + bet_amount)
        else:
            total_winnings -= bet_amount
            spin_results.append(-bet_amount)
            results_by_spin.append(results_by_spin[i] - bet_amount)

            if last_result:
                last_result = False
                bet_amount = 1
            else:
                bet_amount = bet_amount * 2

    return total_winnings, spin_results, results_by_spin


def experiment_two(win_prob):

    ## FIGURE FOUR ##
    results = []

    eighty = 0
    not_eighty = 0
    total_winnings_list = []

    for i in range(1000):
        total_winnings, spin_results, results_by_spin = simulate_episode_experiment_two(win_prob)
        results.append(results_by_spin)
        total_winnings_list.append(total_winnings)

        if total_winnings == 80:
            eighty += 1
        else:
            not_eighty += 1

    print(f'Eighty: {eighty}')
    print(f'Not Eighty: {not_eighty}')
    print(f'Proportion: {eighty/(eighty+not_eighty)}')
    print(f'Total Winnings Mean: {np.mean(total_winnings_list)}')

    transposed_data = zip(*results)
    means = []
    medians = []
    stds = []
    for col in transposed_data:
        means.append(np.mean(col))
        medians.append(np.median(col))
        stds.append(np.std(col, ddof=0))

    plt.plot(means)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Mean Accumulated Winnings ($)')
    plt.title('Figure 4 - Mean Accumulated Winnings ($)')
    plt.savefig('images/figure_four')
    plt.show()

    ## FIGURE FIVE ##
    upper = [m + s for m, s in zip(medians, stds)]
    lower = [m - s for m, s in zip(medians, stds)]

    plt.plot(medians, label="Median", color="blue")
    plt.plot(upper, label="Median + Std Dev", linestyle="--", color="green")
    plt.plot(lower, label="Median - Std Dev", linestyle="--", color="red")
    plt.xlim(0, 1000)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Median Accumulated Winnings ($)')
    plt.title('Figure 5 - Median Accumulated Winnings ($)')
    plt.legend()
    plt.savefig('images/figure_five')
    plt.show()


def test_code():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    win_prob = 18/38  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    print(get_spin_result(win_prob))  # test the roulette spin
    # add your code here to implement the experiments  		  	   		 	 	 		  		  		    	 		 		   		 		  

    experiment_one(win_prob)
    experiment_two(win_prob)


if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()
