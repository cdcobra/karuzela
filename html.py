import pandas as pd

def htmlHead():
    head = (
        f'<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>'
        f'<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>'
        f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'
        f'<link href="https://cdn.jsdelivr.net/npm/bootstrap-utilities@4.1.3/bootstrap-utilities.min.css" rel="stylesheet">'
        f'<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>'
        f'<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/js/umd/util.js"></script>'        
        f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="3600" ><meta charset="UTF-8"><title>Karuzela</title></head><body style="background-color:black; height: 100%; display: grid; place-items: center;">'
    )
    return head

def htmlOptions():
    options = (
        f'<hr><hr><hr>'
        f'<div class="dropdown">'
        f'<button class="btn btn-secondary dropdown-toggle btn-sm" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
        f'Menu'
        f'</button>'        
        f'<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">'
        f'<label for="formFileSm" class="form-label">Opcje</label>'
        f'<a class="dropdown-item" href="default.xlsx">Default</a>'
        f'<a class="dropdown-item" href="promocje.xlsx">Aktualne promocje</a>'
        f'<hr>'
        f'<form action="/" method="post" enctype="multipart/form-data">'
        f'<label for="formFileSm" class="form-label">Podegraj nowe promocje</label>'
        f'<input class="form-control" type="file" id="formFile" name="formFile">'
        f'<button type="submit" class="btn btn-default">Wyślij</button> </form>'
        f'</div>'
        f'</div>'
    )
    return options

def htmlCarousel():    
    carousel = (
        f'<div class="container-fluid">'
        f'<div id="carouselContent" class="carousel slide" data-ride="carousel">'
        f'<div class="carousel-inner" role="listbox">'
        f'{cenowki()}'
        f'<a class="carousel-control-prev" href="#carouselContent" role="button" data-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Previous</span></a>'
        f'<a class="carousel-control-next" href="#carouselContent" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Next</span></a>'
        f'</div>'
        f'</div>'
        f'</div>'
    )
    return carousel

def cenowki():
    df = pd.read_excel('promocje.xlsx', sheet_name=0)
    ret = ''
    for idx,pozycja in df.iterrows():
        ret +=htmlCenowka(pozycja, 'active' if ret=='' else '')
    return ret

def htmlCenowka(poz, active):
    cenowka = (        
        f'<div class="carousel-item {active} text-center p-4">'
        f'<h1 style="color: grey; font-size: 50; font-weight: bold;">{poz["h1"]}</h>'
        f'<h1 style="color: grey; font-size: 30; font-weight: bold;">{poz["h2"]}</h>'
        f'<hr><hr><hr><hr><hr><hr><hr><hr>'
        f'<h1 style="color: white; font-size: 80;">{poz["produkt"]}</h>'
        f'<hr><hr><hr><hr><hr><hr><hr><hr>'
        f'<h1 style="color: red; font-size: 80; font-weight: bold;"><u>{poz["cena_netto"]:.2f} zł/{poz["jm"].lower()} netto</u></h>'
        f'<h1 style="color: green; font-size: 50;">{poz["cena_brutto"]:.2f} zł/{poz["jm"].lower()} brutto</h>'
        f'</div>'
    )
    return cenowka