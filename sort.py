{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f445ca5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]\n"
     ]
    }
   ],
   "source": [
    "a = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "a. sort()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9531d9c3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to function call (4246066791.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_8116\\4246066791.py\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    a(0) = a[len(a)-1]\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m cannot assign to function call\n"
     ]
    }
   ],
   "source": [
    "(2,3),(2,1)]\n",
    "b = a(0)a = [(2,5), (1,2), (4,4), \n",
    "a(0) = a[len(a)-1]\n",
    "print(a)\n",
    "a[len(a)-1] = b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "92e0aa2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 5)\n"
     ]
    }
   ],
   "source": [
    "l = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "t = l[0]\n",
    "l[0] = l[len(l)-1]\n",
    "print(t)\n",
    "l[len(l)-1] = t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9d25e3e0",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_8116\\3693329700.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "list = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "list(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "310d3d97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 1)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "list[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "88a2bf48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 5)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "list[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d436c120",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]\n"
     ]
    }
   ],
   "source": [
    "list = [(2,5), (1,2), (4,4), (2,3),(2,1)]\n",
    "list.sort()\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c0e8bf0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "list = [(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]\n",
    "p = list[0]\n",
    "list[0] = list[-1]\n",
    "list[-1] = p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "860605c8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_8116\\3019167673.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mlength\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mtemp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlength\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlength\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtemp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "list = [(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]\n",
    "length = len(list)\n",
    "temp = list(0)\n",
    "list[0] = list[length-1]\n",
    "list[length-1] = temp\n",
    "print(list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "452806a2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1eaeee99",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
