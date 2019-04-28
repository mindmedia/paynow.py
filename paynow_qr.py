# in centos 7 this module can be installed using the following command.
# yum install python-qrcode
import qrcode

# module from https://pycrc.org
import pycrc.algorithms

PayNow_ID = "Company PayNow ID"
Merchant_name = "Company Name"
Bill_number = "Invoice Number"
Transaction_amount = "100.00"

Can_edit_amount = "0"
Merchant_category = "0000"
Transaction_currency = "702"
Country_code = "SG"
Merchant_city = "Singapore"
Globally_Unique_ID = "SG.PAYNOW"
Proxy_type = "2"

start_string = "010212"
Dynamic_PayNow_QR = "000201"
Globally_Unique_ID_field = "00"
Globally_Unique_ID_length = str(len(Globally_Unique_ID)).zfill(2)
Proxy_type_field = "01"
Proxy_type_length = str(len(Proxy_type)).zfill(2)
PayNow_ID_field = "02"
PayNow_ID_Length = str(len(PayNow_ID)).zfill(2)
Can_edit_amount_field = "03"
Can_edit_amount_length = str(len(Can_edit_amount)).zfill(2)
Merchant_category_field = "52"
Merchant_category_length = str(len(Merchant_category)).zfill(2)
Transaction_currency_field = "53"
Transaction_currency_length = str(len(Transaction_currency)).zfill(2)
Merchant_Account_Info_field = "26"
Merchant_Account_Info_length = str(len(Globally_Unique_ID_field + Globally_Unique_ID_length + Globally_Unique_ID + \
                                   Proxy_type_field + Proxy_type_length + Proxy_type + \
                                   PayNow_ID_field + PayNow_ID_Length + PayNow_ID + \
                                   Can_edit_amount_field + Can_edit_amount_length + Can_edit_amount)).zfill(2)

Transaction_amount_field = "54"
Transaction_amount_length = str(len(Transaction_amount)).zfill(2)
Country_code_field = "58"
Country_code_length = str(len(Country_code)).zfill(2)
Merchant_name_field = "59"
Merchant_name_length = str(len(Merchant_name)).zfill(2)
Merchant_city_field = "60"
Merchant_city_length = str(len(Merchant_city)).zfill(2)
Bill_number_field = "62"
Bill_number_sub_length = str(len(Bill_number)).zfill(2)
Bill_number_length = str(len("01" + Bill_number_sub_length + Bill_number)).zfill(2)

data_for_crc = Dynamic_PayNow_QR + start_string + Merchant_Account_Info_field + Merchant_Account_Info_length + \
       Globally_Unique_ID_field + Globally_Unique_ID_length + Globally_Unique_ID + \
       Proxy_type_field + Proxy_type_length + Proxy_type + \
       PayNow_ID_field + PayNow_ID_Length + PayNow_ID + \
       Can_edit_amount_field + Can_edit_amount_length + Can_edit_amount + \
       Merchant_category_field + Merchant_category_length + Merchant_category + \
       Transaction_currency_field + Transaction_currency_length + Transaction_currency + \
       Transaction_amount_field + Transaction_amount_length + Transaction_amount + \
       Country_code_field + Country_code_length + Country_code + \
       Merchant_name_field + Merchant_name_length + Merchant_name + \
       Merchant_city_field + Merchant_city_length + Merchant_city + \
       Bill_number_field + Bill_number_length + "01" + Bill_number_sub_length + Bill_number + \
       "6304"

#print (data_for_crc)

# Sample code from https://pycrc.org
crc = pycrc.algorithms.Crc(width = 16, poly = 0x1021,
          reflect_in = False, xor_in = 0xffff,
          reflect_out = False, xor_out = 0x0000)

my_crc = crc.bit_by_bit_fast(data_for_crc)          # calculate the CRC, using the bit-by-bit-fast algorithm.
crc_data = ('{:#04x}'.format(my_crc))
crc_data_upper = crc_data[-4:].upper()

final_string = data_for_crc + crc_data_upper

#print (final_string)

# example code from the following link.
# https://ourcodeworld.com/articles/read/554/how-to-create-a-qr-code-image-or-svg-in-python

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 5,
    border = 2,
)


# Add data
qr.add_data(final_string)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.png")
