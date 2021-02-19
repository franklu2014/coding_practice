#!/usr/bin/env python
# coding: utf-8

def main():
    while True:
        inp = input('Please enter the income below, enter a string if want to exit\n...=> ')
        try:
            inp = float(inp)
        except:
            break
        brackets = [
            41725,
            41726,
            12361,
            20532,
            41404,
            62252,
            float('inf')
        ]
        rates = [
            5.06,
            7.7, 
            10.5,
            12.29,
            14.7,
            16.8,
            20.5
        ]
        rates = map(lambda x : x * 0.01, rates)
        rules = list(zip(brackets, rates))

        income = inp
        tax = 0.0
        for th, r in rules:
            if income > th:
                income = income - th
                tax += th * r
            else:
                tax += income * r
                break

        print(f'Income = {inp}, tax = {tax:.2f}, net = {inp - tax:.2f}')

if __name__ == '__main__':
    main()