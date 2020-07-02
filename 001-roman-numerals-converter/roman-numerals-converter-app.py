from flask import Flask, render_template, request

app = Flask(__name__)


def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman


user = 'Joe Blue'


@app.route('/', methods=['GET', 'POST'])
def main_entry():
    if request.method == 'POST':
        return result()
    else:
        return index()


def index(validity=True):
    return render_template('index.html', title='001- Roman Numerals Converter Application', user=user, validity=validity)


def result():
    raw_number = request.form['number']

    if not raw_number.isdecimal():
        # print("Not Decimal Number")
        return index(validity=False)

    number = int(raw_number)
    if not (0 < number < 4000):
        # print("Not In Range")
        return index(validity=False)

    return render_template('result.html', title='001- Roman Numerals Converter Application', user=user, input_number=number,
                           roman_number=convert(number))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #app.run()
