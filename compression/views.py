from django.shortcuts import render
from . import mn
from .forms import TextForm
from django.http import JsonResponse

import json


def encode(request):
    context = {}

    if request.POST:
        data = request.POST['txt']

        ans = mn.ee(data)
        context = {
            'data': data,
            'encrypted': ans[0],
            'huffman_encoded': ans[1],
            'hamming_encoded': ans[2],
            'with_errors': ans[3],
            'corrected': ans[4],
            'hamming_decoded': ans[5],
            'huffman_decoded': ans[6],
            'decrypted': ans[7],
            'before': ans[8][0],
            'after': ans[8][1],
            'comratio': ans[8][0]/ans[8][1],
        }

    return render(request, 'encoding.html', context=context)


def mainPage(request):
    return render(request, 'index.html')
