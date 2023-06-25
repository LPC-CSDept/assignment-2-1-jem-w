def main():
    amount_m = int(input('Enter number of males: '))
    amount_f = int(input('Enter number of females: '))

    amount_tot = amount_m + amount_f

    m_perc = (amount_m / amount_tot) * 100
    f_perc = (amount_f / amount_tot) * 100

    print('The total number of students: \t', amount_tot)
    
    print(f'The percentage of males \t {m_perc:.2f}')

    print(f'The percentage of females \t {f_perc:.2f}')

    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
