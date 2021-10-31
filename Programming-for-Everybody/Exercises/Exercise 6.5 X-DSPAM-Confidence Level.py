'''
X-DSPAM-Confidence Level

    Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
    Convert the extracted value to a floating point number and print it out.
'''
data = "X-DSPAM-Confidence:    0.8475"

zeroposition = data.find('0')
# print(zeroposition)

endposition = zeroposition+6
# print(endposition)

confidencelevel = float(data[zeroposition : endposition])

print(confidencelevel)