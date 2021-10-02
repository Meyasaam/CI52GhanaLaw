""" This program calculates the interest on judgment debt in Ghana in accordance with Court (Award of Interest and Post
Judgment Interest) Rules, 2005 (C.I. 52). Simple interest method is applied to the judgment debt at the prevailing
statutory interest rate; where no interest rate and method for interest calculation has been specified by a statute or
the contract between the parties.

Example: A judge awards the following:
"1. GH₵98,000 being arrears of rent due and owing from the Defendant in respect of the said premises;
 2. Interest thereon at the prevailing rate from the 30th day of November 2016 till date of this judgment."
Assuming date of judgment is 30 September 2021 and interest rate is 3.25%.
date1 = 2016/11/30; date2 = 2021/09/30; interest_rate = 3.25; principal = GH₵98000.

"""

from datetime import datetime


def main():
    date1 = input("(dd/mm/yyyy): ")
    date1 = datetime.strptime(date1, '%d/%m/%Y')
    # converts string from input to datetime
    date2 = input("(dd/mm/yyyy): ")
    date2 = datetime.strptime(date2, '%d/%m/%Y')
    period = (date2 - date1).total_seconds()
    # converts the units of "period" from days to seconds so calculations can be done using float.
    principal = input("principal = ")
    interest_rate = input("interest rate = ")
    interest_rate = float(interest_rate)/100
    interest = (float(principal) * interest_rate * period)/31536000
    # 31536000 seconds = 1 year
    interest = round(interest, 2)
    print('Interest on judgment debt is: GH₵' + str(interest))


# This provided line is required at the end of a Python program to call the main() function.
if __name__ == '__main__':
    main()
