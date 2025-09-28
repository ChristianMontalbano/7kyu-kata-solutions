def maskify(cc_number):
    last_four = cc_number[-4:]
    cc_length = len(cc_number) - 4
    pound_sign = cc_length * "#"

    if len(cc_number) <= 4:
        return cc_number
    return pound_sign + last_four

def main():
    cc_number = "69694343434343434343434346464646464"
    final_number = maskify(cc_number)
    print(final_number)
    

main()


