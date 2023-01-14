{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9c0d8249-8f7f-43d5-8c76-e552099ee9df",
   "metadata": {},
   "source": [
    "# * old-school formatting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c8e425a1-3156-426f-b902-e1b78e5bb163",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one two\n",
      "one two\n",
      "1 2\n",
      "1 []\n"
     ]
    }
   ],
   "source": [
    "print('%s %s' %('one', 'two'))\n",
    "print('{} {}'.format('one', 'two'))\n",
    "print('%d %d' %(1, 2))\n",
    "print('{} []'.format(1, 2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6a349e3-7f2e-4860-8707-8692d3729ba0",
   "metadata": {},
   "source": [
    "### - % format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7879428d-226f-42f5-bfd5-6dc641e46ae6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I eat 3 apples.\n",
      "I eat five apples.\n"
     ]
    }
   ],
   "source": [
    "print(\"I eat %d apples.\" % 3)\n",
    "print(\"I eat %s apples.\" % \"five\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f858f7d9-42dc-4a1a-9fb1-64aa66216eb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i ate 3 apple. I was sick for there days.\n",
      "produt: Apple, Price per unit: 5.243000.\n"
     ]
    }
   ],
   "source": [
    "number = 3; \n",
    "day = \"there\"\n",
    "print(\"i ate %d apple. I was sick for %s days.\" % (number, day))\n",
    "print(\"produt: %s, Price per unit: %f.\" % (\"Apple\", 5.243))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c4afe526-2932-4a4f-8c04-ad2de92b02ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product:      Apple, Price per Unit:        5.2.\n"
     ]
    }
   ],
   "source": [
    "# 자리수 지정\n",
    "print(\"Product: %10s, Price per Unit: %10.1f.\" % (\"Apple\", 5.243))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "194469ec-112f-4984-9c03-f761d6221930",
   "metadata": {},
   "source": [
    "### - str.format() 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bc616621-5350-4569-b91a-c613667d5c77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm 37 years old.\n",
      "My name is cjs and 37 years old.\n",
      "Product: Apple, Price per unit:  5.243.\n"
     ]
    }
   ],
   "source": [
    "age = 37; \n",
    "name = 'cjs'\n",
    "print(\"I'm {0} years old.\".format(age))\n",
    "print(\"My name is {0} and {1} years old.\".format(name, age))\n",
    "print(\"Product: {0}, Price per unit: {1: .3f}.\".format(\"Apple\", 5.243))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d3ae7f3-7521-4b0f-9911-433dd3244c94",
   "metadata": {},
   "source": [
    "### - padding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "131b3236-7aae-4412-aafd-3fb1e6940769",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product: Apple, Price per unit: 5.24300\n",
      "Product: Apple, Price per unit: 5.24300\n",
      "Product:      Apple, Price per unit:      5.243\n",
      "Product:      Apple, Price per unit:      5.243\n",
      "Product: Apple     , Price per unit: 5.243     \n"
     ]
    }
   ],
   "source": [
    "print('Product: %5s, Price per unit: %.5f' % ('Apple', 5.243))\n",
    "print('Product: {0:5s}, Price per unit: {1:.5f}'.format('Apple', 5.243))\n",
    "print('Product: %10s, Price per unit: %10.3f' % ('Apple', 5.243))\n",
    "print('Product: {0:>10s}, Price per unit: {1:10.3f}'.format('Apple', 5.243))\n",
    "print('Product: {0:<10s}, Price per unit: {1:<10.3f}'.format('Apple', 5.243))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2014f36-0860-4673-94f9-05ab05c182a2",
   "metadata": {},
   "source": [
    "### - naming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f2179677-9d49-4bc7-8e25-1ddd8778775f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product:      Apple, Price per unit:    5.24300.\n",
      "Product:      Apple, Price per unit:    5.24300.\n"
     ]
    }
   ],
   "source": [
    "print(\"Product: %(name)10s, Price per unit: %(price)10.5f.\" % {\"name\":\"Apple\", \"price\":5.243})\n",
    "print(\"Product: {name:>10s}, Price per unit: {price:10.5f}.\".format(name=\"Apple\", price=5.243))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c7adfd8-0a5f-4c88-ae68-705cd185a11d",
   "metadata": {},
   "source": [
    "# f-string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b8dbedf9-372a-4a20-906e-e23707e7f38b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, cjs. You are 37.\n",
      "cjs                 \n",
      "                 cjs\n",
      "cjs*****************\n",
      "*****************cjs\n",
      "********cjs*********\n"
     ]
    }
   ],
   "source": [
    "name = \"cjs\"\n",
    "age = 37\n",
    "print(f\"Hello, {name}. You are {age}.\")\n",
    "print(f\"{name:20}\")\n",
    "print(f\"{name:>20}\")\n",
    "print(f\"{name:*<20}\")\n",
    "print(f\"{name:*>20}\")\n",
    "print(f\"{name:*^20}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "095b5096-aa3a-449f-bd4e-90a95b3ceffa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.14\n"
     ]
    }
   ],
   "source": [
    "number = 3.141592653589793\n",
    "print(f'{number:.2f}')"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
