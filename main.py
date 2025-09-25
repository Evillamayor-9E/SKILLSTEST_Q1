from pyscript import display, document

def ordering_form(e):
    document.getElementById("output2").innerHTML = ""
    Food1 = document.getElementById('menu1')
    Food2 = document.getElementById('menu2')
    Food3 = document.getElementById('menu3')

    total = (float(Food1.value) * Food1.checked + 
             float(Food2.value) * Food2.checked + 
             float(Food3.value) * Food3.checked)
    
    display(f'The total amount is {total}', target='output2')

def collecting_data(e):
    document.getElementById("output").innerHTML = ""
    first = document.getElementById("fn").value
    address = document.getElementById("ad").value
    phone = document.getElementById("ph").value

    display(f"Order For: {first} Address: {address} Contact Number: {phone}", target="output")
